 class Solution {
 public:
  int numJewelsInStones(string J, string S) {
    int ret = 0, chars[128] = {0};
    for (auto& j : J) {
      ++chars[j];
    }
    for (auto& s : S) {
      ret += chars[s];
    }
    return ret;
  }
 };