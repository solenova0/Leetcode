 class Solution {
 public:
  int balancedStringSplit(string s) {
    int ret = 0, running_sum = 0;
    for (auto& c : s) {
      running_sum += c == 'R' ? 1 : -1;
      ret += running_sum == 0 ? 1 : 0;
    }
    return ret;
  }
 };