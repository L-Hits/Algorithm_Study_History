class Solution {
    public String solution(String my_string, String letter) 
    {
        String answer = "";
        String[] change_answer = my_string.split("");
        
        for(int i = 0; i < change_answer.length; i++)
        {
            if(change_answer[i].equals(letter))
            {
                change_answer[i] = "";
            }
            answer += change_answer[i];
        }
        return answer;
    }
}