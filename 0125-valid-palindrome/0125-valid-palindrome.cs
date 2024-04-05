public class Solution {
    public bool IsPalindrome(string s) {
        int l = 0;
        int r = s.Length - 1;

        while (l <= r) {
            while (!Char.IsLetterOrDigit(s[l]) && l < r) l++;
            while (!Char.IsLetterOrDigit(s[r]) && l < r) r--;
            if (Char.ToLower(s[l]) != Char.ToLower(s[r])) return false;
            l++;
            r--;
        }

        return true;
    }
}