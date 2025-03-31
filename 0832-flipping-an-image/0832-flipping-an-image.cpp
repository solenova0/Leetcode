class Solution {
 public:
  vector<vector<int>> flipAndInvertImage(vector<vector<int>>& A) {
    int m = A.size(), n = A[0].size();
    bool even_col = n % 2 == 1;
    for (int i = 0; i < m; ++i) {
      for (int l = 0, r = n - 1; l < r; ++l, --r) {
        swap(A[i][l], A[i][r]);
        A[i][l] ^= 1;
        A[i][r] ^= 1;
      }
      if (even_col) {
        A[i][n / 2] ^= 1;
      }
    }
    return A;
  }
 };