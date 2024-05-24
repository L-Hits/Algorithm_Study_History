import java.util.*;


class Solution {
    public String[] solution(String my_str, int n) 
    {
        int num = my_str.length()/n;
        String[] answer = new String[num];
        String[] arr_str = my_str.split("");
        String new_str = "";
        
        List<String> list = new ArrayList<>(Arrays.asList(arr_str));
        
        for(int i = num; i >= 1; i--)
        {
            list.add( n*i , "/");
        }
        
        arr_str = list.toArray(arr_str);
        
        for(int j = 0; j < arr_str.length; j++)
        {
            new_str += arr_str[j];
        }
        
        
        answer = new_str.split("/");

        
        return answer;
    }
}