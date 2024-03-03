class Solution {
    public int[] createTargetArray(int[] nums, int[] index) {
        ArrayList<Integer> res = new ArrayList<>();
        for (int i = 0; i < nums.length; i++){
            res.add(index[i], nums[i]);
        }
        int target[] = new int[nums.length];
        for (int i = 0; i < nums.length; i++){
            target[i] = res.get(i);
        }
        return target;
    }
}