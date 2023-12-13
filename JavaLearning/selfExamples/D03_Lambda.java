
/**
 * Lambda expressions. (Lambda表达式)
 * From Java 8.
 * 
 * @version 1.0 2023-07-01
 * @author Zhao Chonghao
 */

import com.chzhao.javalearning.persons.Employee;
import com.chzhao.javalearning.persons.Person;

import java.awt.event.*;
import java.awt.*;
import java.time.*;
import javax.swing.Timer;

import javax.swing.*;

import java.util.*;
import java.util.function.*;

public class D03_Lambda {
    public static void main(String[] args) {

        /*
         * Lambda表达式是一种用于精简代码的表达方法
         * 本质和Python里的匿名方法(Lambda)是一个东西，但是不能独立定义
         * 
         * 在D02回调方法中与D01Comparator接口中均将类的实例pass给一个方法
         * 且类中的方法不是当时就调用的，这时我们可以考虑Lambda表达式
         * 
         * 结构：
         * 1. 参数：无参数时()不能省略，单参数时()可以省略，变量类有时可省
         * 2. 右箭头->
         * 3. 表达式：多表达式时用{}括起来，无需声明输出的类型
         * 
         * 注意：Lambda表达式含有分支语句时必须定义所有分支的输出且类型需要一致
         * 注意：Lambda表达式仅适用于简化函数式接口的调用
         * 
         * 延申1 方法引用：
         * 当lambda表达式中的方法只有一条且只对参数进行了引用的话，可以进一步简化
         * var timer = new Timer(1000, event -> System.out.println(event));
         * 可以简化为
         * var timer = new Timer(1000, System.out::println);
         * 这被称为方法引用(method reference)
         * 格式：对象::实例方法名、类::静态方法名、类::动态方法名
         * 此处简化的方案即为类::静态方法名的情况
         * 更多实用的函数引用方法见 Core Java 1 Page 506
         * 
         * 延申2 构造函数引用：
         * 格式：类::new、类[]::new
         * n -> new int[n]; 可以简化为 int[]::new;
         * 具体见Core Java 2 Chapter 1
         * 部分类型不能使用这种方法，数组构造函数引用见Core Java 1 Chapter 8
         * 
         * 延申3 变量作用域：
         * lambda表达式中的参数都是表达式自身提供的，但是也可以使用外部的自由变量
         * 我们需要重新认识lambda表达式的结构：
         * 1. 一个代码块
         * 2. 参数
         * 3. 包裹代码块的外层函数中的自由变量的值
         * 注意：自由变量的值不能在lambda表达式块中变化，防止并发时不安全的调用
         * 也不能引用在lambda表达式块以外会变化的变量，更不能起和方法中同名的局部变量
         */

        // Arrays.sort可以自定义排序方法
        var planets = new String[] { "Mercury", "Venus", "Earth", "Mars",
                "Jupiter", "Saturn", "Uranus", "Neptune" };
        System.out.println("原数组:");
        System.out.println(Arrays.toString(planets));

        System.out.println("字典排序:");
        Arrays.sort(planets);
        System.out.println(Arrays.toString(planets));

        System.out.println("长度排序:");
        // Arrays.sort(planets, new LengthComparator());
        // 简化之后我们可以直接在方法里建立匿名实例，不必再通过类建立
        Arrays.sort(planets, (first, second) -> first.length() - second.length());
        System.out.println(Arrays.toString(planets));

        // java.util.function包中定义了很多函数式接口
        // 我们可以通过这种方式存储一个函数方法，然后用apply实现
        BiFunction<String, String, Integer> comp = (first, second) -> first.length() - second.length();
        String[] words = { "Long", "Longer" };
        if (comp.apply(words[0], words[1]) > 0) {
            System.out.printf("Word '%s' is longer than '%s'!\n", words[0], words[1]);
        } else {
            System.out.printf("Word '%s' is shorter than '%s'!\n", words[0], words[1]);
        }

        ArrayList<String> list = new ArrayList<>(
                Arrays.asList(null, "Test", "114", null, "514"));
        System.out.println("删除前: " + list);
        // list.removeIf(e -> e == null); // 可以用方法引用进一步简化
        list.removeIf(Objects::isNull); // removeIf中的参数是一个Predicate接口
        System.out.println("删除后: " + list);

        // lambda表达式的不同执行方法
        repeat(10, () -> System.out.println("Hello, world!"));
        repeatInt(10, i -> System.out.println("Countdown:" + (9 - i)));

        // 对一些接口中的默认方法，我们也可以直接用lambda表达式来调用
        // 这个例子中我们对姓名长度或薪水进行比较
        var staff = new Employee[3];
        staff[0] = new Employee("Simon", 35000);
        staff[1] = new Employee("Anna", 75000);
        staff[2] = new Employee("Mary", 38000);
        detailInfo(staff);
        Arrays.sort(staff,
                Comparator.comparing(Person::getName,
                        (s, t) -> Double.compare(s.length(), t.length())));
        detailInfo(staff); // 通过姓名长度排序
        Arrays.sort(staff, Comparator.comparingDouble(p -> p.getSalary()));
        detailInfo(staff); // 通过薪水排序

        // 定时器
        // var listener = new TimePrinter();
        // Timer timer = new Timer(1000, listener);

        // 简化之后我们可以直接在方法里建立匿名实例，不必再通过类建立
        // 函数式接口使我们编写lambda表达式时更关注函数本身
        Timer timer = new Timer(1000, event -> {
            System.out.println("At the tone, the time is " + Instant.ofEpochMilli(event.getWhen()));
            Toolkit.getDefaultToolkit().beep();
        });

        timer.start();

        // 通过自由变量进行方法化可以直接调用方法，该方法每1000毫秒println一次Hello
        // repeatMessage("Hello", 1000);

        JOptionPane.showMessageDialog(null, "Quit program?");
        System.exit(0);
    }

