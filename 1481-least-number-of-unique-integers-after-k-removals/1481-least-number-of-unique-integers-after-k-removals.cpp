 class Solution {
 public:
  int findLeastNumOfUniqueInts(vector<int>& arr, int k) {
    unordered_map<int, int> cnt;
    for (auto& a : arr) ++cnt[a];
    vector<pair<int, int>> p;
    for (auto& c : cnt) p.push_back({c.second, c.first});
    sort(p.rbegin(), p.rend());
    while (k > 0 && !p.empty()) {
      k -= p.back().first;
      if (k >= 0) {
        p.pop_back();
      }
    }
    return p.size();
  }
 };