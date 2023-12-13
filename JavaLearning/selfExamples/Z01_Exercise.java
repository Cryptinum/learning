import java.util.*;

public class Z01_Exercise {

    public static void main(String[] args) {
        int[] nums = new int[] { 2, 7, 11, 15 };
        int target = 9;
        int[] sum = new int[] {};
        sum = twoSum(nums, target);
        System.out.println(Arrays.toString(sum));
    }

    public static int[] twoSum(int[] nums, int target) {
        int n = nums.length;
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if (nums[i] == target - nums[j]) {
                    return new int[] { i, j };
                }
            }
        }
        return new int[] {};
    }
}
