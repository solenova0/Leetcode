class Solution {
public:
    int singleNumber(std::vector<int>& nums) {
        int singleNumber = 0; 
        for (int num : nums) {
            singleNumber ^= num; 
        }

        return singleNumber; 
    }
};
