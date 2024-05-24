class Solution {
    public String solution(int age) 
    {
        String[] arr = {"a","b","c","d","e","f","g","h","i","j"};
        String answer = "";
        
        String str = Integer.toString(age);
		for(int i = 0; i<str.length(); i++)
		{
			char k = str.charAt(i); //문자 하나를 가져와서 변경
			int num = Character.getNumericValue(k);
			answer += arr[num];
		}
        
        
        
        return answer;
    }
}