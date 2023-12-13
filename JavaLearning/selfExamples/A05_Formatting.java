import static java.lang.System.*;

/**
 * Formatting output.
 * 
 * @version 1.0 2023-04-25
 * @author Zhao Chonghao
 */

public class A05_Formatting {
    public static void main(String[] args) {

        double x = 10000.0 / 3.0;
        out.println("x = " + x);
        out.printf("x = %,+.2f", x);

        String name = "Fred";
        int age = 24;
        out.printf("\nHello, %s. Next year, you'll be %d.\n", name, age + 1);
        String message = String.format("Hello, %s. Next year, you'll be %d.", name, age + 1);
        out.println(message);
    }
}
