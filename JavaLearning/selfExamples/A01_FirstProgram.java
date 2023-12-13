import static java.lang.Math.*;
import static java.lang.System.out;
import java.math.*;

/**
 * First Program.
 * 
 * @version 1.0 2023-04-17
 * @author Zhao Chonghao
 */

public class A01_FirstProgram {

    // Enumerated types are public static and final.
    enum Size {
        SMALL, MEDIUM, LARGE, EXTRA_LARGE
    };

    public static void main(String[] args) {
        out.println("This is my FIRST JAVA PROGRAM!");

        Double i = Double.NaN; // Floating value - NaN.
        if (Double.isNaN(i)) {
            out.println("i is NaN!");
        }

        // \u0022 (") will be converted to " before parsing.
        out.println("\u0027+\u0027");

        // Variables declaration and initialization.
        int vacationDays;
        vacationDays = 12;

        long earthPopulation;
        boolean done;
        double salary = 65000.0;

        var greeting = "Hello"; // Specified as a string automatically.

        // Referencing constant from class.
        out.println("1 inch equals to " + A01_FirstProgram.CM_PER_INCH + " cm.");

        // Enumerated Types.
        Size aSize = Size.LARGE;
        out.println(aSize);

        for (Size bSize : Size.values()) {
            out.print(bSize + " "); // Loop through a enum.
        }

        // Mathematical function.
        out.println(sin(salary));
        out.println(pow(salary, 1.0 / 2));
        out.println(atan2(Double.POSITIVE_INFINITY, Double.NEGATIVE_INFINITY) / Math.PI);

        // Lost precision.
        int n = 123456789;
        float f = n;
        out.println("n is " + n + ", but f is " + f + ".");

        // Round a float number.
        double x = 9.997;
        out.println("x is " + x + ", but simply int x is " + (int) x + ".");

        int nx = (int) round(x);
        out.println("x is " + x + ", and (int) Math.round(x) is " + nx + ".");

        // Big numbers.
        // in java.math package
        BigInteger a = BigInteger.valueOf(100);
        out.println(a);
        BigInteger reallyBig = new BigInteger("222232244629420445529739893461909967206666939096499764990979600");
        out.println(reallyBig);
        BigDecimal reallyPrecise = new BigDecimal(0.1);
        out.println(reallyPrecise);
        BigDecimal reallySmall = new BigDecimal("0.1"); // Always use String to keep precision.
        out.println(reallySmall);

        out.println(reallyBig.multiply(reallySmall.toBigInteger()));
    }

    // Create a class constant by keyword "final".
    public static final double CM_PER_INCH = 2.54;
}