class Solution {
    public int minLength(String s) {
        Stack<Character> stack = new Stack<>();
        for (int i = 0; i < s.length(); i++){
            char c = s.charAt(i);
            if (stack.isEmpty()){
                stack.push(c);
                continue;
            }
            if (c == 'B' && stack.peek() == 'A'){
                stack.pop();
            }
            else if (c == 'D' && stack.peek() == 'C'){
                stack.pop();
            }
            else{
                stack.add(c);
            }
        }
        return stack.size();
    }
}