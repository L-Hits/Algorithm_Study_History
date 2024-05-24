import java.util.*;


class Solution 
{
    public int[] solution(String my_string) 
    {
        
        my_string = my_string.replaceAll("[a-z]",""); //문자열에서 소문자를 다 제거 - > 숫자들만 남음

        int[] answer = new int[my_string.length()]; //남은 숫자의 개수만큼 배열의 크기를 정의

        for(int i = 0; i < answer.length; i++)
        {
            answer[i] = my_string.charAt(i) - '0';
        }

        Arrays.sort(answer); //정렬

        return answer;
       
    }
}