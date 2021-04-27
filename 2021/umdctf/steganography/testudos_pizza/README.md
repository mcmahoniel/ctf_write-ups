# Testudo's Pizza

## Challenge:

My local pizzeria is trying out a new logo that is bringing in a lot of new customers. I think something fishy is going on. What are they doing?

## Solution:

We have a single image:

<img src="hiddenmsg.jpg" alt="Pie" width="200">

Let's take a quick look at the strings:

```bash
$ strings hiddenmsg.jpg | grep UMDCTF
\f0\fs24 \cf0 \'93UMDCTF-{W3_ar3_th3_b3st_P1ZZ3r1a}\'94}
```

And our flag is revealed: `UMDCTF-{W3_ar3_th3_b3st_P1ZZ3r1a}`.
