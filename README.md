# Persistent Python

Persistent Python interpreter for Sublime Text 3.

> WARNING: proof of concept

<br>

### Usage

1. Install this plug-in
2. Ctrl + Shift + B and select "Persistent Python" to build
3. Ctrl + B or F7 to build all or selected text
4. (optional) Press Ctrl + Enter to build

If no text is selected, the entire view is built and cleared.

Enable/disable the package as per usual via "Enable Package" and "Disable Package" commands.

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