class Solution {
    public int[] solution(int n, int k) {
        int[] answer = new int[ n/k ];
        int num = 2;
        int after_num = 1 * k;
        
        for(int i = 0; i < answer.length; i++)
        {
            if(after_num <= n)
            {
                answer[i] = after_num;
                after_num = k * num;
                num++;
            }
            else 
                return answer;
            
        }
        
        return answer;
    }
}