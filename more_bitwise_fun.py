from hamming_weight import hamming_weight_smarter

def propogate_rightmost_one(x):
    """
    e.g. if
    :param n is 01010000  (80)
    :return:    01011111  (95)
    """
    y = x & ~(x-1)
    return x+y-1

print(propogate_rightmost_one(80))


def compute_mod_power_two(x, exp):
    """
    :param x: int type - e.g. 77 = 01001101
    :param exp: power of 2 (e.g. 6 -> 2^6 = 64)
    :return: x modulo 2^exp (e.g. 77 mod 64 = 13)
    """
    mask = (1 << exp) - 1
    return x & mask

print(compute_mod_power_two(77, 6))
print(compute_mod_power_two(173, 8))


def is_power_of_two(x):
    return hamming_weight_smarter(x) == 1

print(is_power_of_two(64))
print(is_power_of_two(65))
