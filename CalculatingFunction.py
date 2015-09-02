__author__ = 'deveshbajpai'

def solve(n):
    if(n%2==0):
        return (n-2)*(n+2)/2 - (n-2)*(n)/2
    else:
        return (n-3)*(n-3)/2 - (n-1)*(n+1)/2

if __name__ == "__main__":
    n = input()
    print solve(n)
