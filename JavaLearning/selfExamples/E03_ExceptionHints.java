
/**
 * Tips for Using Exceptions
 * 
 * @version 2023-07-21
 * @author Zhao Chonghao
 */

import java.util.*;

public class E03_ExceptionHints {
    public static void main(String[] args) {

        // 能用简单测试的地方不需要非得用异常handle
        System.out.println("处理时间为(毫秒): " + popSimple(1_000_000));
        System.out.println("处理时间为(毫秒): " + popException(1_000_000));

        // 不要把每行代码都隔离出一个try代码块

        // 要根据情况选择合适的异常，尽量细化到子异常或甚至自定义的异常

        // 仅在异常真的不重要时才不在catch中处理异常

        // 正确地在方法中选择throws和catch

        // 使用标准方法报告null-pointer或out-of-bounds异常
        Objects.requireNonNull(1); // obj = null时抛出异常
        Objects.checkIndex(0, 1); // index>=length时抛出异常
        Objects.checkFromToIndex(0, 0, 1);
        Objects.checkFromIndexSize(0, 1, 1);
        
        // 不要向终端用户展示堆栈跟踪日志

        // 堆栈跟踪不必通过catch生成，只需要调用以下方法
        Thread.dumpStack();
    }

    static long popSimple(int i) {
        Stack<String> s = new Stack<String>();
        long start = System.currentTimeMillis();
        while (i > 0) {
            // 简单的if测试
            if (!s.empty())
                s.pop();
            i--;
        }
        return System.currentTimeMillis() - start;
    }

    static long popException(int i) {
        Stack<String> s = new Stack<String>();
        long start = System.currentTimeMillis();
        while (i > 0) {
            // 复杂的异常测试
            try {
                s.pop();
            } catch (EmptyStackException e) {
            } finally {
                i--;
            }
        }
        return System.currentTimeMillis() - start;
    }
}
