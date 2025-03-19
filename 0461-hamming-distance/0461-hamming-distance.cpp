class Solution {
 public:
  int hammingDistance(int x, int y) {
    int ret = 0, m = x ^ y;
    for (int m = x ^ y; m != 0; m /= 2) {
      ret += m % 2;
    }
    return ret;
  }
 };