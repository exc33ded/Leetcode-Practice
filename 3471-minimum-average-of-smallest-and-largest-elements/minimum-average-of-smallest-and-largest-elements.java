class Solution {
    public double minimumAverage(int[] nums) {
        int l = 0;
        int r = nums.length - 1;
        double min = Double.MAX_VALUE;
        Arrays.sort(nums);
        while(l < r){
            double avg = (double) (nums[l] + nums[r]) / 2;
            min = Math.min(min, avg);
            l++;
            r--;
        }
        return min;
    }
}