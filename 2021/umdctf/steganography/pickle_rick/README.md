# Pickle Rick

## Challenge:

You recieve these audio files from someone named Alan Eliasen.

https://drive.google.com/drive/folders/135epDZ18MdIycbBt_Fekbi8hdF-83v6Y?usp=sharing

## Solution:

We have two WAV files with two Rick Astley songs, the classic Never Gonna Give You Up and Together Forever.

If we run a Google search for “Alan Eliasen” we find a page discussing steganography tools and an online version of `steghide`. If we upload `rickroll.wav`, we get an error. However, `together-forever-encoded.wav` decodes immediately to `The password is "big_chungus"!`.

Let’s try that password to decode `rickroll.wav`...

And we have our flag: `UMDCTF-{n3v3r_g0nna_l3t_y0u_d0wn}`.
