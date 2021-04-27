# BF means best friend, right?

## Challenge:

We only got part of Melon Eusk's program that prints out their password. Looks like it creates the right string in memory but does not print, see if you can figure out what it is (wrap the string in flag{}).

## Solution:

If we check the provided file, it seems to be plain text:

```
$ file main.bf
main.bf: ASCII text, with no line terminators
```

It’s instantly recognizable as [Brainfuck](https://en.wikipedia.org/wiki/Brainfuck):

```
--[----->+<]>----[-<+>]+[--------->++<]>[-<+>]--[----->+<]>-----[-<+>]+[----->+++<]>++[-<+>]+[------->++<]>[-<+>]++[------>+<]>++[-<+>]--[----->+<]>----[-<+>]+[------->++<]>--[-<+>]--[----->+<]>-----[-<+>]+[--------->++<]>+[-<+>]--------[-->+++<]>[-<+>]
```

We can plug it into [an interpreter](https://www.dcode.fr/brainfuck-language):

```
Memory:
[0] = b (98)
[1] = r (114)
[2] = a (97)
[3] = i (105)
[4] = n (110)
[5] = - (45)
[6] = b (98)
[7] = l (108)
[8] = a (97)
[9] = s (115)
[10] = t (116)
```

And there’s the flag: `flag{brain-blast}`.
