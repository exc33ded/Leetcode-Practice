class Solution {
    public boolean uniqueOccurrences(int[] arr) {
        Map<Integer,Integer> map = new HashMap<>();
        for(int i:arr){
            if(map.containsKey(i)){
                int temp = map.get(i);
                map.put(i,++temp);
            }
            else{
                map.put(i,1);
            }
        }
        Set<Integer> set = new HashSet<>();
        for(int i:map.values()){
            if(!set.add(i)){
                return false;
            }
        }
    return true;
    }
}