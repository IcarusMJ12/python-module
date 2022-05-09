"""
Exposes the `Module` metaclass that makes your classes behave like modules.
"""


from copy import deepcopy
import types


class _ModuleWrapper:
  """
  A class that wraps a module and passes all attribute requests to it.

  Also wraps __name__, __doc__, and __repr__ a la `functools.wraps`.
  """

  def __init__(self, module):
    self._module = module
    self.__name__ = module.__name__
    self.__doc__ = module.__doc__

  def __getattr__(self, attr):
    return getattr(self._module, attr)

  def __repr__(self):
    return self._module.__repr__()

  def __call__(self, name, _, attr):
    return Module.__new__(_, name, (self._module,), attr)


class Module(type):
  """
  A metaclass that makes your classes have module level scope and lets you
  define functions instead of methods.  Such scoping for internally defined
  classes is not currently supported.

  Modules do not have inheritance, but you can "single inherit" by providing
  the resultant class as a metaclass.

  Note also that the resultant class is not of type `type` and this will result
  in errors with type checkers like `mypy`.
  """

  def __new__(cls, name: str,  # type: ignore[misc]
              bases: tuple[types.ModuleType], attr: dict) -> _ModuleWrapper:
    module = types.ModuleType(name=name)
    for base in bases:
      for key in dir(base):
        if key.startswith('__'):
          continue
        module.__dict__[key] = deepcopy(getattr(base, key))
    for key, value in attr.items():
      module.__dict__[key] = value
    for k, v in module.__dict__.items():
      if isinstance(v, types.FunctionType):
        module.__dict__[k] = types.FunctionType(
            v.__code__, vars(module), v.__name__, v.__defaults__,
            v.__closure__)
    return _ModuleWrapper(module)
