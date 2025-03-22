 class Solution {
 public:
  int projectionArea(vector<vector<int>>& grid) {
    int x = 0, y = 0, z = 0;
    vector<int> col_max(grid[0].size(), 0);
    vector<int> row_max(grid.size(), 0);
    for (int i = 0; i < (int)grid.size(); ++i) {
      for (int j = 0; j < (int)grid[0].size(); ++j) {
        if (grid[i][j] > 0) {
          ++z;
        }
        row_max[i] = max(row_max[i], grid[i][j]);
      }
    }
    for (int j = 0; j < (int)grid[0].size(); ++j) {
      for (int i = 0; i < (int)grid.size(); ++i) {
        col_max[j] = max(col_max[j], grid[i][j]);
      }
    }
    for (auto& r : row_max) {
      y += r;
    }
    for (auto& c : col_max) {
      x += c;
    }
    return x + y + z;
  }
 };