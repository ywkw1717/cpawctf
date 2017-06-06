#!/usr/bin/env python

import sys


def main():
    f = open('./list', 'r')

    sys.stdout.write('cpaw{')
    for i in f:
        sys.stdout.write(chr(int(i, 16)))

    sys.stdout.write('}')

    f.close()

if __name__ == '__main__':
    main()
