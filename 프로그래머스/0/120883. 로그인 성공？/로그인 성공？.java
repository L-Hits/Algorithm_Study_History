class Solution {
    public String solution(String[] id_pw, String[][] db) 
    {
        String answer = "";
        
        for(int i = 0; i < db.length; i++)
        {
            if(id_pw[0].equals(db[i][0]))   //아이디만 같은지 비교
            {
                if(id_pw[1].equals(db[i][1])) // 로그인 성공
                {
                    answer = "login";
                }
                else    //아이디는 같으나 비번이 다름
                {
                    answer = "wrong pw";
                }
                break;
            }
            else
            {
                answer = "fail";
            }
        }
        
        return answer;
    }
}