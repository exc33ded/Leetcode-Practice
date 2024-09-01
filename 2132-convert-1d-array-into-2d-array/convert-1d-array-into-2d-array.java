class Solution {
    public int[][] construct2DArray(int[] original, int m, int n) {
        if (original.length != m * n) {
            return new int[0][0]; 
        }    

        int row = 0; 
        int col = 0;

        int[][] arr = new int[m][n];

        for (int i = 0; i < original.length; i++){
            arr[row][col] = original[i];
            col++;
            if (col == n){
                col = 0;
                row++;
            }
        }
        return arr;
    }
}