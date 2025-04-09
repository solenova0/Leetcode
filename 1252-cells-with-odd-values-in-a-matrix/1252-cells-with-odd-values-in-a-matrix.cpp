 class Solution {
 public:
  int oddCells(int n, int m, vector<vector<int>>& indices) {
    vector<bool> row(n, false), col(n, false);
    int nr = 0, nc = 0;
    for (auto& index : indices) {
      row[index[0]] = !row[index[0]];
      col[index[1]] = !col[index[1]];
      nr += row[index[0]] ? 1 : -1;
      nc += col[index[1]] ? 1 : -1;
    }
    return m * nr + n * nc - 2 * nr * nc;
  }
 };