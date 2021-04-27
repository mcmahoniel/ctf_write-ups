# Coldplay's Flags

## Challenge:

I just downloaded Coldplay's latest song and noticed that my song file seems a bit odd. Can you help me figure out what's up with my file?

Note: For the password, think words, not characters

https://drive.google.com/drive/folders/1e0D5LElerPu9VcUm2bKp5j542CLuNadB?usp=sharing
## Solution:

The audio file plays normally, no indication of anything off.

But if we run `binwalk`, we can see two compressed files embedded in our WAV:

```bash
$ binwalk -e flags.wav

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
712822        0xAE076         MySQL ISAM compressed data file Version 1
845224        0xCE5A8         MySQL ISAM index file Version 1
6088742       0x5CE826        MySQL MISAM index file Version 3
6936308       0x69D6F4        MySQL ISAM compressed data file Version 1
20443148      0x137F00C       MySQL ISAM compressed data file Version 6
27679314      0x1A65A52       MySQL MISAM index file Version 5
28755155      0x1B6C4D3       MySQL MISAM index file Version 8
35886544      0x22395D0       MySQL MISAM compressed data file Version 1
36095154      0x226C4B2       MySQL ISAM compressed data file Version 4
38195278      0x246D04E       Zip archive data, encrypted at least v1.0 to extract, compressed size: 45, uncompressed size: 33, name: flag.txt
38195483      0x246D11B       End of Zip archive, footer length: 22
38195505      0x246D131       Zip archive data, at least v2.0 to extract, compressed size: 82, uncompressed size: 97, name: hint.txt
38195731      0x246D213       End of Zip archive, footer length: 22
```

Unfortunately, `flags.txt` is in an encrypted archive, but `hint.txt` gives us a clue.

```bash
$ cat hint.txt
Assume all characters are lowercase
password: (1:49)_(1:01)_(0:16)_(0:56)_(0:17)_(1:33)_a_(1:34)?
```

Are these timestamps in the song?

```bash
1:49: can
1:01: tchaikovsky
0:16: talk
0:56: to
0:17: skeletons
1:33: by
1:34: ouija
```

Attempting to extract `flags.txt` with the password `can_tchaikovsky_talk_to_skeletons_by_a_ouija?` works!

We can see our flag: `UMDCTF-{PY07r_11Y1CH_7CH41K0V5KY}`.
