# Two Truths and a Fib

## Challenge:

Can you catch the fibber?

nc umbccd.io 6000

## Solution:

Let's connect to the server:

```bash
$ nc umbccd.io 6000
Welcome to two truths and a fib! You'll be given three numbers:
one of them will be a fibonacci number and two of them will not.
It's your job to tell which is which and send back the fibonacci.
Example:
12, 8, 4
Which number is a fib?
>> 8
Correct!

[6947430254846, 1597, 5502044371417]
>>
Oof, too slow!
```

We're given a set of numbers and we need to figure out which one is a [Fibonacci number](https://en.wikipedia.org/wiki/Fibonacci_number).

Calculating the entire sequence for every set would be crazy. Thankfully, there's [a formula](https://math.stackexchange.com/questions/9999/checking-if-a-number-is-a-fibonacci-or-not) we can use to figure it out quickly. We need to get the square root of 5 times our number squared, plus or minus 4, and see which one is an integer. The perfect cube will be our Fibonacci number.

We can use [pwntools](https://github.com/Gallopsled/pwntools) to make a connection and parse the output:

```python
from pwn import *
import re

conn = remote('umbccd.io',6000)

count = 0
while True:
    if count == 100:
        print(conn.recvline())
        break

    question = conn.recvuntil(']\n>>')

    numbers = re.search('\[(.*)\]', str(question))
    numbers = numbers[1].split(', ')

    fibonacci = '0'

    for i in numbers:
        add = math.sqrt((5*int(i)**2)+4)
        sub = math.sqrt((5*int(i)**2)-4)
        if add.is_integer() or sub.is_integer():
            fibonacci = i

    conn.send(fibonacci + '\n')
    conn.recvuntil('\n\n')

    count = count + 1 
```

This will run through 100 different challenges for us followed by our flag:

```bash
[+] Opening connection to umbccd.io on port 6000: Done
b"Congrats! Here's your flag: DawgCTF{jU$T_l1k3_w3lc0me_w33k}\n"
[*] Closed connection to umbccd.io port 6000
```

There it is: `DawgCTF{jU$T_l1k3_w3lc0me_w33k}`.
