
/**
 * Stack trace. (堆栈跟踪)
 * 
 * @version 2023-07-21
 * @author Zhao Chonghao
 */

import java.io.*;
import java.util.*;

public class E02_StackTrace {

    public static void main(String[] args) {

        /*
         * 堆栈跟踪(stack trace)是一个堆栈数组，用来收集方法调用的信息并给出位置
         * 具体见Core Java 2 Chapter 1
         */

        // 堆栈跟踪
        var t = new Throwable();
        var out = new StringWriter();
        t.printStackTrace(new PrintWriter(out)); // 用printStackTrace
        String description = out.toString();
        System.out.println(description); // 输出行号和类(Throwable)

        // 更灵活的方式
        StackWalker walker = StackWalker.getInstance();
        walker.forEach(frame -> System.out.println(frame)); // 直接输出行号

        // 在方法中使用堆栈跟踪
        try (var in = new Scanner(System.in)) {
            System.out.print("Enter n: ");
            int n = in.nextInt();
            factorial(n);
        }
    }

    /**
     * 计算一个整数的阶乘
     * 
     * @param n 非负整数
     * @return n! = 1 * 2 * . . . * n
     */
    public static int factorial(int n) {
        System.out.println("factorial(" + n + ")");
        var walker = StackWalker.getInstance();
        walker.forEach(System.out::println);
        int r;
        if (n <= 1)
            r = 1;
        else
            r = n * factorial(n - 1);
        System.out.println("return " + r);
        return r;
    }
}
