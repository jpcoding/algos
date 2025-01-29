def longestOnes( nums, k) -> int:
    left = 0 

    for right in range(len(nums)):
        if(nums[right] == 0):
            k-=1 
        if (k < 0):
            if(nums[left] == 0):
                k+=1
            left += 1 
        print("left ", left, " right ", right )
        
    return right-left+1 


A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
k = 3

print(longestOnes(A,k))

