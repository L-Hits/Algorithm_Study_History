class Solution {
    public int solution(String myString, String pat) 
    {
        int answer = 0;
        String[] str = myString.split("");
        String[] str_pat = pat.split("");

        for (int i = 0; i < str.length; i++) 
        {
            if (str[i].equals("A")) {
                str[i] = "B";
            } else if (str[i].equals("B")) 
            {
                str[i] = "A";
            }
        }

        for (int i = 0; i <= myString.length() - pat.length(); i++) 
        {
            int count = 0;
            while (count < pat.length()) 
            {
                if (!str[i + count].equals(str_pat[count])) 
                {
                    answer = 0;
                    break;
                }
                answer = 1; // 일치할 경우에만 1로 설정
                count++;
            }
            
            if (answer == 1) // 만약 일치하는 부분이 있다면 반복문 종료
                break;
        }

        return answer;
        
        //myString = myString.replace("A", "a").replace("B", "A").replace("a", "B");
        //return myString.contains(pat) ? 1 : 0;
    }
}