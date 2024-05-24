class Solution {
    public int solution(String my_string) 
    {
        int answer = 0;
        
        String[] str = my_string.split(" ");
        
        answer = Integer.parseInt(str[0]);
        /*
            결과 result를 정의해주고
            다음 인덱스에 오는 str이 + 혹은 - 이면 그 전에 있던 값이랑 다음에 오는 값을 result에 업데이트 해준다.
            이를 반복.
        */
        
        for(int i = 1; i < str.length-1; i++) // 인덱스 1부터 시작 str[1] 
        {
            if(str[i].equals("+") || str[i].equals("-")) //연산자라면.
            {
                        
                if(str[i].equals("+")) //+인 경우
                {
                    answer += Integer.parseInt(str[i+1]);
                }
                else // -인 경우
                {
                    answer -= Integer.parseInt(str[i+1]);
                }
                
            }
        }
      
        return answer;
    }
}