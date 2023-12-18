class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        if (nums.size() < 2) return false;

        set<int> logger;
        int i = 0;

        while (i < nums.size()) {
            if (logger.count(nums[i]) > 0) return true;
            logger.insert(nums[i]);
            i++;
        }

        return false;
    }
};