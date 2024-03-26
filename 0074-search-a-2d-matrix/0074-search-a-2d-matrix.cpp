class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int top = 0;
        int bottom = matrix.size() - 1;

        while (top <= bottom) {
            int midInd = floor((top + bottom) / 2);
            vector midMat = matrix[midInd];

            if (midMat.front() > target) {
                bottom = midInd - 1;
                continue;
            }
            if (midMat.back() < target) {
                top = midInd + 1;
                continue;
            }

            int l = 0;
            int r = midMat.size() - 1;

            while (l <= r) {
                int mid = floor((l + r) / 2);

                if (midMat[mid] == target) return true;
                else if (midMat[mid] < target) l = mid + 1;
                else r = mid - 1;
            }
            break;
        }
        return false;
    }
};