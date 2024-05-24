import java.util.*;

class Solution {
    public int[] solution(int n) 
    {
        ArrayList<Integer> list = new ArrayList<Integer>(); // 타입 지정
     
        for(int i = 1; i <= n; i++)
        {
            if(n % i == 0)
            {
                list.add(i);
            }
        }
        int[] answer = new int[list.size()];

        
        for (int i = 0; i < list.size(); i++) 
        {
            answer[i] = list.get(i); // 리스트의 각 요소를 배열에 복사
        }
        
        
       
        return answer;
    }
}