import static java.lang.System.*;
import java.util.*;

/**
 * Arrays.
 * 
 * @version 1.0 2023-04-26
 * @author Zhao Chonghao
 */

public class A07_Arrays {
    public static void main(String[] args) {

        // declare
        int[] a;
        // initialize
        int[] b = new int[100]; // cannot change its length later
        // shortcut
        int[] smallPrimes = { 2, 3, 5, 7, 11, 13 };
        // string array
        String[] authors = {
                "Lu Xun",
                "Lao She",
                "Ba Jin",
                "Guo Moruo",
        };
        // anonymous array, reinitialize
        smallPrimes = new int[] { 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31 };
        // zero length array
        int[] empty = new int[] {};

        // array printing
        System.out.println(Arrays.toString(smallPrimes));

        // access elements
        for (int i = 0; i < 10; i++) {
            for (int j = 0; j < 10; j++) {
                int index = 10 * i + j;
                b[index] = index + 1;
                out.printf("%3d ", b[index]);
            }
            out.print("\n");
        }
        for (int i = 0; i < b.length; i++) {
            out.print(b[i] + " ");
        }

        // foreach loop
        out.print("\n");
        for (int i : smallPrimes) {
            out.print(i + " "); // print all i in smallPrimes
        }
        out.println(Arrays.toString(smallPrimes));

        // array copying
        int[] luckyNumbers = smallPrimes;
        out.println(smallPrimes + " " + luckyNumbers); // in same memory
        luckyNumbers = Arrays.copyOf(smallPrimes, 2 * smallPrimes.length);
        out.println(smallPrimes + " " + luckyNumbers); // in different memories

        // array sorting
        Random rd = new Random();
        int[] randomNumbers = new int[10];
        for (int i = 0; i < randomNumbers.length; i++) {
            randomNumbers[i] = rd.nextInt(1, 101);
        }
        out.println(Arrays.toString(randomNumbers));
        Arrays.sort(randomNumbers); // quick sort
        out.println(Arrays.toString(randomNumbers));

        // lottery draw
        Scanner in = new Scanner(System.in);

        // out.print("How many numbers to draw: ");
        // int n = in.nextInt();
        // out.print("What is the max number to draw: ");
        // int max = in.nextInt();
        int n = 7;
        int max = 36;

        int[] all = new int[max];
        int[] lottery = new int[n];
        int index = max - 1;

        for (int i = 0; i < all.length; i++)
            all[i] = i;
        for (int i = 0; i < n; i++) {
            int draw;
            if (index != 0) {
                draw = rd.nextInt(0, index);
            } else {
                draw = 0;
            }
            lottery[i] = all[draw] + 1;
            all[draw] = all[index];
            index--;
        }
        Arrays.sort(lottery);
        out.print("Your draw is:");
        for (int i = 0; i < lottery.length; i++)
            out.print(" " + lottery[i]);
        out.println();

        // multidimensional arrays
        double[][] returns = new double[10][6];

        for (int j = 0; j < returns[0].length; j++) {
            returns[0][j] = (j + 1) / 100.0;
            returns[1][j] = 10000;
        }
        for (int i = 2; i < returns.length; i++) {
            for (int j = 0; j < returns[0].length; j++) {
                returns[i][j] = returns[i - 1][j] * (1 + returns[0][j]);
            }
        }

        for (int j = 0; j < returns[0].length; j++) {
            out.printf("%9.0f%%", 100 * returns[0][j]);
        }
        out.println();
        for (int i = 1; i < returns.length; i++) {
            for (int j = 0; j < returns[0].length; j++) {
                out.printf("%10.2f", returns[i][j]);
            }
            out.println();
        }

        // ragged arrays
        int MAX = 10;
        int[][] yanghui = new int[MAX][];
        for (int i = 0; i < MAX; i++) {
            yanghui[i] = new int[i + 1]; // initialize each row
        }
        yanghui[0][0] = 1;

        for (int i = 1; i < MAX; i++) {
            yanghui[i][0] = yanghui[i - 1][0]; // initialize 1st column
            yanghui[i][i] = yanghui[i - 1][i - 1]; // initialize i-th column
        }
        for (int i = 2; i < MAX; i++) {
            for (int j = 1; j < i; j++) {
                yanghui[i][j] = yanghui[i - 1][j - 1] + yanghui[i - 1][j];
            }
        }
        
        for (int[] row : yanghui) {
            for (int r : row) {
                out.printf("%4d", r);
            }
            out.println();
        }
    }

}
