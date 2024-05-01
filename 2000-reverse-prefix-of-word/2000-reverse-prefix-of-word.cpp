class Solution {
public:
    string reversePrefix(string word, char ch) {
        string ans = "";

        for (int i = 0; i < word.size(); i++) {
            if (ans.size() > 0) {
                ans += word[i];
            }
            else if (word[i] == ch) {
                for (int j = 0; j < i + 1; j++) {
                    ans = word[j] + ans;
                }
            }
        }
        return ans.size() > 0 ? ans : word;
    }
};