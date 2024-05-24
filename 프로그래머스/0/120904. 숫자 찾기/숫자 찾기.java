class Solution {
    public int solution(int num, int k) 
    {
        int answer = 0;
        String str_num = Integer.toString(num);
        
        answer = str_num.indexOf(Integer.toString(k));
        
        if(answer != -1)
        {
            answer += 1;
        }
        
        
        return answer;
    }
}