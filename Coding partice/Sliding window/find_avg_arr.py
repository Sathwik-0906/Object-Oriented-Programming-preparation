# Array: [1, 3, 2, 6, -1, 4, 1, 8, 2], K=5
# Given an array, find the average of all contiguous subarrays of size ‘K’ in i


# brute force
# def find_avg_arr(k,arr):
#     result=[]
#     for i in range(len(arr)-k+1):
#         sum=0.0
#         for j in range(i,i+k):
#             sum+=arr[j]
#         result.append(sum/k)
#     return result

# def main():
#     res = find_avg_arr(5,[1, 3, 2, 6, -1, 4, 1, 8, 2])
#     print("Avearge of the sub array of size k:",str(res))
    
# main()



# Step-by-step Description of the Sliding Window Algorithm:
# Initialize an empty list to store the final results (averages).

# Set up two variables:

# One to store the current sum of the window.

# Another to mark the start index of the current window.

# Iterate through the array using a loop, treating the current index as the end of the window.

# Add the current element to the running window sum.

# Once the window size reaches K:

# Calculate the average of the current window and store it.

# Subtract the element at the start of the window from the sum (as it will slide out).

# Move the start of the window one step forward.

# Continue this process until the end of the array is reached.

# Return the list of all calculated averages.

def find_avg_arr(k,arr):
    result=[]
    windowsum,windowstart=0.0,0
    for windowend in range (len(arr)):
        windowsum+=arr[windowend]
        if windowend >= k-1:
            result.append(windowsum/k)
            windowsum-=arr[windowstart]
            windowstart+=1
    return result

def main():
    res = find_avg_arr(5,[1, 3, 2, 6, -1, 4, 1, 8, 2])
    print("Avearge of the sub array of size k:",str(res))

main()


