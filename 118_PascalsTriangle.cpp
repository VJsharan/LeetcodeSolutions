class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result=[[1]]
    #since the 1st row 1 is guaranteed, a nested list is created here
        for i in range(numRows-1):
            temp = [0] + result[-1] + [0]
            row=[]
    #since the 1st row is already there we are taking only the rest of the rows so -1 from initial no. of rows, then the currently last element in the result is taken and contanated with 2 lists at beginning and end, so that the addition can be done
#also an empty list is being declared for the rows created further
            for j in range(len(result[-1])+1):
                row.append(temp[j]+temp[j+1])
            result.append(row)
        return result 
