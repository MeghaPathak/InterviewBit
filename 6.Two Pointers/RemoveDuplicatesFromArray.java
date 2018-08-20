public class Solution {
    public int removeDuplicates(ArrayList<Integer> a) {
        int j = a.size() - 1;
        while(j > 0) {
            if(a.get(j).equals(a.get(j-1))) {
                a.remove(j);
            }
            j--;
        }
        
        return a.size(); 
 

    }
}
