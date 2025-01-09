class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res={}
        for key, value in enumerate(nums):
            diff=target-value
            if diff in res:
                return [res[diff],key]
            res[value]=key
        return 
    
#starts a dictionary, gets two values key and value, calculates the diff, since we are searching for the difference which can be added to the accessed element so that it equals the target val
#then the given diff is checked, if its there in the dict, if its there then the current element index and its index are given as o/p
#the way enumerate() works is by accessin both the index and the value of what it is traversing, whereas range() only takes index into consideration, so its able to put 2 entities at o/p
#res[value]=key, is used to store the value along with its index into the dict as pairs
