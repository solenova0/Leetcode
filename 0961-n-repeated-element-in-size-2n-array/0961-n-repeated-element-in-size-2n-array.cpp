 class Solution {
 public:
  int repeatedNTimes(vector<int>& A) {
    unordered_map<int, int> m;
    for (auto& n : A) {
      if (++m[n] > 1) {
        return n;
      }
    }
    return -1;
  }
 };