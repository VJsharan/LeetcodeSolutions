class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        setof=set(nums)
        if len(nums)==len(setof):
            return False
        else:
            return True

#pretty simple but what happens here is the given list is converted into a set, and their lenths are compared, 
#since sets have no duplication, if the list len != set len, there is said to be duplication in the i/p, otherwise they are all unique
