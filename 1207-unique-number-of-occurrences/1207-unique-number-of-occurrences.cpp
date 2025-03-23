 class Solution {
 public:
  bool uniqueOccurrences(vector<int>& arr) {
    unordered_map<int, int> m;
    unordered_set<int> occurence;
    for (auto& n : arr) {
      ++m[n];
    }
    for (auto& n : m) {
      occurence.insert(n.second);
    }
    return occurence.size() == m.size();
  }
 };