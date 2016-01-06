def hamming_weight_brute_force(n):
    count = 0
    while n > 0:
        count += n & 1
        n >>= 1
    return count

result = hamming_weight_brute_force(415)
print(result)