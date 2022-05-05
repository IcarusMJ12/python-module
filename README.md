# Module

Python modules are hard.  `module` attempts to make them easier to write in the interpreter.
Here's a quick usage example:


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
