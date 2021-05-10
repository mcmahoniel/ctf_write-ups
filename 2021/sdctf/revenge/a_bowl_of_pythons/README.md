# A Bowl of Pythons

## Challenge:

A bowl of spaghetti is nice. What about a bowl of pythons?

**chal.py**

https://cdn.discordapp.com/attachments/840060278204006440/840065069894074398/chal.py

## Solution:

We're provided with some obfuscated Python:

```python
#! /usr/bin/env python3
FLAG = 'sdctf{a_v3ry_s3cur3_w4y_t0_st0r3_ur_FLAG}' # lol

a = lambda n: a(n-2) + a(n-1) if n >= 2 else (2 if n == 0 else 1)

b = lambda x: bytes.fromhex(x).decode()

h = eval(b('7072696e74'))

def d():
    h(b('496e636f727265637420666c61672120596f75206e65656420746f206861636b206465657065722e2e2e'))
    eval(b('5f5f696d706f72745f5f282273797322292e65786974283129'))
    h(FLAG)

def e(f):
    h("Welcome to SDCTF's the first Reverse Engineering challenge.")
    c = input("Input the correct flag: ")
    if c[:6].encode().hex() != '{2}3{0}{1}{0}3{2}{1}{0}{0}{2}b'.format(*map(str, [6, 4, 7])):
        d()
    if c[int(chr(45) + chr(49))] != chr(125):
        d()
    g = c[6:-1].encode()
    if bytes( (g[i] ^ (a(i) & 0xff) for i in range(len(g))) ) != f:
        d()
    h(b('4e696365206a6f622e20596f7520676f742074686520636f727265637420666c616721'))

if __name__ == "__main__":
    e(b't2q}*\x7f&n[5V\xb42a\x7f3\xac\x87\xe6\xb4')
else:
    eval(b('5f5f696d706f72745f5f282273797322292e65786974283029'))
```

Sadly, the flag at the beginning is _not_ our flag.

Running `chal.py` confirms that text is being read from somewhere:

```bash
$ python chal.py                                                                                                                                                                                                                                                                                                               126 ↵
Welcome to SDCTF's the first Reverse Engineering challenge.
Input the correct flag: sctf{???}
Incorrect flag! You need to hack deeper...
```

We find that `b` decodes our binary text data and `h` is just `print()`:

```python
>>> b = lambda x: bytes.fromhex(x).decode()
>>> h = eval(b('7072696e74'))
>>> h
<built-in function print>
>>> b('7072696e74')
'print'
>>> b('496e636f727265637420666c61672120596f75206e65656420746f206861636b206465657065722e2e2e')
'Incorrect flag! You need to hack deeper...'
```

There are some additions just to throw us off the scent. The follow makes sure our flag looks like `sdctf{...}`, and sets `g` to everything between the curly braces:

```python
    if c[:6].encode().hex() != '{2}3{0}{1}{0}3{2}{1}{0}{0}{2}b'.format(*map(str, [6, 4, 7])):
        d()
    if c[int(chr(45) + chr(49))] != chr(125):
        d()
    g = c[6:-1].encode()
```

The main portion is this:

```python
    if bytes( (g[i] ^ (a(i) & 0xff) for i in range(len(g))) ) != f:
```

This encodes our input and compares it to the encoded flag in the source:

```python
e(b't2q}*\x7f&n[5V\xb42a\x7f3\xac\x87\xe6\xb4')
```

We can reverse the encoder and get our flag: 

```
def solve(answer):
    for i in range(20):
        print((a(i) & 0xff) ^ answer[i])

if __name__ == "__main__":
    solve(b't2q}*\x7f&n[5V\xb42a\x7f3\xac\x87\xe6\xb4')
```

```
$ python modified.py
118
51
114
121
45
116
52
115
116
121
45
115
112
104
52
103
51
116
116
49
```

We can use `chr(...)` to get the characters of the flag, giving us `v3ry-t4sty-sph4g3tt1`.

Now we have our flag: `sdctf{v3ry-t4sty-sph4g3tt1}`.
