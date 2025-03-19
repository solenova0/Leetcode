 class Solution {
 public:
  bool isPowerOfFour(int num) {
    int n = __builtin_popcount(num);
    if (n != 1 || n <= 0) return false;
    while (num != 0 && (num & 1) != 1) num >>= 2;
    return num == 1;
  }
 };