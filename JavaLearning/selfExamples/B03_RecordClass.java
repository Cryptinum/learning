import static java.lang.System.*;
import java.util.*;

/**
 * Record class and example.
 * From JDK16.
 * 
 * @version 1.0 2023-05-02
 * @author Zhao Chonghao
 */

public class B03_RecordClass {
    public static void main(String[] arg) {

        var p = new Point(3, 4);
        out.println("Coordinates of p: (" + p.x() + "," + p.y() + ")");
        out.println("Distance from origin: " + p.distanceFromOrigin());
        out.println("Distance from origin: " + Point.distance(Point.ORIGIN, p));

        // A mutable record
        var pt = new PointInTime(3, 4, new Date());
        out.println("Before: " + pt);
        pt.when().setTime(0);
        out.println("After: " + pt);

        // Invoking a compact constructor

        var r = new Range(4, 3);
        out.println("r: " + r);

    }
}

/*
 * A record class has a intrinsic instance fields.
 * For record Point(double x, double y), we have
 * - private final double x;
 * - private final double y;
 * in this situation, the instance fields of a record are called its components.
 * 
 * This class also have a constructor of (namely Canonical constructor)
 * - Point(double x, double y)
 * and accessor methods
 * - public double x()
 * - public double y()
 */
record Point(double x, double y) {

    // add instance fields to a record is not allowed
    // private double r; // ERROR

    // define custom constructor by invoke canonical constructor
    public Point() {
        this(0, 0);
    }

    // define own methods.
    public double distanceFromOrigin() {
        return Math.hypot(x, y);
    }

    // static fields and methods
    public static Point ORIGIN = new Point(0, 0);

    public static double distance(Point p, Point q) {
        return Math.hypot(p.x - q.x, p.y - q.y);
    }
}

record PointInTime(double x, double y, Date when) {
}

/*
 * Provide custom implementation in the custom constructor.
 */
record Range(int from, int to) {

    // more encouraged to use compact form
    // this will run before 'from' and 'to' assigned to this.from and this.to
    public Range {
        if (from > to) {
            int temp = from;
            from = to;
            to = temp;
        }
    }
}