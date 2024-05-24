import java.util.Arrays;

class Solution {
    public int[] solution(int[] emergency) {
        int[] answer = new int[emergency.length];
        
        // 원래 배열을 복사하여 정렬
        int[] sortedEmergency = Arrays.copyOf(emergency, emergency.length);
        Arrays.sort(sortedEmergency);
        
        // 정렬된 배열에서 각 요소의 인덱스를 찾아서 answer에 저장
        for (int i = 0; i < emergency.length; i++) {
            int index = Arrays.binarySearch(sortedEmergency, emergency[i]);
            answer[i] = emergency.length - index;
        }
        
        return answer;
    }
}