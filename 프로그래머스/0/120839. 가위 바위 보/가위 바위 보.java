class Solution {
    public String solution(String rsp) 
    {
        String answer = "";
        
        String[] next_answer = rsp.split("");
        
        for(int i = 0; i < next_answer.length; i++)
        {
            switch(next_answer[i])
            {
                case "2":
                    {
                        answer +="0";
                        break;
                    }
                case "0":
                    {
                        answer +="5";
                        break;
                    }
                case "5":
                    {
                        answer +="2";
                        break;
                    }
            }
        }
        
        return answer;
    }
}