__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/1080/A

Solution: TODO
'''


def solve(n, k):

    return ceil_division(2 * n, k) + ceil_division(5 * n, k) + ceil_division(8 * n, k)


def ceil_division(a, b):

    return (a + b - 1) / b


if __name__ == "__main__":

    n, k = map(int, raw_input().split(" "))
    print solve(n, k)
