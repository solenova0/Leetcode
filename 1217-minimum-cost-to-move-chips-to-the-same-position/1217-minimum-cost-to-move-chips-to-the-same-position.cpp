 class Solution {
 public:
//
  int minCostToMoveChips(vector<int>& chips) {
    int odd = 0, even = 0;
    for (auto& c : chips) {
      if (c % 2 == 1) {
        ++odd;
      } else {
        ++even;
      }
    }
    return min(odd, even);
  }
 };