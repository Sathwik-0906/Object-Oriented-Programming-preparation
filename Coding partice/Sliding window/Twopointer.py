# Input: [1, 2, 3, 4, 6], target=6
# Output: [1, 3]
# Explanation: The numbers at index 1 and 3 add up to 6: 2+4=6

def target(nums,k):
    i = 0
    j = len(nums)-1
    ans=[]
    while i < j:
        if nums[i]+nums[j] == k:
             ans.append(i)
             ans.append(j)
        if nums[i]+nums[j]>k:
            j-=1
        else:
            i+=1

    return ans

def main():
    print("target found at sub index of : ",target([2, 5, 9, 11],11))

main()

