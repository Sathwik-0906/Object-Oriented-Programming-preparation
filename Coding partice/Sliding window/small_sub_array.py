# Smallest Subarray with a given sum
# Problem Statement #
# Given an array of positive numbers and a positive number ‘S’, find the length of the smallest contiguous subarray whose sum is greater than or equal to ‘S’. Return 0, if no such subarray exists.
# input = [2,1,5,2,3,2]
# s = 7
import math
def small_sub(s,arr):
    windowsum = 0
    minlen = math.inf
    windowstart = 0

    for windowend in range(0,len(arr)):
        windowsum += arr[windowend]
        while windowsum >= s :
            minlen = min(minlen,windowend - windowstart+1)
            windowsum-=arr[windowstart]
            windowstart+=1

    if minlen==math.inf:
        return 0
    else:
        return minlen
    
def main():
    print("smallest sub array len:"+str(small_sub(7,[2,1,5,2,3,2])))

main()
        


        