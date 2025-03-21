 class Solution {
 public:
  int maxPower(string s) {
    if (s.empty()) return 0;
    int cnt = 1;
    int ret = 1;
    for (int i = 1; i < (int)s.size(); ++i) {
      if (s[i] == s[i - 1]) {
        ret = max(ret, ++cnt);
      } else {
        cnt = 1;
      }
    }
    return ret;
  }
 };