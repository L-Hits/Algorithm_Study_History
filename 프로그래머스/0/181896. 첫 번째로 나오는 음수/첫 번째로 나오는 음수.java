class Solution {
    public int solution(int[] num_list) {
        int answer = 0;
        
        int index = 0;
        
        while(index != num_list.length)
        {
            if(num_list[index] < 0)
            {
                return index;
            }
            index++;
        }
        
        
        return -1;
    }
}