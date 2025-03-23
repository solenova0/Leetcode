 class Solution {
 public:
  vector<int> relativeSortArray(vector<int>& arr1, vector<int>& arr2) {
    vector<int> ret;
    map<int, int> m;
    for (auto& n : arr1) {
      ++m[n];
    }
    for (auto& n : arr2) {
      while (m[n]-- > 0) {
        ret.push_back(n);
      }
    }
    for (auto it = m.begin(); it != m.end(); ++it) {
      while (it->second-- > 0) {
        ret.push_back(it->first);
      }
    }
    return ret;
  }
 };