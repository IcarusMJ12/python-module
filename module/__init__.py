import sys
import types


class Module(type):
  def __new__(cls, name, bases, attr):
    module = types.ModuleType(name=name)
    for key, value in attr.items():
      module.__dict__[key] = value
    for k, v in module.__dict__.items():
      if isinstance(v, types.FunctionType):
        module.__dict__[k] = types.FunctionType(v.__code__, vars(module), v.__name__, v.__defaults__, v.__closure__)
    return module


sys.modules[__name__] = Module
