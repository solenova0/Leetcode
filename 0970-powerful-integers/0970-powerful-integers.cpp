 class Solution {
 public:
  vector<int> powerfulIntegers(int x, int y, int bound) {
    vector<int> xPowers, yPowers;
    unordered_set<int> ret;
    for (int i = 0; pow(x, i) <= bound; ++i) {
      xPowers.push_back(pow(x, i));
      if (x == 1) break;
    }
    for (int i = 0; pow(y, i) <= bound; ++i) {
      yPowers.push_back(pow(y, i));
      if (y == 1) break;
    }
    for (int i = 0; i < (int)xPowers.size(); ++i) {
      for (int j = 0; j < (int)yPowers.size(); ++j) {
        int p = xPowers[i] + yPowers[j];
        if (p <= bound) {
          ret.insert(p);
        }
      }
    }
    return vector<int>(ret.begin(), ret.end());
  }
 };