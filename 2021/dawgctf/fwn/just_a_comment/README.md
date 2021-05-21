# Just A Comment

## Challenge:

Just a comment, we love our people here at ClearEdge!

justacomment.pcapng: https://drive.google.com/file/d/1vcLdCLi-zYTe_WPtXyu2Gr3rM0a3Ct7h/view?usp=sharing

## Solution:

We're provided a `.pcapng` file. Normally we would load this up in Wireshark or another tool to analyze, but all it takes is `strings`:

```bash
$ strings justacomment.pcapng | grep DawgCTF
DawgCTF{w3 h34r7 0ur 1r4d 734m}
```

There it is: `DawgCTF{w3 h34r7 0ur 1r4d 734m}`.
