def romanToInt( s: str) -> int:
    values = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }
    total = values.get(s[-1])
    for i in reversed(range(len(s) - 1)):
        if values[s[i]] < values[s[i + 1]]:
            total -= values[s[i]]
        else:
            total += values[s[i]]
    return total

def merge(nums):
    if len(nums)>1:
        mid = len(nums)//2
        L,R = nums[:mid],nums[mid:]
        merge(L)
        merge(R)
        i,k,j=0,0,0
        while i<len(L) and j<len(R):
            if (L[i][0]<R[j][0]) or (L[i][0] == R[j][0] and L[i][2]<R[j][2]):
                nums[k]=L[i]
                i+=1
            else:
                nums[k]=R[j]
                j+=1
            k+=1
        while i<len(L):
            nums[k] = L[i]
            i += 1
            k+=1
        while j<len(R):
            nums[k]=R[j]
            j+=1
            k+=1
    return nums

def func(names):
    arr=[]
    for i in range(len(names)):
        x = names[i].split(" ")
        x.append(romanToInt(x[1]))
        arr.append(x)
    merge(arr)
    for i in range(len(arr)):
        x = arr[i]
        x.pop()
        arr[i] = ' '.join(x)
    return arr

names = ["Steven XL","Steven XVI","David IX","Mary XV","Masy XIII","Mary XX","Louis IX","Louis VIII","Philip II","Philippe I"]
print(func(names))
