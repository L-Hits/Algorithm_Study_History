class Solution {
    public int solution(int[] array) 
    {   
        int change;
        
        
        for(int i = 0; i < array.length; i ++)
        {
            for(int j = i +1; j <array.length; j++)
            {
                if (array[j] < array[i])
            {
                change = array[i];
                array[i] = array[j];
                array[j] = change;
            }
            }
        }
        return array[array.length / 2];
        
    }
}