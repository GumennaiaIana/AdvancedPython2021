# -*- coding: utf-8 -*-

import argparse
from multiprocessing import Pool


def factorize(n):
    k = 2
    factors = []
    while n != 1:
        while n % k == 0:
            n //= k
            factors.append(k)
        k += 1
    return factors


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("integers", type=int, nargs='*')
    numbers = vars(parser.parse_args())['integers']

    with Pool() as p:
        factorized = p.map(factorize, numbers)

    for pair in zip(numbers, factorized):
        print(f"{pair[0]}:", *pair[1])
        
        
    




