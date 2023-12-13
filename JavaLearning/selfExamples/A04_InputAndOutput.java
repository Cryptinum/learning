import java.util.*; // Scanner is in this package.
import java.io.Console;
import static java.lang.System.*;

/**
 * Input and output.
 * 
 * @version 1.0 2023-04-25
 * @author Zhao Chonghao
 */

public class A04_InputAndOutput {
    public static void main(String[] args) {

        // Construct a new scanner.
        Scanner in = new Scanner(System.in);

        // read a line of string
        out.print("What is your name? ");
        String name = in.nextLine();
        out.println("Hello, " + name + ".");

        // read a word, delimited by whitespace
        out.print("What is your full name? ");
        String lastName = in.next();
        String firstName = in.next();
        out.println("Last name: " + lastName);
        out.println("First name: " + firstName);

        // read an integer
        out.print("How old are you? ");
        int age = in.nextInt();
        out.println("You are " + age + " years old.");

        // Scanner is not suitable for reading password, use Console
        Console cons = System.console();
        String username = cons.readLine("User name: ");
        char[] passwd = cons.readPassword("Password: ");

    }
}
