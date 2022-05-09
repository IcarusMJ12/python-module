# ModuleMeta

Python modules are hard.  `modulemeta` attempts to make them easier to write in the interpreter.

## Basic Usage

```
>>> from modulemeta import Module
>>> class Wat(metaclass=Module):
...   _ermelon = 5
...
...   def ermelon():  # type: ignore[misc]
...     return _ermelon
...
>>> Wat.ermelon()
5
>>> Wat
<module 'Wat'>
```


## Inheritance

Shockingly, modules cannot be inherited from, therefore they are treated as metaclasses:

```
from modulemeta import Module


class Wat(metaclass=Module):
  pass


class Wat2(metaclass=Wat):  # type: ignore[misc]
  pass
```
