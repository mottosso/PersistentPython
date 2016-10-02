# Persistent Python

Persistent Python interpreter for Sublime Text 3.

> WARNING: proof of concept

<br>

### Install

Choose **one** of the following methods.

1. Search for `PersistentPython` in Package Control.
2. Clone this repository into your `packages/` directory.

<br>

### Overview

Like the interactive Python interpreter, this plug-in enables code to run in an interpreter that remembers state from previous runs.

```python
>>> import sys
<RUN>
>>> executable = sys.executable
>>> print(executable)
<RUN>
'c:\python27\python.exe'
```
