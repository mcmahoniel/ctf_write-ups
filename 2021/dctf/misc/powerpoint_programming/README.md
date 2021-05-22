# Powerpoint programming

## Challenge:

A login page in powerpoint should be good enough, right?

Flag is not in format. DCTF{ALL_CAPS_LETTERS_OR_NUMBERS}

## Solution:

If we open up the presentation in Keynote and select a key, we see an Order value that might correspond to when we should press that key. If we drag a key off, we can see that there are layers so keys can be pressed more than once:

<img src="order.png" alt="One by One" width="600">

One by one, we can find the Order values for each key:

```bash
1: 19, 59, 53
3: 31, 49, 41, 
C: 3, 43
D: 1
F: 7
N: 23
P: 13, 11
R: 47, 33
S: 21, 55, 39
T: 25, 15, 5, 61
U: 45
V: 29
Y: 35
{: 9
}: 63
_: 27, 17, 57, 51, 37
```

Now we just need to put these in their relative order to get our flag: `DCTF{PPT_1SNT_V3RY_S3CUR3_1S_1T}`.
