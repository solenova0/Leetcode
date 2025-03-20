class Solution {
 public:
  bool checkIfCanBreak(string s1, string s2) {
    sort(s1.begin(), s1.end());
    sort(s2.begin(), s2.end());
    int n = s1.size();
    bool greaterThan = true, lessThan = true;
    for (int i = 0; i < n; ++i) {
      if (s1[i] > s2[i]) {
        lessThan = false;
      }
      if (s1[i] < s2[i]) {
        greaterThan = false;
      }
    }
    return lessThan || greaterThan;
  }
 };