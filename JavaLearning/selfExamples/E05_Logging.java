
/**
 * Logging. (日志)
 * 
 * @version 1.0 2023-07-23
 * @author Zhao Chonghao
 */

import java.io.*;
import java.util.*;
import java.util.logging.*;

public class E05_Logging {
    public static void main(String[] args) {

        /*
         * 日志可以有以下功能
         * 1. 可以开关部分异常的日志
         * 2. 可以同时在控制台和文件中显示
         * 3. 可以过滤筛选不同异常的日志
         * 4. 可以以不同的格式显示
         * 5. 可以生成多个日志文件
         * 6. 日志通过配置文件进行配置
         * 
         * 可以用外部日志框架，如
         * Log4J https://logging.apache.org/log4j/2.x
         * Logback https://logback.qos.ch
         * SLF4J https://www.slf4j.org
         * Commons Logging https://commons.apache.org/proper/commons-logging
         * 
         * 日志代理是一种通过创建匿名子类，用子方法生成父方法日志的技巧
         * 
         * 具体见 Core Java 1 Chapter 7.5
         */

        /*
         * 在命令行中可以输出程序的所有错误日志
         * 输出System.out:
         * java MyProgram > errors.txt
         * 输出System.err:
         * java MyProgram 2> errors.txt
         * 输出二者:
         * java MyProgram 1> errors.txt 2>&1
         */

        // 使用global logger的info方法进行简单的日志生成
        Logger.getGlobal().info("File->Open menu item selected");

        // 抑制该行以后的日志生成
        Logger.getGlobal().setLevel(Level.OFF);
        Logger.getGlobal().setLevel(Level.FINEST); // 重新打开所有log

        // 一些日志方法
        myLogger.setLevel(Level.FINEST); // 细化某个Logger的日志信息
        myLogger.warning("一条警告信息");
        myLogger.fine("一条明细信息");
        myLogger.log(Level.WARNING, "另一条警告信息");
        // 明细用logp
        myLogger.logp(Level.WARNING, "测试类", "测试方法", "测试信息", myLogger);

        // 用日志记录异常
        try {
            Stack<String> s = new Stack<String>();
            s.pop();
        } catch (EmptyStackException e) {
            Logger.getLogger("E05_Logging").log(Level.WARNING, "空栈", e);
        }

        // 自定义handler
        Logger logger = Logger.getLogger("com.mycompany.myapp");
        logger.setLevel(Level.FINE);
        logger.setUseParentHandlers(false);
        var handler = new ConsoleHandler();
        handler.setLevel(Level.FINE);
        logger.addHandler(handler);

        // *日志代理*
        // 当nextDouble方法被调用时，一条日志信息就被生成
        var generator = new Random() {
            public double nextDouble() {
                double result = super.nextDouble();
                Logger.getGlobal().info("nextDouble: " + result);
                return result;
            }
        };
        System.out.println(generator.nextDouble()); // 从内向外

        // 堆栈跟踪生成日志
        var out = new StringWriter();
        new Throwable().printStackTrace(new PrintWriter(out));
        String description = out.toString();
        System.out.println(description);
    }

    // 不被任何变量引用的logger可能被garbage-collected，用static避免
    private static final Logger myLogger = Logger.getLogger("com.chzhao");
}