 class Solution {
 public:
  vector<int> distributeCandies(int candies, int num_people) {
    int n = num_people;
    vector<int> ret(n, 0);
    int i = 0;
    while (candies > 0) {
      if (i + 1 <= candies) {
        ret[i % n] += i + 1;
        candies -= i + 1;
      } else {
        ret[i % n] += candies;
        candies = 0;
      }
      ++i;
    }
    return ret;
  }
 };