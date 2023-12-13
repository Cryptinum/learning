
/**
 * Proxy. (代理)
 * 
 * @version 1.0 2023-07-13
 * @author Zhao Chonghao
 */

import java.lang.reflect.*;
import java.util.*;

public class D06_Proxy {
    public static void main(String[] arg) {

        /*
         * 代理类是允许在运行中实时创建应用接口的类
         * 一般用于希望应用接口但不知道接口具体性质的情况
         * blog.csdn.net/Passer_hua/article/details/122617628
         * 
         * 详见Core Java 1 Chapter 6.5
         * 
         * 代理类中一般需要定义这些方法：
         * 1. 应用的接口中的所有方法
         * 2. Object类中的所有方法
         * 代理类除了会监控类数组中的方法以外，还会监控Object类中的部分方法
         * 有toString, equals, hashCode
         * 
         * 代理类是自动public且final的，如果应用的类都public，代理类就不属于任何一个包
         */

        var elements = new Object[1000];

        // fill elements with proxies for the integers 1 . . . 1000
        for (int i = 0; i < elements.length; i++) {
            // 注意Integer实际上应用了Comparable接口
            Integer value = i + 1;

            // 建立我们定义的请求处理器示例
            var handler = new TraceHandler(value);

            /*
             * 用Proxy.newProxyInstance创建一个代理对象，有三个参数：
             * 1. 类加载器，详见Core Java 2 Chapter 9
             * 2. 类数组，一般定义为new Class[] {}
             * 3. 请求处理器(invocation handler)
             * 代理类只有一个实例域handler
             * 
             * 本例中我们的handler会跟踪所有Comparable下的类的方法调用
             */
            Object proxy = Proxy.newProxyInstance(
                    ClassLoader.getSystemClassLoader(),
                    new Class[] { Comparable.class }, handler);

            // 跟踪elements中的参数
            elements[i] = proxy;
        }

        // 随机数
        Integer key = (int) (Math.random() * elements.length) + 1;

        // 二分法查找
        // 实际上判断了if (elements[i].compareTo(key) < 0)，调用了invoke
        int result = Arrays.binarySearch(elements, key);

        // 找到后输出这个数
        // 对数组元素的println调用了.toString()
        // 尽管不属于Comparable，特定的Object方法仍然会被调用
        if (result >= 0)
            System.out.println(elements[result]);
    }
}

/*
 * 用代理和请求处理器跟踪方法调用
 */
class TraceHandler implements InvocationHandler {

    private Object target;

    public TraceHandler(Object t) {
        target = t;
    }

    public Object invoke(Object proxy, Method m, Object[] args) throws Throwable {
        // 隐式参数
        System.out.print(target);
        // 方法名
        System.out.print("." + m.getName() + "(");
        // 显式参数
        if (args != null) {
            for (int i = 0; i < args.length; i++) {
                System.out.print(args[i]);
                if (i < args.length - 1)
                    System.out.print(", ");
            }
        }
        System.out.println(")");

        return m.invoke(target, args);
    }
}