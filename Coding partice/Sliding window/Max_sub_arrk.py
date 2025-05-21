# def max_sub_arr_of_size_k(k,arr):
#     res=[]
#     for i in range(len(arr)-k+1):
#         sum=0
#         for j in range(i,i+k):
#             sum+=arr[j]
#         res.append(sum)
#     return max(res)

# def main():
#     res = max_sub_arr_of_size_k(3,[2,1,5,1,3,2])
#     print("max sub elemt of the array  with size k is:",str(res))
# main()



def max_sub(k,arr):
    res=[]
    windowsum=0
    windowstart=0
    for windowend in range(len(arr)):
        windowsum+=arr[windowend]
        if windowend >= k - 1:
            res.append(windowsum)
            windowsum-=arr[windowstart]
            windowstart+=1
    return max(res)

def main():
    res=max_sub(3,[2,1,5,1,3,2])
    print(str(res))

main()