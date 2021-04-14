# snek

## Challenge:

No step on snek

## Solution:

We have a file called `snek`:
```
$ file snek
snek: python 3.7 byte-compiled
```
So instead of a binary this is a compiled Python file (usually a `.pyc`). We also know the specific version of Python.


Let’s try to run it:
```
$ python snek
Enter my name: Foo
WRONG
```
We can open `snek` directly, but it’s mostly gibberish. Running `strings` also doesn’t help. We’ll need to decompile the code to see what’s going on.

If we look up how to decompile byte-compiled Python, we’ll probably come across [this Stack Overflow question](https://stackoverflow.com/questions/5287253/is-it-possible-to-decompile-a-compiled-pyc-file-into-a-py-file) which presents some options. Let’s try `uncompyle6`:
```
$ pip install uncompyle6
...
$ uncompyle6 snek
# file snek
# path snek must point to a Python source that can be compiled, or Python bytecode (.pyc, .pyo)
```
Easy enough:
```
$ mv snek snek.pyc
$ uncompyle6 snek.pyc > snek.py
$ cat snek.py
# uncompyle6 version 3.7.4
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.7.10 (default, Apr 10 2021, 18:08:58)
# [Clang 12.0.0 (clang-1200.0.32.29)]
# Embedded file name: snek.py
# Compiled at: 2021-04-08 07:24:05
# Size of source mod 2**32: 834 bytes
"""
Written for RITSEC CTF 2021
Author: knif3
Flag: RITSEC{}

TODO: Finish this challenge
"""

class d(object):

    def __init__(self, password):
        self.password = password.encode()
        self.decrypt = [97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 95, 82, 83, 123, 97, 108, 108, 95, 104, 105, 36, 36, 95, 97, 110, 100, 95, 110, 48, 95, 98, 105, 116, 51, 125]

    def __eq__(self, other):
        if self.password == bytes(self.decrypt):
            print('!flag')
            return True
        return False


x = input('Enter my name: ')
a = d(x)
if a == x:
    print('IS_THIS_THE_FLAG??')
    print('NOPE')
else:
    print('WRONG')
# okay decompiling snek.pyc
```
We now have the decompiled script and can see that our input is encoded and compared against the encoded flag. We also see an interesting string, “TODO: Finish this challenge”. Could it be that there isn’t actually any encryption happening here?

We can drop it into Cyberchef using the Magic recipe. And... nothing. But if we [remove the commas](https://gchq.github.io/CyberChef/#recipe=Magic(3,false,false,'')&input=OTcgOTggOTkgMTAwIDEwMSAxMDIgMTAzIDEwNCAxMDUgMTA2IDEwNyAxMDggMTA5IDExMCAxMTEgMTEyIDExMyAxMTQgMTE1IDExNiAxMTcgMTE4IDExOSAxMjAgMTIxIDEyMiA2NSA2NiA2NyA2OCA2OSA3MCA3MSA3MiA3MyA3NCA3NSA3NiA3NyA3OCA3OSA4MCA4MSA4MiA4MyA4NCA4NSA4NiA4NyA4OCA4OSA5MCA5NSA4MiA4MyAxMjMgOTcgMTA4IDEwOCA5NSAxMDQgMTA1IDM2IDM2IDk1IDk3IDExMCAxMDAgOTUgMTEwIDQ4IDk1IDk4IDEwNSAxMTYgNTEgMTI1):

<img src="magic.png" alt="Secret flag." width="600">

We now see our flag: `RS{all_hi$$_and_n0_bit3}`.
