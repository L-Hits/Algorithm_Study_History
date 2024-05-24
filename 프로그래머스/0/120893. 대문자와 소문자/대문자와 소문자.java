class Solution {
    public String solution(String my_string) 
    {
        String answer = "";
        // a (65 ~ 90)+32  -> A 97 ~ 122
        String[] arr = my_string.split("");
        int asci;
        
        for(int i= 0; i < arr.length; i++)
        {
            asci = (int)(arr[i].charAt(0));
            
            if(asci < 97) //소문자라면
            {
                asci += 32;
            }
            
            else
            {
                asci -= 32;
            }
            
            answer += (char)asci;
        }
        
        return answer;
    }
}