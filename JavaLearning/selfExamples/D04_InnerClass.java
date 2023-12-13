
/**
 * Inner classes. (内部类)
 * 
 * @version 1.0 2023-07-13
 * @author Zhao Chonghao
 */

import com.chzhao.javalearning.persons.Employee;

import java.awt.event.*;
import java.awt.*;
import java.time.*;
import javax.swing.*;
import javax.swing.Timer;

import java.util.*;
import java.util.List;

public class D04_InnerClass {
    public static void main(String[] args) {

        /*
         * 内部类是定义在其他类中的类，我们基于如下动机
         * 1. 内部类可以对同一个包的其他类隐藏
         * 2. 内部类可以访问类中的private变量
         * 
         * 内部类可以过去被用来回调函数，目前被lambda表达式取代
         * 注意：内部类不能是static的
         */

        // 实例和匿名内部类的区别
        var e1 = new Employee(10000); // 一个Employee对象
        var e2 = new Employee(20000) { // 一个拓展Employee类的内部类对象
        };

        // 用双括号技巧简化只出现一次的实例，比较少见
        var friends = new ArrayList<String>();
        friends.add("Harry");
        friends.add("Tony");
        invite(friends);
        // 以上可以简化为这种
        invite(new ArrayList<String>() { // 外层大括号定义了匿名内部类
            {
                // 内层大括号对变量进行了初始化
                add("Harry");
                add("Tony");
            }
        });
        invite(List.of("Harry", "Tony")); // 特别地，还能这样简化

        // 静态内部类示例
        Random rand = new Random();
        double[] d = new double[10];
        for (int i = 0; i < d.length; i++) {
            d[i] = ((double) Math.round(rand.nextDouble(0, 100) * 100)) / 100;
        }
        System.out.println(Arrays.toString(d));
        ArrayAlg.Pair p = ArrayAlg.minmax(d); // 静态内部类的引用
        System.out.println("min = " + p.getFirst());
        System.out.println("max = " + p.getSecond());

        // var clock = new TalkingClock(1000, true);
        // clock.start();

        var clock = new TalkingClock();
        clock.start(1000, true);

        // 展示一个对话框，保持计时器运行直到用户点击确定
        JOptionPane.showMessageDialog(null, "退出程序？");
        System.exit(0);

    }

    public static void invite(List<String> list) {
        // 局部变量List<String> list使得我们可以接收List和ArrayList
    }
}

class TalkingClockOld {
    private int interval;
    private boolean beep;

    public TalkingClockOld(int interval, boolean beep) {
        this.interval = interval;
        this.beep = beep;
    }

    public void start() {
        var listener = new TimePrinter();
        var timer = new Timer(interval, listener);
        timer.start();
    }

    /*
     * 内部类的例子，这说明了并非所有TalkingClock都有TimePrinter实例域
     * TimePrinter中调用了TalkingClock中的private变量beep
     * 
     * 内部类中实际上自动定义了class TimePrinter(TalkingClock clock)
     * 所以beep实际上是是clock.beep
     * 抽象地，beep是OuterClass.this.beep，通过外部类的实例访问private变量
     * 
     * 特别地，由于TimePrinter在本例子中只在start()方法中出现
     * 那么，这个内部类也可以定义在start()方法中，进一步提高私密性且可以访问方法的局部变量
     * 称局部地定义在方法中的内部类为：局部内部类(local inner class)
     * 局部内部类无法定义可访问性(public或private)
     * 
     * 更特别地，由于TimePrinter在本例子中只在start()方法中出现并只建立了一个实例
     * 那么，这个局部内部类也可以直接调用接口定义为new ActionListener() {...};
     * 称这种不出现类名的的局部内部类为：匿名内部类(anonymous inner class)
     * 格式：var 实例名 = new 父类或接口(构造变量) {内部类的方法和数据};
     * 匿名内部类无法创建构造器(constructor)
     */
    class TimePrinter implements ActionListener {

        public void actionPerformed(ActionEvent event) {
            System.out.println("At the tone, the time is "
                    + Instant.ofEpochMilli(event.getWhen()));
            // 相对于D02中的例子检查了beep，因为在上面的域中我们定义了是否beep
            if (beep) {
                Toolkit.getDefaultToolkit().beep();
            }
        }
    }
}

// 通过匿名内部类简化的计时器主体
class TalkingClock {

    public void start(int interval, boolean beep) {
        var listener = new ActionListener() {
            public void actionPerformed(ActionEvent event) {
                System.out.println("At the tone, the time is "
                        + Instant.ofEpochMilli(event.getWhen()));
                if (beep) {
                    Toolkit.getDefaultToolkit().beep();
                }
            }
        };

        var timer = new Timer(interval, listener);
        timer.start();
    }
}

/*
 * 通过静态内部类压缩main中的代码
 * 静态内部类(static inner class)也被称为嵌套类(nested class)
 * 
 * 静态内部类一般用于内部类无需访问外部类对象的情况
 * 静态内部类可以有静态域和静态方法
 * 定义在接口内的类是自动static并且public的
 * 定义在类中的接口、记录类、枚举类是自动static的
 */

class ArrayAlg {

    public static class Pair {
        private double first;
        private double second;

        public Pair(double f, double s) {
            first = f;
            second = s;
        }

        public double getFirst() {
            return first;
        }

        public double getSecond() {
            return second;
        }
    }

    public static Pair minmax(double[] values) {
        double min = Double.POSITIVE_INFINITY;
        double max = Double.NEGATIVE_INFINITY;
        for (double v : values) {
            if (min > v) min = v;
            if (max < v) max = v;
        }
        return new Pair(min, max);
    }
}