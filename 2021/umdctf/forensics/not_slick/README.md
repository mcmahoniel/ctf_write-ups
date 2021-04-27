# Not Slick

## Challenge:

My friend always messes with PNGs.... what did he do this time?

## Solution:

All we have a is [a broken PNG](notslick.png).

Running `file` doesn't give us much:

```bash
$ file notslick.png
notslick.png: data
```

Which isn't surprising, the [file signature](https://en.wikipedia.org/wiki/List_of_file_signatures) doesn't seem to match anything:

```bash
$ xxd notslick.png | head
00000000: 8260 42ae 444e 4549 0000 0000 2b2c edb5  .`B.DNEI....+,..
...
```

But if we run a Google search for `B.DNEI`, we find some other CTF challenges that indicate that this is actually a reversed PNG.

Sure enough, we can see the telltale indicator of a PNG at the end of the file:

```bash
$ xxd notslick.png | tail
...
00018c80: 8007 0000 5244 4849 0d00 0000 0a1a 0a0d  ....RDHI........
00018c90: 474e 5089                                GNP.
```

Repurposing a script borrowed from [this CTF write-up](https://ctftime.org/writeup/18056), we can repair our PNG:

<img src="reversed.png" alt="GNP" width="600">

That gives us our flag: `UMDCTF-{abs01ute1y_r3v3r53d}`.
