class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
         unordered_map<int, int> numMap;

        for (int i = 0; i < nums.size(); i++) {
            int complement = target - nums[i];

            // Check if the complement exists in the hash map
            if (numMap.find(complement) != numMap.end()) {
                // Return the indices of the current number and its complement
                return {numMap[complement], i};
            }

            // Store the current number and its index in the hash map
            numMap[nums[i]] = i;
        }

        // If no solution is found, return an empty vector
        return {};
    }
};