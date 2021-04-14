# Keysar v2

## Challenge:

Wow! Aplet sent me a message... he said he encrypted it with a key, but lost it. Gotta go though, I have biology homework!

[Source](https://files.actf.co/45d2f41c58c51d0e7eeeac6b4fae4b01fca1427bd8e8d2cf5a127b8d7abfcdee/chall.py) [Output](https://files.actf.co/8125825ae0a5c81fe0f3e4520b95c02937a4d6624929afec84e451366ede6552/out.txt)

## Solution:

We’re given a Python script to encrypt text along with the ciphertext containing our flag. The script loads two files containing the plaintext and a key and it shifts the plaintext to generate the ciphertext.

To make this easy, we can throw our ciphertext into [a tool](https://www.boxentriq.com/code-breaking/cipher-identifier) to identify the type of cipher we’re dealing with. It quickly identifies this as a monoalphabetic substitution cipher. Next, we can put it into an [automatic decoder](https://www.boxentriq.com/code-breaking/cryptogram).

Almost immediately, we’re greeted with the familiar Bee Movie script and our flag: `actf{keyedcaesarmorelikesubstitution}`.
