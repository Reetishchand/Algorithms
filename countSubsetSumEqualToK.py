# Given a set of non-negative integers, and a value sum, determine if there is a subset of the given set with sum equal to given sum.
# Example:
#
# Input: set[] = {3, 34, 4, 12, 5, 2}, w = 9
# Output: True
# There is a subset (4, 5) with sum 9.
#
# Input: set[] = {3, 34, 4, 12, 5, 2}, w = 30
# Output: False
# There is no subset that add up to 30.



# This is similar to knapsack problem

def subSetSumEqualToK(arr,w,n):
    #using top-down/iteration
    t = [[0 for i in range(w + 1)] for j in range(n + 1)]
    if n==0 and w==0:
        return True
    for i in range(n + 1):
        t[i][0] = 1
    for i in range(1, w + 1):
        t[0][i] = 0
    for i in range(1,n+1):
        for j in range(1,w+1):
                if arr[i - 1] <= j:
                    t[i][j] = t[i - 1][j - arr[i - 1]] + t[i - 1][j]
                else:
                    t[i][j] = t[i - 1][j]
    return t[n][w]




w=10
arr = [3,3,6,8]
n=len(arr)
print(subSetSumEqualToK(arr,w,n))







