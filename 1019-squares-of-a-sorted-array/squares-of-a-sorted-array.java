class Solution {
    public int[] sortedSquares(int[] nums) {
        int[] res = new int[nums.length];
        int i = 0;
        for (int num : nums) {
            res[i] = (int) Math.pow((double) num, 2);
            i++;
        }
        Arrays.sort(res);
        return res;
    }
}