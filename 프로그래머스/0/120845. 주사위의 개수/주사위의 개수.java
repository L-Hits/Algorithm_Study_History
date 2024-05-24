class Solution 
{
    public int solution(int[] box, int n) 
    {
        int answer = 1;
        
        int[] dice_xyz = new int[3];
        
        for(int i = 0; i < 3; i++)  //몫
        {
            dice_xyz[i] = box[i] / n;
            
        }

        
        for(int j = 0; j < 3; j++)
        {
            if(dice_xyz[j] != 0)
            {
                answer *= dice_xyz[j];
            }
            else //0이면
            {
                answer = 0;
            }
            
        }
        
        return answer;
    }
}