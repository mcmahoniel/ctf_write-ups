# cookin the ramen

## Challenge:

Apparently we made cookin the books too hard, here's some ramen to boil as a warmup: .--- ...- ...- . ....- ...- ... ..--- .. .-. .-- --. -.-. .-- -.- -.-- -. -... ..--- ..-. -.-. ...- ...-- ..- --. .--- ... ..- .. --.. -.-. .... -- ...- -.- . ..- -- - . -. ...- -. ..-. --- -.-- --.. - .-.. .--- --.. --. --. ...-- ... -.-. -.- ..... .--- ..- --- -. -.- -..- -.- --.. -.- ...- ..- .-- - -.. .--- -... .... ..-. --. --.. -.- -..- .. --.. .-- ...- ... -- ...-- --.- --. ..-. ... .-- --- .--. .--- .....

## Solution:

It's pretty clear that we're looking at [Morse code](https://en.wikipedia.org/wiki/Morse_code).

We can convert it to readable text [in CyberChef](https://gchq.github.io/CyberChef/#recipe=From_Morse_Code('Space','Forward%20slash')&input=Li0tLSAuLi4tIC4uLi0gLiAuLi4uLSAuLi4tIC4uLiAuLi0tLSAuLiAuLS4gLi0tIC0tLiAtLi0uIC4tLSAtLi0gLS4tLSAtLiAtLi4uIC4uLS0tIC4uLS4gLS4tLiAuLi4tIC4uLi0tIC4uLSAtLS4gLi0tLSAuLi4gLi4tIC4uIC0tLi4gLS4tLiAuLi4uIC0tIC4uLi0gLS4tIC4gLi4tIC0tIC0gLiAtLiAuLi4tIC0uIC4uLS4gLS0tIC0uLS0gLS0uLiAtIC4tLi4gLi0tLSAtLS4uIC0tLiAtLS4gLi4uLS0gLi4uIC0uLS4gLS4tIC4uLi4uIC4tLS0gLi4tIC0tLSAtLiAtLi0gLS4uLSAtLi0gLS0uLiAtLi0gLi4uLSAuLi0gLi0tIC0gLS4uIC4tLS0gLS4uLiAuLi4uIC4uLS4gLS0uIC0tLi4gLS4tIC0uLi0gLi4gLS0uLiAuLS0gLi4uLSAuLi4gLS0gLi4uLS0gLS0uLSAtLS4gLi4tLiAuLi4gLi0tIC0tLSAuLS0uIC4tLS0gLi4uLi4). That gives us a long string:

```bash
JVVE4VS2IRWGCWKYNB2FCV3UGJSUIZCHMVKEUMTENVNFOYZTLJZGG3SCK5JUONKXKZKVUWTDJBHFGZKXIZWVSM3QGFSWOPJ5
```

Using the [Magic operation](https://gchq.github.io/CyberChef/#recipe=From_Morse_Code('Space','Forward%20slash')Magic(3,false,false,'DawgCTF')&input=Li0tLSAuLi4tIC4uLi0gLiAuLi4uLSAuLi4tIC4uLiAuLi0tLSAuLiAuLS4gLi0tIC0tLiAtLi0uIC4tLSAtLi0gLS4tLSAtLiAtLi4uIC4uLS0tIC4uLS4gLS4tLiAuLi4tIC4uLi0tIC4uLSAtLS4gLi0tLSAuLi4gLi4tIC4uIC0tLi4gLS4tLiAuLi4uIC0tIC4uLi0gLS4tIC4gLi4tIC0tIC0gLiAtLiAuLi4tIC0uIC4uLS4gLS0tIC0uLS0gLS0uLiAtIC4tLi4gLi0tLSAtLS4uIC0tLiAtLS4gLi4uLS0gLi4uIC0uLS4gLS4tIC4uLi4uIC4tLS0gLi4tIC0tLSAtLiAtLi0gLS4uLSAtLi0gLS0uLiAtLi0gLi4uLSAuLi0gLi0tIC0gLS4uIC4tLS0gLS4uLiAuLi4uIC4uLS4gLS0uIC0tLi4gLS4tIC0uLi0gLi4gLS0uLiAuLS0gLi4uLSAuLi4gLS0gLi4uLS0gLS0uLSAtLS4gLi4tLiAuLi4gLi0tIC0tLSAuLS0uIC4tLS0gLi4uLi4), we find that this has been encoded a few times.

We can Base32 decode, Base64 decode, and Base58 decode to [see our flag](https://gchq.github.io/CyberChef/#recipe=From_Morse_Code('Space','Forward%20slash')From_Base32('A-Z2-7%3D',true)From_Base64('A-Za-z0-9%2B/%3D',true)From_Base58('123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz',true)&input=Li0tLSAuLi4tIC4uLi0gLiAuLi4uLSAuLi4tIC4uLiAuLi0tLSAuLiAuLS4gLi0tIC0tLiAtLi0uIC4tLSAtLi0gLS4tLSAtLiAtLi4uIC4uLS0tIC4uLS4gLS4tLiAuLi4tIC4uLi0tIC4uLSAtLS4gLi0tLSAuLi4gLi4tIC4uIC0tLi4gLS4tLiAuLi4uIC0tIC4uLi0gLS4tIC4gLi4tIC0tIC0gLiAtLiAuLi4tIC0uIC4uLS4gLS0tIC0uLS0gLS0uLiAtIC4tLi4gLi0tLSAtLS4uIC0tLiAtLS4gLi4uLS0gLi4uIC0uLS4gLS4tIC4uLi4uIC4tLS0gLi4tIC0tLSAtLiAtLi0gLS4uLSAtLi0gLS0uLiAtLi0gLi4uLSAuLi0gLi0tIC0gLS4uIC4tLS0gLS4uLiAuLi4uIC4uLS4gLS0uIC0tLi4gLS4tIC0uLi0gLi4gLS0uLiAuLS0gLi4uLSAuLi4gLS0gLi4uLS0gLS0uLSAtLS4gLi4tLiAuLi4gLi0tIC0tLSAuLS0uIC4tLS0gLi4uLi4): `DawgCTF{0k@y_r3al_b@by's_f1r5t}`.
