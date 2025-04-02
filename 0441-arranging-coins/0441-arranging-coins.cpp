 class Solution {
 public:
  int arrangeCoins(int n) {
    return floor(sqrt(2.0 * n + 1.0 / 4) - 1.0/2);
  }
 };