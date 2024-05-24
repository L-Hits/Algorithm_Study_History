class Solution {
    public int solution(int price) 
    {
        int answer = 0;
        double price1 = (double)price;
        
        if(price >= 500000) 
        {
            price1 *= 0.8; // 20% discount for price >= 500,000
        } 
        else if (price >= 300000) 
        {
            price1 *= 0.9; // 10% discount for price >= 300,000 and price < 500,000
        } 
        else if (price >= 100000) 
        {
            price1 *= 0.95; // 5% discount for price < 300,000
        }

        answer = (int)price1;
        
        return answer;
    }
}