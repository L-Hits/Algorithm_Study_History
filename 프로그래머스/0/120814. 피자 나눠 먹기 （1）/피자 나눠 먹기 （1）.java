class Solution {
    public int solution(int n) {
        
        int answer = n / 7;
        
        // 만약 나머지가 0이 아니면, 피자가 하나 더 필요합니다.
        if (n % 7 != 0) {
            answer += 1;
        }
        
        return answer;
    }
}