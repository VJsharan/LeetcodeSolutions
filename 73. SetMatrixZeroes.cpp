class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        int col0 = 1, rows = matrix.size(), cols = matrix[0].size();
    //the way is works is by getting the matrixes as i/p and then gaining their lengths which are then stored in rows and col
// then row and coln are both initially 0s, then its changed to 1 to signify that, THAT ENTIRE ROW OR COLN needs to be turned into zeroes
    for (int i = 0; i < rows; i++) {
        if (matrix[i][0] == 0) col0 = 0;
        for (int j = 1; j < cols; j++)
            if (matrix[i][j] == 0)
                matrix[i][0] = matrix[0][j] = 0;
    }
//it checks the elements and makes col0 as 0 if something is zero out there, and with that if it comes over a zero element, the first element of that row where 0 is present is made zero and the col first element is also made 0
//this is to signify which rows and coloumns to convert to 0
//then the changes are made in the given matrix and sent as o/p
    for (int i = rows - 1; i >= 0; i--) {
        for (int j = cols - 1; j >= 1; j--)
            if (matrix[i][0] == 0 || matrix[0][j] == 0)
                matrix[i][j] = 0;
        if (col0 == 0) matrix[i][0] = 0;
    }
    }
};
