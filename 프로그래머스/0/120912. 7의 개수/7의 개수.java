class Solution 
{
    public int solution(int[] array) 
    {
        int answer = 0;
        String str = "";
        
        
        for(int i = 0; i < array.length; i++)
        {
            str += array[i]+"";
        }
        
        String new_str = str.replace("7", "");
        
        answer = str.length() - new_str.length();
        
        return answer;
    }
}