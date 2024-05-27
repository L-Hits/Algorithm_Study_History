class Solution {
    public int solution(String my_string) {
        int answer = 0; //숫자 아스키코드 49~57
        
        String[] str = my_string.split("");
        
        for(int i = 0; i < str.length; i++)
        {
            if( str[i].charAt(0) >= 47 && str[i].charAt(0) <= 57 )
            {
                answer += Integer.parseInt(str[i]);
            }
        }
        
        return answer;
    }
}