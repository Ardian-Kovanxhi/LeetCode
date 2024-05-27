impl Solution {
    pub fn eval_rpn(tokens: Vec<String>) -> i32 {
        let mut stack: Vec<i32> = Vec::new();
        for token in tokens {
           match &token[..] {
            "+" => {
                let right = stack.pop().unwrap();
                let left = stack.pop().unwrap();
                stack.push(left + right);
            }
            "-" => {
                let right = stack.pop().unwrap();
                let left = stack.pop().unwrap();
                stack.push(left - right);
            }
            "*" => {
                let right = stack.pop().unwrap();
                let left = stack.pop().unwrap();
                stack.push(left * right);
            }
            "/" => {
                let right = stack.pop().unwrap();
                let left = stack.pop().unwrap();
                stack.push(left / right);
            }
            value => stack.push(value.parse::<i32>().unwrap()),
           }
        }
        return stack[0];
    }
}