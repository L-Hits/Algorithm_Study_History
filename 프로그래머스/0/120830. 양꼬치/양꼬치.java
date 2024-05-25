class Solution {
    public int solution(int n, int k) {
        int answer = 0;
        //n 양꼬치, k 음료수 먹은 개수
        
        int eatOver = n / 10;
        
        if( eatOver != 0)    //10인분 이상 먹음
        {
            answer = (12000 * n) + (k - eatOver) * 2000;
        }
        else
            answer = (12000 * n) + (2000 * k);
        
        return answer;
    }
}