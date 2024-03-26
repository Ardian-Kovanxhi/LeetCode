class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map <string, vector<string>> logger;

        for (int i = 0; i < strs.size(); i++) {
            string key = getKey(strs[i]);
            logger[key].push_back(strs[i]);
        }

        vector < vector <string> > ans;
        for (auto i = logger.begin(); i != logger.end(); i++) {
            ans.push_back(i -> second);
        }
        return ans;
    }

private:
    string getKey (string str) {
        vector <int> count(26);
        for (int i = 0; i < str.size(); i++) {
            count[str[i] - 'a']++;
        }

        string key = "";
        for (int i = 0; i < count.size(); i++) {
            key.append(to_string(count[i]) + "#");
        }

        return key;
    }
};