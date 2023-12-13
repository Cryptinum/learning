import java.time.*;
import static java.lang.System.*;
import java.util.*;

/**
 * Predefined classes.
 * Use java.time.LocalDate to write a program that can show the
 * calendar of given month.
 * 
 * @version 1.0 2023-04-28
 * @author Zhao Chonghao
 */

public class B01_PredefinedClasses {
    public static void main(String[] args) {

        // Scanner in = new Scanner(System.in);
        // out.print("Input year month day (separate by spaces): ");
        // int year = in.nextInt();
        // int month = in.nextInt();
        // int day = in.nextInt();

        // LocalDate date = LocalDate.of(year, month, day);
        LocalDate date = LocalDate.now();
        int year = date.getYear();
        int month = date.getMonthValue();
        int day = date.getDayOfMonth();

        date = date.minusDays(day - 1); // set to the start of the month.
        DayOfWeek weekDay = date.getDayOfWeek(); // get the start weekday of the month.
        int weekValue = weekDay.getValue(); // turn weekday to value.

        out.printf("Calendar of %d-%d\n", year, month);
        out.println("Mon Tue Wed Thu Wed Sat Sun");
        for (int i = 1; i < weekValue; i++)
            out.print("    ");

        while (date.getMonthValue() == month) {
            out.printf("%3d", date.getDayOfMonth());
            if (date.getDayOfMonth() == day)
                out.print("*");
            else
                out.print(" ");
            if (date.getDayOfWeek().getValue() == 7)
                out.println();
            date = date.plusDays(1);
        }
    }
}
