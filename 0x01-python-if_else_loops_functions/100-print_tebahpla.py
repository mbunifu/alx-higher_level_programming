#!/usr/bin/python3
for i in range(ord('z'), ord('a') - 1, -1):
    if i % 2 == 0:
        diff = 0
    else:
        diff = 32
        printf('{}'.format(chr(i - diff)), end='')
