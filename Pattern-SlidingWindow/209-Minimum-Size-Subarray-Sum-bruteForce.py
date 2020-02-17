def minSumSubarray(arr, s):
    if arr is None: return 0
    if s is None: return 0
    for k in range(len(arr)):
        for i in range(len(arr)-k+1):
            summ=0
            for j in range(i, i+k):
                summ+=arr[j]
            if summ >= s:
                return k

def main():
    res = minSumSubarray([3, 4, 4, 6, 6], 1)
    print(res)
main()