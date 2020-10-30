def func(n,m,h,v):
    x=[1]*(n+1)
    y = [1]*(m+1)
    for i in range(len(h)):
        x[h[i]]=0
    for i in range(len(v)):
        y[v[i]]=0
    ox = float("-inf")
    cy = 0
    oy = float("-inf")
    cx=0
    for i in range(1,n+1):
        if x[i]:
            cx=0
        else:
            cx+=1
            ox = max(ox,cx)
    for i in range(1,m+1):
        if y[i]:
            cy=0
        else:
            cy+=1
            oy = max(oy,cy)
    return (ox + 1) * (oy + 1)

print(func(3,2,[1,2,3],[1,2]))


