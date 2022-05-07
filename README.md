# Module

Python modules are hard.  `module` attempts to make them easier to write in the interpreter.

## Basic Usage

```
>>> import module
>>> class Wat(metaclass=module):
...   _ermelon = 5
...
...   def ermelon():
...     return _ermelon
...
>>> Wat.ermelon()
5
>>> Wat
<module 'Wat'>
>>> module
<class 'module.Module'>
```


## Inheritance

Shockingly, modules cannot be inherited from, therefore they are treated as metaclasses:

```
import module


class Wat(metaclass=module):
  pass


class Wat2(metaclass=Wat):
  pass
```
