import java.util.ArrayList;

class Solution {
    public int maxSubArray(int[] nums) {
        int curSub = nums[0];
        int curSum = 0;
        
        for(int i = 0; i < nums.length; i++){
            if(curSum < 0){
                curSum = 0;
            }
            curSum += nums[i];
            curSub = Math.max(curSub, curSum);
        }
        return curSub;
    }
}