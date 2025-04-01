 class Solution {
 public:
  int minStartValue(vector<int>& nums) {
    partial_sum(nums.begin(), nums.end(), nums.begin());
    int ret = *min_element(nums.begin(), nums.end());
    return ret >= 0 ? 1 : 1 - ret;
  }
 };