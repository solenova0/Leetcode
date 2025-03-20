 class Solution {
 public:
  string destCity(vector<vector<string>>& paths) {
    unordered_set<string> cities;
    unordered_set<string> departs;
    for (auto& p : paths) {
      cities.insert(p[0]);
      cities.insert(p[1]);
      departs.insert(p[0]);
    }
    for (auto& d : departs) {
      cities.erase(d);
    }
    string ret;
    for (auto& c : cities) {
      ret = c;
    }
    return ret;
  }
 };