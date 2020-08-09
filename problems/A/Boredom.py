__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/455/A

TODO: NOT YET PASSING ALL TESTCASES IN THE OJ
Solution: We first calculate the frequency map of the array and the maximum element in that.   
freq_map[arr[i]]= frequency of occurrence of arr[i] element

The recurrence can be observed as:
dp[num]= maximum points that can be obtained by considering elements numerically equal to num

To compute that, there can be 2 possibilities:

case 1: num is selected
In this case, we would select all the occurrences of element num in the array to gather that much points. 
Also, the problem would reduce to f(1.... num-2) since all occurrences of num-1 would be deleted as well.

So points scored in this case = num * freq_map[num] + dp[num-2]

case 2: num is not selected
In this case, the strategy would be to move over to the next element to score points which would be num-1.

So points scored in this case = dp[num-1]

So thus we get the recurrence relation is:
 dp[num] = max(dp[num-1] , dp[num-2] + freq_map[num]*num)
 
In order to have efficient space complexity, we make the dp array up till the maximum element in the array, 
which is calculated while build the frequency map. 
'''


def solve(n, arr):

    freq_map = {}

    #max_elem = arr[0]
    max_elem = 100000
    for i in xrange(0, n):
        freq_map[arr[i]] = arr.count(arr[i])
        #max_elem = max(max_elem, arr[i])

    dp = [0] * (max_elem + 1)
    max_dp = 0
    for num in xrange(1, max_elem + 1):
        dp[num] = max(dp[num-1], dp[num-2] + num * (freq_map.get(num, 0)))
        max_dp = max(max_dp, dp[num])

    return max_dp


if __name__ == "__main__":

    n = int(raw_input())
    arr = map(int, raw_input().split(" "))
    print solve(n, arr)
