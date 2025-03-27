class Solution {
 public:
  string toLowerCase(string str) {
     for (auto& c : str) {
      c = 'A' <= c && 'Z' >= c ? c + ('a' - 'A') : c;
    }
    return str;
  }
 };