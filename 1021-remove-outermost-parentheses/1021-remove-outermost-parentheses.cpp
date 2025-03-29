 class Solution {
 public:
  string removeOuterParentheses(string S) {
    string ret;
    int status = 0;
    for (auto& c : S) {
      if (c == '(') {
        if (status++ > 0) {
          ret += c;
        }
      } else {
        if (--status > 0) {
          ret += c;
        }
      }
    }
    return ret;
  }
 };