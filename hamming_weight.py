import random

# N.B.: If computation is done repeatedly, most efficient method would be to create a lookup table.
# Might lookup 16 bits at a time (table of size 2^16 = 65536 entries); for inputs > 65535,
# mod by powers of 2 ^ 16 and add results of lookups

def hamming_weight_brute_force(n):
    """
    O(len(n))
    """
    count = 0
    while n > 0:
        count += n & 1
        n >>= 1
    return count

# result = hamming_weight_brute_force(415)
# if result != 7:
#     print 'brute_force returns %d should return %d' % (result, 7)


def hamming_weight_smarter(n):
    count = 0
    while n > 0:
        n &= (n-1)
        count += 1
    return count


# for i in xrange(10):
#     next = random.randint(0, 1024)
#     brute = hamming_weight_brute_force(next)
#     smart = hamming_weight_smarter(next)
#     if brute != smart:
#         print 'brute_force for %d returns %d - should return %d' % (next, smart, brute)
#     else:
#         print 'result for %d is correct (%d)' % (next, smart)