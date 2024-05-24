class Solution 
{
    public long solution(String numbers) 
    {
        long answer = 0;
        numbers = numbers.replace("zero", "0");
        numbers = numbers.replace("one", "1");
        numbers = numbers.replace("two", "2");
        numbers = numbers.replace("three", "3");
        numbers = numbers.replace("four", "4");
        numbers = numbers.replace("five", "5");
        numbers = numbers.replace("six", "6");
        numbers = numbers.replace("seven", "7");
        numbers = numbers.replace("eight", "8");
        numbers = numbers.replace("nine", "9");
        
        
        
        
        /*
        String str_answer = "";
        
        String[] str = numbers.split("");
        String word = "";
        
        
        
        for(int i = 0; i < str.length; i++)
        {
            word += str[i];
            if (word.length() > 2)
            {
                switch(word)
                {
                    case "zero":
                        str_answer += "0";
                        word = "";
                        break;
                    case "one":
                        str_answer += "1";
                        word = "";
                        break;
                    case "two":
                        str_answer += "2";
                        word = "";
                        break;
                    case "three":
                        str_answer += "3";
                        word = "";
                        break;
                    case "four":
                        str_answer += "4";
                        word = "";
                        break;
                    case "five":
                        str_answer += "5";
                        word = "";
                        break;
                    case "six":
                        str_answer += "6";
                        word = "";
                        break;
                    case "seven":
                        str_answer += "7";
                        word = "";
                        break;
                    case "eight":
                        str_answer += "8";
                        word = "";
                        break;
                    case "nine":
                        str_answer += "9";
                        word = "";
                        break;
                }
            }
        }
        */
        
        
        answer = Long.parseLong(numbers);
        
        
        
        
        return answer;
    }
}