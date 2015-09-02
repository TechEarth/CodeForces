__author__ = 'Devesh Bajpai'

def solve(n,m):
    if(m>n):
        return -1
    elif(m==n):
        return n
    else:



if __name__ == "__main__":
    n,m = map(int,raw_input().split(" "))
    print solve(n,m)
