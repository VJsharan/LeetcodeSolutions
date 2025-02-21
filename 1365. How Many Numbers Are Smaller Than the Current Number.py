class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        dic={}
        for index, num in enumerate(nums):
            if num not in dic:
                dic[num] = index
        result_list=[]
        for vals in nums:
            result_list.append(dic[vals])
        return result_list


        
