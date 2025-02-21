class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        new_nums=sorted(nums)
        dic={}
        for index, num in enumerate(new_nums):
            if num not in dic:
                dic[num] = index
        result_list=[]
        for vals in nums:
            result_list.append(dic[vals])
        return result_list

''' 
Code explanation  : 
    the given nums list is sorted, using the sorted func and not the .sort() since the .sort() doesnt return anything new, just sorts the original list, so no value to work with
then a new dict is created, 
and in a for loop, the nums is in enumerate, so that each value in the list and its index is both accessed and stored in the loop variables,
if the accessed element isnt in the dict, then that ele along with its index is added as the key value pair to the dict,
eg : [4,2,5,6] -> [2,4,5,6], (6) is at 3rd index, making it larger than 3 nos,
then the values of the specific keys are taken and appended and returned as result
'''
        
