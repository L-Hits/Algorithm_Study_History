import java.util.*;

class Solution {
    public int solution(String before, String after)
    {
        int answer = 0;
        
        for(int i = 0; i < after.length(); i++)
        {
            char target = after.charAt(i); 
            before = before.replaceFirst(String.valueOf(target), "");
        }
        
        if(before.length() == 0)
        {
            answer = 1;
        }
        
        
        
        return answer;
    }
}