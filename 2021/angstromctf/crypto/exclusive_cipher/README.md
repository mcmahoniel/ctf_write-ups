# Exclusive Cipher

## Challenge:

Clam decided to return to classic cryptography and revisit the XOR cipher! Here's some hex encoded ciphertext:

```
ae27eb3a148c3cf031079921ea3315cd27eb7d02882bf724169921eb3a469920e07d0b883bf63c018869a5090e8868e331078a68ec2e468c2bf13b1d9a20ea0208882de12e398c2df60211852deb021f823dda35079b2dda25099f35ab7d218227e17d0a982bee7d098368f13503cd27f135039f68e62f1f9d3cea7c
```

The key is 5 bytes long and the flag is somewhere in the message.

## Solution:

We know the key is 5 bytes long. And we have a crib, `actf{`.

But before we do any work, let's try a [decoder](https://www.dcode.fr/xor-cipher). We can limit it to a 5 byte key and tell it that we're expecting ASCII.

Running it, we immediately get our flag: `actf{who_needs_aes_when_you_have_xor}`.
