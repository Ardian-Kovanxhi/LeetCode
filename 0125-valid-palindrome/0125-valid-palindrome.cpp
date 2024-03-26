class Solution {
public:
    bool isPalindrome(string s) {
        std::string palindrome;
        
        for(const char ch : s){
            if(std::isalnum(ch)){
                palindrome += std::tolower(ch);
            }
        }
        std::string temp(palindrome);
        std::reverse(palindrome.begin(),palindrome.end());
        return temp == palindrome;
    }
};