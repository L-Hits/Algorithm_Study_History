class Solution {
    public String solution(String my_string) 
    {
        String answer = "";
        
        String[] str = my_string.split("");
        
        for(int i = 0; i < str.length; i++)
        {
            answer += str[str.length -i -1];
        }
        return answer;
    }
}