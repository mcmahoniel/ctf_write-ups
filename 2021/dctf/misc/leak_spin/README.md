# Leak Spin

## Challenge:

We have confident insider report that one of the flags was leaked online. Can you find it?

Hint: The organisers only control a limited amount of places on the internet, looks through those...

## Solution:

The obvious first place to check is https://dragonsec.si/. There doesn’t seem to be anything there, but there are links to Twitter and GitHub.

Their [GitHub account](https://github.com/DragonSecSI) only has three repositories, one of which says “Make sure to keep this info private!” It only has [two files](https://github.com/DragonSecSI/DCTF1-chall-leak-spin), the README and `challenge.yml`.

If we open that up:

```
name: "Leak Spin"
author: "Miha M."
category: Web

description: We have confident insider report that one of the flags was leaked online. Can you find it?
value: 100
type: standard

flags:
  - dctf{I_L1k3_L1evaAn_P0lkk4}

tags:
  - web

state: visible
 
version: "1.0"
```

We have our flag: `dctf{I_L1k3_L1evaAn_P0lkk4}`.
