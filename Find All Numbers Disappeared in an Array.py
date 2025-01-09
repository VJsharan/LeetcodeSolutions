class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nums.sort()
        res=[]
        x=set(nums)
        givensum=sum(x)
        for i in range(1,len(nums)+1):
            if i not in x:
                res.append(i)
        return res

#did it on my own less fucking go
#sorts the array, converts it into a set, calculates the sum, 
# the + 1 is used so that the last is not left out, since in range(1,10), does only from 1-9, we need all 10 so adding the 1 to make it
#goes through all the elements from 1 - given n and checks if the current i is present in the set, if it is not, then its added to the result array ret
