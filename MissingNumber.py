class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        givenSum=sum(nums)
        #n1=nums[-1]
        actualsum=sum(range(len(nums)+1))
        return int(actualsum-givenSum)
    #sorts the given array, SUMS takes the sum of the elements in the array, then the actualsum is calculated by traversing linearly via all the elements in the array using range and adding them using the sum, their sums are subracted to find the missing num
# + 1 is done in line 6 since the range goes for i-1 interations usually for range(i), so for missing iteration 1 is added



previous solution :
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        num=nums.sort()
        #x=set(nums)
        for i in range(0,len(nums)):
            if((num[i]+1) != num[i+1]):
                num.insert(i+1, num[i]+1)
                return (num[i]+1)
            else:
                continue    
#this didnt work since there I Was trying to modify the values of elements which weren't even accessed 
# so obviously it threw memory out of bounds error but tho its a good idea i came up with it, it will work if line 19 is modified of some sort
