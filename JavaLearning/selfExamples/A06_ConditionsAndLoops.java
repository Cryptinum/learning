import java.util.*;
import static java.lang.System.*;
import static java.lang.Math.*;

/**
 * Conditions and loops.
 * 
 * @version 1.0 2023-04-25
 * @author Zhao Chonghao
 */

public class A06_ConditionsAndLoops {
    public static void main(String[] args) {

        // Condition.
        int target = 500;
        double bonus;
        String performance;

        Scanner in = new Scanner(System.in);
        out.print("How much is your sales? ");
        int yourSales = in.nextInt();

        if (yourSales >= target) {
            performance = "Satisfactory";
            bonus = 100 + 0.01 * (yourSales - target);

            String message = String.format(
                    "Well done, your sales is %d, more than the sale target %d.\nYour performance is %s and will get bonus of %.2f!",
                    yourSales, target, performance, bonus);
            out.println(message);
        } else {
            performance = "Unsatisfactory";
            bonus = 0;

            String message = String.format(
                    "Oops, your sales is %d, didn't reach the sale target %d.\nYour performance is %s and will get bonus of %.0f!",
                    yourSales, target, performance, bonus);
            out.println(message);
        }

        // multiple selections
        out.print("Select an option (1, 2, 3, 4): ");
        int choice = in.nextInt();
        String ball;
        ball = switch (choice) {
            case 1 -> "Red ball";
            case 2 -> "Yellow ball";
            case 3 -> "Green ball";
            case 4 -> "Brown ball";
            default -> "Bad choice";
        };
        out.println(ball);

        // while loop
        // Calculate present value of bond.
        out.print("Coupon face value: ");
        double faceValue = in.nextDouble();
        out.print("Coupon rate: ");
        double couponRate = in.nextDouble();
        double couponPayments = faceValue * couponRate / 100;
        out.print("Market interest rate: ");
        double marketInterest = in.nextDouble() / 100;
        out.print("Number of payments: ");
        int paymentNumber = in.nextInt();

        double marketValue = 0;
        int number = 1;

        while (number <= paymentNumber) {
            marketValue += couponPayments / pow((1 + marketInterest), number);
            number++;
        }
        marketValue += faceValue / pow((1 + marketInterest), paymentNumber);
        String message = String.format("The market value of your coupon is %.2f.", marketValue);
        out.println(message);

        // for loop
        for (int i = 1; i <= 10; i++)
            out.print(i + " ");

    }
}