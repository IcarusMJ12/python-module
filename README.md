# Module

Python modules are hard.  This module attempts to make them easier to write.
Here's a quick usage example.


```
>>> import module
>>> class Foo(metaclass=module):
...   bar = 7
...
...   def baz():
...     return bar
...
>>> Foo.baz()
7
>>>
>>> Foo
<module 'Foo'>
>>> module
<class 'module.Module'>
```
