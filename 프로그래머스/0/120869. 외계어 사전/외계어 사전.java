class Solution {
    public int solution(String[] spell, String[] dic) 
    {
        int answer = 0;
        
        boolean t_f = false;
        
        
        for (int i = 0; i < dic.length; i++) 
        {
            int count = 0;
            for (int j = 0 ; j < spell.length; j++) 
            {
                if (dic[i].contains(spell[j])) count++;
            }
            
            if (count == spell.length) //dic 안에있는 단어중 하나라도 가능하면 for문 중지 
            {
                t_f = true;
                break;
            }
        }
        
        if(t_f)
        {
            answer = 1;
        }
        else
        {
            answer = 2;
        }
        return answer;
    }
}

/*
dic의 문자열마다 spell에 있는 단어가 없으면 다음 단어로 넘김.
넘기기 전에는 answer = 2로 고정

단어가 있으면 answer = 1로 하고 break

spell에 있는 단어가 하나라도 있으면

true

어떻게 하지..?

dic의 단어와 spell에 있는 것들을 따로 비교하는 변수 필요.

dic의 단어 하나마다 spell에 있는 모든 단어가 다 맞으면
모든 반복문을 중지.

-> true
*/