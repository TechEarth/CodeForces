__author__ = 'Devesh Bajpai'

class ArrivaloftheGeneral:

    n = 0
    heights = ()

    def solve(self):
        for i in range(0,self.n):
            print self.heights[i]

if __name__ == "__main__":
    a = ArrivaloftheGeneral()
    a.n = int(raw_input())
    a.heights = map(int,raw_input().split(" "))
    print a.solve()