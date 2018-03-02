import random
from Crypto.Util.number import *

def main():
    p = 0
    q = 0
    g = 2 ** 128
    for b in range(127,-1,-1):
        # q = 2 ** b | p
        g = g >> 1
        g += p
        # bs = format((2 ** b) + p, '0128b')
        bs = format(g, '0128b')
        q = int(bs, 2)
        k = long_to_bytes(q, 16)
        # print q, bin(q), bytes_to_long(k).bit_length()

        # print q.bit_length(), q
        print bs, len(bs)
        # print "p = ", bin(p)
        # print "q = ", bin(q)
        # print " k = {} bytes".format(len(k))
        # print bytes_to_long(k).bit_length()
        # p = 1 << 12
        # p = q

        if random.choice([True, False]):
            # print "Heads!"
            p = 2 ** 127
        else:
            # print "Tails!"
            p = 0



if __name__ == '__main__':
    main()
