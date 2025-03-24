 class Solution {
 public:
  bool isToeplitzMatrix(vector<vector<int>>& matrix) {
    for (int i = 0; i < (int)matrix.size(); ++i) {
      for (int k = 1; k < (int)matrix[0].size(); ++k) {
        if (i + k < (int)matrix.size() && matrix[i + k][k] != matrix[i + k - 1]
 [k - 1]) {
          return false;
        }
      }
    }
    for (int j = 0; j < (int)matrix[0].size(); ++j) {
      for (int k = 1; k < (int)matrix.size(); ++k) {
        if (j + k < (int)matrix[0].size() && matrix[k][j + k] != matrix[k - 1][j 
+ k - 1]) {
          return false;
        }
      }
    }
    return true;
  }
 };