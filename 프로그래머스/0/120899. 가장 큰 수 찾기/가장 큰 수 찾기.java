import java.util.*;

class Solution {
    public int[] solution(int[] array) {
        int[] answer = new int[2];
        
        // int[] 배열을 Integer[] 배열로 변환
        Integer[] integerArray = Arrays.stream(array).boxed().toArray(Integer[]::new);
        
        // Integer[] 배열을 리스트로 변환
        ArrayList<Integer> list = new ArrayList<>(Arrays.asList(integerArray));
        
        // 리스트에서 최대값을 찾음
        answer[0] = Collections.max(list);
        
        // 리스트에서 최대값의 인덱스를 찾음
        answer[1] = list.indexOf(answer[0]);
        
        return answer;
    }
}