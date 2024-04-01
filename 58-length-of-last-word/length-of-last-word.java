class Solution {
    public int lengthOfLastWord(String s) {
        int res = 0;
        char[] arr = s.toCharArray();
        for (int i = arr.length - 1; i >= 0; i--) {
            if (arr[i] != ' ') {
                res++;
            } else if (res > 0) {
                return res;
            }
        }
        return res;
    }
}
