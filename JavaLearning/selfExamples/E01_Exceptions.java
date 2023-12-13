
/**
 * Java程序中的错误与异常
 * 
 * @version 1.0 2023-07-15
 * @author Zhao Chonghao
 */

import java.io.*;
import java.nio.charset.*;
import java.nio.file.*;
import java.util.*;

public class E01_Exceptions {
    public static void main(String[] args) {

        /*
         * 错误(Error)通常由错误的文件导入或错误的输入引起
         * 
         * 错误发生时，程序需要采取以下两种方法之一
         * 1. 返回到安全状态，提醒用户使用其他输入
         * 2. 保存用户的数据并关闭程序
         * 
         * 需要考虑到的因素包括但不限于：
         * 1. 用户的无效输入 (一般会输出IOException)
         * 2. 硬件设备未在线
         * 3. 设备容量限制
         * 4. 代码bug (一般会输出RuntimeException)
         */

        /*
         * Exception分为RuntimeException和其他exception
         * 
         * RuntimeException一般是因为代码有bug，包括但不限于
         * 1. 类型cast有误
         * 2. 数组长度不够
         * 3. null指针访问
         * 因此这种情况多半是代码编写者的问题
         * 
         * 其他exception包括但不限于
         * 1. 试图读取文件末尾之后的部分
         * 2. 试图读取不存在的文件
         * 3. 试图获取一个不属于任何类的对象的类
         * 
         * 因此可能抛出异常的情况包括但不限于
         * 1. 调用可能抛出检查异常的方法
         * 2. 侦测异常并使用throw抛出检查异常
         * 3. 编写者程序错误给出了未检查异常
         * 4. JVM或库的内部错误
         * 我们需要抛出的是前两种，即所有*检查异常*
         * 格式：方法名 (参数) throws 异常1, 异常2, ...
         * 注意：不要手动抛出错误和未检查异常，这两种无法控制
         * 注意：子类的方法不能抛出父类对应的方法更general的异常，但可以更specific或不抛出
         * 
         * 抛出异常的两种方法：
         * 1. 使用java.io内置已定义的异常
         * 2. 创建自定义异常
         */

        try {
            // 抛出内置异常的方法
            // 第一种，分体式
            var e = new EOFException("This is an exception.");
            throw e;

            // 第二种，合并式
            // throw new EOFException();
        } catch (Exception e) {
            System.out.println("EOFException caught.");
        }

        // 捕捉异常的方法：try代码块
        try {
            // 在try中捕捉到异常的话会自动跳过代码块中剩余的语句，并运行catch中的语句
            // 若无异常则自动跳过catch代码块
        } catch (Exception e) {
            // 处理异常的语句
        }

        // 用try语句构造读写文件的方法
        String pathIn = "selfExamples\\com\\chzhao\\resource\\textTestIn.txt";
        readData(pathIn);

        String pathOut = "selfExamples\\com\\chzhao\\resource\\textTestOut.txt";
        var context = new ArrayList<String>();
        readScanner(context, pathIn);
        printOut(context, pathOut);

        // 多层异常可以在抛出子系统中异常的同时保留原始异常的详细信息
        // 具体见Core Java 1 Chapter 7.2.3

        // finally代码块，实践中多使用try-with-resources代替
        // try-finally语句可以不包含catch代码块
        try {
        } finally {
            // 当try语句调用了资源时需要在finally中解除占用释放内存
            // 无论是否捕捉到异常都会执行
            // 因此不要在finally中return, throw, break, continue
        }
    }

    // 一个完整的用try语句读取输出文件内容的方法
    public static void readData(String filePath) {

        // 使用try-with-resources语句，不必在finally中用.close()关闭文件
        try (var fileInputStream = new FileInputStream(filePath)) {
            int readData = 0; // data初始化为0
            while ((readData = fileInputStream.read()) != -1) {
                // 逐字符输出
                System.out.print((char) readData);
            }
            System.out.println();
        } catch (FileNotFoundException | NullPointerException e) {
            // 多个异常共用一个处理方法，此时e为final
            System.out.println("文件路径不存在");
        } catch (IOException e) {
            // System.out.println(e.getClass().getName()); // 输出异常的类
            // System.out.println(e.getMessage()); // 输出异常详细信息
            e.printStackTrace(); // 输出异常详细信息
        }
    }

    // Scanner版
    public static void readScanner(ArrayList<String> context, String fileIn) {
        try (var in = new Scanner(Path.of(fileIn), StandardCharsets.UTF_8)) {
            while (in.hasNextLine()) {
                String line = in.nextLine();
                context.add(line.toString());
                System.out.println(line);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    // 写文件
    public static void printOut(ArrayList<String> lines, String fileOut) {
        try (var out = new PrintWriter(fileOut, StandardCharsets.UTF_8)) {
            for (String line : lines)
                out.println(line);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}

// 自定义异常的方法，本质上是类的继承
class FileFormatException extends IOException {
    public FileFormatException() {
    }

    public FileFormatException(String gripe) {
        super(gripe);
    }
}