
def knapsackRecursive(weights,values,maxCapacity,n,mem):
    #n is the size of weights and values
    #mem is a nested list which stores intermidiatte values
    #base case
    if (n==0 or maxCapacity==0):
        return 0

    if mem[n][maxCapacity]==-1:
        if weights[n-1]<=maxCapacity:
            mem[n][maxCapacity] = max(values[n-1]+knapsackRecursive(weights,values,maxCapacity-weights[n-1],n-1,mem),
                                  knapsackRecursive(weights,values,maxCapacity,n-1,mem))
        else:
            mem[n][maxCapacity] = knapsackRecursive(weights,values,maxCapacity,n-1,mem)
    return mem[n][maxCapacity]

# Time Complexity: O(N*W).
# Auxiliary Space: O(N*W).


def knapSackIterative(weights,values,maxCapacity,n,t):
    if (n == 0 or maxCapacity == 0):
        return 0
    for i in range(0,n+1):
        for j in range(0,maxCapacity+1):
            if i==0 or j==0:
                t[i][j]=0
                continue
            if weights[i-1]<=j:
                t[i][j] = max(values[i-1]+t[i-1][j-weights[i-1]], t[i-1][j])
            else:
                t[i][j] = t[i-1][j]
    return t[n][maxCapacity]



maxCapacity=10
n=4
values = [1,3,5,7]
weights = [1,5,7,10]
mem = [[-1 for i in range(maxCapacity+2)] for j in range(n+2)]
print(knapsackRecursive(weights,values,maxCapacity,n,mem))
print(knapSackIterative(weights,values,maxCapacity,n,mem))