    /*
     * 这是一个使用自由变量的例子，是对上面定时器的方法化
     * lambda表达式里的text参数由外层的repeatMessage提供，并被lambda表达式捕捉(capture)
     */
    public static void repeatMessage(String text, int delay) {
        ActionListener listener = event -> {
            System.out.println(text);
            Toolkit.getDefaultToolkit().beep();
        };
        new Timer(delay, listener).start();
    }

    /*
     * lambda表达式起到延迟执行代码或在特定时间执行代码的作用
     * 以下方法给出了一个重复某个操作int n次的作用，其中通过Runnable函数式接口实现操作的重复
     * java中的重要函数式接口见Core Java 1 Page 514
     * 如下面的repeatInt方法，IntConsumer是Consumer<Integer>的一个特殊形式
     * java中的特殊函数式接口见Core Java 1 Page 516
     */
    public static void repeat(int n, Runnable action) {
        for (int i = 0; i < n; i++) {
            action.run();
        }
    }

    public static void repeatInt(int n, IntConsumer action) {
        for (int i = 0; i < n; i++) {
            action.accept(i);
        }
    }

    public static void detailInfo(Employee[] employees) {
        System.out.println("详细信息:");
        for (Employee e : employees) {
            System.out.println(e.toString());
        }
    }
}

/*
 * 以下是D02中应用ActionListener接口进行计时器事件发生的代码块，我们如何简化这一代码？
 * 
 * 这个方法可以简化为
 * event -> {
 * System.out.println("At the tone, the time is " +
 * Instant.ofEpochMilli(event.getWhen()));
 * Toolkit.getDefaultToolkit().beep();
 * }
 */
class TimePrinter implements ActionListener {
    public void actionPerformed(ActionEvent event) {
        System.out.println("At the tone, the time is " + Instant.ofEpochMilli(event.getWhen()));
        Toolkit.getDefaultToolkit().beep();
    }
}

/*
 * 以下是D01中应用Comparator接口进行String长度比较的代码块，我们如何简化这一代码？
 * 
 * 这个方法可以简化为
 * (first, second) -> first.length() - second.length()
 */
class LengthComparator implements Comparator<String> {
    public int compare(String first, String second) {
        return first.length() - second.length();
    }

}