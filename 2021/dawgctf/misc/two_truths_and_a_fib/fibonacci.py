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
