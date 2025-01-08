class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        x=[]
        x=nums.copy()
        return (nums+x)
#easy shit, just make a copy of the given i/p list, store it in smth, then concatenate the og and the copy, simple as that
