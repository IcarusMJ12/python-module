from copy import deepcopy
import sys
import types


class Module(type):
  def __new__(cls, name, bases, attr):
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
        module.__dict__[k] = types.FunctionType(v.__code__, vars(module), v.__name__, v.__defaults__, v.__closure__)
    return ModuleWrapper(module)


class ModuleWrapper:
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


sys.modules[__name__] = Module
