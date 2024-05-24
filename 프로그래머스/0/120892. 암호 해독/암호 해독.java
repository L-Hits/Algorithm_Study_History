class Solution {
    public String solution(String cipher, int code) 
    {
        String answer = "";
        
        String[] sp_st = cipher.split("");
        
        for(int i = 1; i <= sp_st.length / code; i++)
        {
            answer += sp_st[i*code-1];
            
        }
        return answer;
    }
}