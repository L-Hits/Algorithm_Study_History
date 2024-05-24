class Solution 
{
    public static int factorial(int n) //팩토리얼 함수 /오버플로우 남
    {
        if(n == 1)
        {
            return 1;
        }
        return n * factorial(n-1);
    }
    
    public static int combination(int n, int m) //조합 구하는 함수 /가능함
    {
        if(m == 0 || n == m)
        {
            return 1;
        }
        return combination(n-1, m-1) + combination(n-1, m);
    }
    
    
     public static int com(int n, int m) //재귀함수 안썼는데 안씀 -> 문제는 int형의 최대값에 있는듯 21억
     {
        // 예외 처리: m이 0이거나 n과 m이 같은 경우는 항상 1을 반환
        if (m == 0 || n == m) 
        {
            return 1;
        }
        
        // n개 중에서 m개를 선택하는 경우의 수를 계산
        int numerator = 1;
        int denominator = 1;
        for (int i = 0; i < m; i++) 
        {
            numerator *= (n - i);
            denominator *= (i + 1);
        }
        return numerator / denominator;
    }
    
    public int solution(int balls, int share) //확통에서의 balls c share
    {
        int answer = 0;
          
        //answer = factorial(balls) / (factorial(balls-share) * factorial(share));
        //오버플로우 발생
       
        answer = combination(balls, share);
        
        
        //answer = com(balls, share); 오버플로우 발생
        
        return answer;
    }
}