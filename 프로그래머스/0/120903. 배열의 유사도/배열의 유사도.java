import java.util.*;


class Solution {
    public int solution(String[] s1, String[] s2) {
        int answer = 0;
        
         ArrayList<String> strList = new ArrayList<>(Arrays.asList(s2));
        
        for(int i = 0; i < s1.length; i++)
        {
            if(strList.contains(s1[i]))
            {
                answer++;
            }
            
        }
        return answer;
    }
}