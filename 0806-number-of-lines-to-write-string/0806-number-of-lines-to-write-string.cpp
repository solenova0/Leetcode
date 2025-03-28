 class Solution {
 public:
  vector<int> numberOfLines(vector<int>& widths, string S) {
    int lines = S.size() > 0 ? 1 : 0, cur = 0;
    for (auto& c : S) {
      if (cur + widths[c - 'a'] > 100) {
        ++lines;
        cur = widths[c - 'a'];
      } else {
        cur += widths[c - 'a'];
      }
    }
    return {lines, cur};
  }
 };