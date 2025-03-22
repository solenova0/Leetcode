 class Solution {
 public:
  vector<int> selfDividingNumbers(int left, int right) {
    vector<int> ret;
    for (int i = left; i <= right; ++i) {
      if (self_dividing(i)) {
        ret.push_back(i);
      }
    }
    return ret;
  }
 
  bool self_dividing(int n) {
    string s = to_string(n);
    for (auto& c : s) {
      if (c == '0' || (c != '0' && n % (c - '0') != 0))
        return false;
    }
    return true;
  }
 };