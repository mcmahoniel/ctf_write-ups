# FREE FLAGS!!1!!

## Challenge:

Clam was browsing armstrongctf.com when suddenly a popup appeared saying "GET YOUR FREE FLAGS HERE!!!" along with [a download](https://files.actf.co/6ddcb4e935b82c477140ee6833eceaf1149e0c732af1ba742a9e67db98693f88/free_flags). Can you fill out the survey for free flags?

Find it on the shell server at `/problems/2021/free_flags` or over netcat at `nc shell.actf.co 21703`.

## Solution:

We're given a binary which we can run right now on the shell server:

```bash
team8317@actf:~$ cd /problems/2021/free_flags
team8317@actf:/problems/2021/free_flags$ ls
flag.txt  free_flags
team8317@actf:/problems/2021/free_flags$ ./free_flags
Congratulations! You are the 1000th CTFer!!! Fill out this short survey to get FREE FLAGS!!!
What number am I thinking of???
1
Wrong >:((((
```

Since we're not psychic, we're going to need to look into the binary to see what's expected here.

Running `strings` against the binary reveals some questions we haven’t seen yet; “What two numbers am I thinking of???”, “What animal am I thinking of???”.

Let’s open up Ghidra. In the decompilation we can see what may be our answers:

```c
  puts("What number am I thinking of???");
  __isoc99_scanf("%d",&local_11c);
  if (local_11c == 0x7a69) {
    puts("What two numbers am I thinking of???");
    __isoc99_scanf("%d %d",&local_120,&local_124);
    if ((local_120 + local_124 == 0x476) && (local_120 * local_124 == 0x49f59)) {
      puts("What animal am I thinking of???");
      __isoc99_scanf(" %256s",local_118);
      sVar2 = strcspn(local_118,"\n");
      local_118[sVar2] = '\0';
      iVar1 = strcmp(local_118,"banana");
```

The number they're thinking of is `0x7a69`, or `31337` in decimal. That gets us to step 2:

```bash
team8317@actf:/problems/2021/free_flags$ ./free_flags
Congratulations! You are the 1000th CTFer!!! Fill out this short survey to get FREE FLAGS!!!
What number am I thinking of???
31337
What two numbers am I thinking of???
1 2
Wrong >:((((
```

From our decomplication, we know that we're working with `0x476` (`1142`) and `0x49f59` (`302937`). We need two numbers that when added together equal `1142` and when multiplied equal `302937`. We can list out all factors of `302937` and find that `429` and `723` add and multiply together to get our numbers.

Finally, we can see the word `banana` listed, and try that as our “animal”:

```bash
team8317@actf:/problems/2021/free_flags$ ./free_flags
Congratulations! You are the 1000th CTFer!!! Fill out this short survey to get FREE FLAGS!!!
What number am I thinking of???
31337
What two numbers am I thinking of???
419 723
What animal am I thinking of???
banana
Wow!!! Now I can sell your information to the Russian government!!!
Oh yeah, here's the FREE FLAG:
actf{what_do_you_mean_bananas_arent_animals}
```

And now we have our flag: `actf{what_do_you_mean_bananas_arent_animals}`.
