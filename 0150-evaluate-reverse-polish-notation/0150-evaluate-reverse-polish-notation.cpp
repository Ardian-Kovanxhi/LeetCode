class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack <int> stk;

        for (int i = 0; i < tokens.size(); i++) {
            string token = tokens[i];

            if (token.size() > 1 || isdigit(token[0])) {
                stk.push(stoi(token));
                continue;
            }

            int right = stk.top();
            stk.pop();
            int left = stk.top();
            stk.pop();

            int result = 0;
            if (token == "+") result = left + right;
            if (token == "-") result = left - right;
            if (token == "*") result = left * right;
            if (token == "/") result = left / right;
            stk.push(result);
        }

        return stk.top();
    }
};