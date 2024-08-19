import java.util.ArrayList;

class Solution {
    public int minSteps(int n) {
        ArrayList<Integer> res = new ArrayList<>();

        while (n % 2 == 0) {
            res.add(2);
            n = n / 2;
        }

        for (int i = 3; i <= Math.sqrt(n); i += 2) {
            while (n % i == 0) {
                res.add(i);
                n = n / i;
            }
        }

        
        if (n > 2) {
            res.add(n);
        }

        int sum = 0;
        for(int i = 0; i < res.size(); i++){
            sum = sum + res.get(i);
        }
        return sum;
    }
}
