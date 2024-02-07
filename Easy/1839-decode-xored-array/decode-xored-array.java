class Solution {
    public int[] decode(int[] encoded, int first) {
        int arr[] = new int[encoded.length+1];
        arr[0] = first;

        for(int i = 1; i < arr.length; i++){
            int last = arr[i-1];
            int xor = encoded[i-1] ^ last;
            arr[i] = xor;
        }
        return arr;
    }
}