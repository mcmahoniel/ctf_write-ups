# Archaic

## Challenge:

The archaeological team at ångstromCTF has uncovered an archive from over 100 years ago! Can you read the contents?

Access the file at `/problems/2021/archaic/archive.tar.gz` on the shell server.

## Solution:

Our flag is sitting in a tarball on the shell server. Let's try to extract it:

```
team8317@actf:/problems/2021/archaic$ tar zxvf archive.tar.gz
flag.txt
tar: flag.txt: Cannot open: Operation not permitted
tar: Exiting with failure status due to previous errors
```

It looks like we don't have write access here. Let's try to extract to our home folder instead:

```
team8317@actf:/problems/2021/archaic$ tar zxvf archive.tar.gz -C /home/team8317/
flag.txt
tar: flag.txt: implausibly old time stamp 1921-04-01 22:45:12
```

It looks like that worked! Now to open up the flag:

```
team8317@actf:/problems/2021/archaic$ cat ~/flag.txt
cat: /home/team8317/flag.txt: Permission denied
```

Alright, we can't open it. But why?

```
team8317@actf:~$ ls -lah
total 68K
drwx------    3 team8317 team8317 4.0K Apr  3 12:25 .
drwx--x--x 1180 root     root      36K Apr  3 12:24 ..
-rw-------    1 team8317 team8317  348 Apr  3 00:14 .bash_history
-rw-r--r--    1 team8317 team8317  220 Feb 25  2020 .bash_logout
-rw-r--r--    1 team8317 team8317 3.7K Feb 25  2020 .bashrc
drwx------    2 team8317 team8317 4.0K Apr  2 22:48 .cache
-rw-r--r--    1 team8317 team8317  807 Feb 25  2020 .profile
----------    1 team8317 team8317   37 Apr  1  1921 flag.txt
```

It looks like we don't have read access. Let's fix that:

```
team8317@actf:~$ chmod 777 flag.txt
team8317@actf:~$ cat flag.txt
actf{thou_hast_uncovered_ye_ol_fleg}
```

And now we can read our flag: `actf{thou_hast_uncovered_ye_ol_fleg}`.
