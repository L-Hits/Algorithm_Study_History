import java.util.*;

class Solution 
{
    public int[] solution(int n, int[] numlist) 
    {
        ArrayList<Integer> list = new ArrayList<>();
        
        for(int i = 0; i < numlist.length; i++)
        {
            if(numlist[i] % n == 0)
            {
                list.add(numlist[i]);
            }
        }
        int[] answer = new int[list.size()];    //리스트 크기만큼 정적배열을 하나 만들어 준다.
        
        for(int j = 0; j < list.size(); j ++)
        {
            answer[j] = list.get(j);
        }
        
        
        return answer;
    }
}