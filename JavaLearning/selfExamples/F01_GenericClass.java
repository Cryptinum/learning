import java.time.LocalDate;
import java.util.*;
import com.chzhao.javalearning.*;

/**
 * Generic Programming and Generic Classes. (泛型编程与泛型类)
 * 
 * @version 1.0 2023-07-29
 * @author Zhao Chonghao
 */

public class F01_GenericClass {
    public static void main(String[] args) {
        /*
         * 泛型可以将类型参数化
         * 引入泛型主要是为了程序的安全、可读、适配与易维护
         * 
         * 创建实例的方法:
         * GenClass<T> o = new GenClass<>();
         * 其中T在构造器中称为形式泛型类型，创建实例时用引用类型替代泛型类型，称为泛型实例化
         * 
         * 给类定义泛型类型，泛型类型在类名后
         * 给方法定义泛型类型，泛型类型在方法名和输出类型前
         * 
         * 可以用非受限通配(unbounded wildcard)、受限通配、下限通配为泛型类型指定范围
         * 1. 非受限通配: ?, 相当于? extends Object, 无类型限制
         * 2. 受限通配: ? extends T, 表示T或T的子类
         * 3. 下限通配: ? super T, 表示T或T的父类
         * 
         * 惯例用单个大写字母表示类变量
         * E->element, K->key, V->value, T,U,S->type
         * 
         * 需要注意，若S是T的子类，那么Class<S>不一定是Class<T>的子类
         * 实际上二者甚至可能毫无关系，但二者都是Class的子类
         * 这是为了保证泛型方法不会错误地改变对象中的参数化类型
         */

        // ArrayList就是一个泛型类
        // 钻石运算符可以使用匿名子类(Java 9)
        // 括号内的get扩充了ArrayList中的get方法，将'.'替换为'*'
        ArrayList<String> passwords = new ArrayList<>() {
            public String get(int n) {
                return super.get(n).replaceAll(".", "*");
            }
        };

        // 泛型类型必须是引用类型，不能是基本类型，另见C04
        var intList = new ArrayList<Integer>(); // 允许
        // var intList = new ArrayList<int>(); // 不允许

        // 使用创建的泛型类
        var stack1 = new GenericStack<String>();
        stack1.push("London");
        stack1.push("Paris");
        stack1.push("Berlin");

        var stack2 = new GenericStack<Integer>();
        stack2.push(1);
        stack2.push(2);
        stack2.push(3);

        // 使用创建的泛型方法print
        Integer[] integers = { 1, 2, 3, 4, 5 };
        String[] strings = { "London", "Paris", "New York", "Austin" };
        F01_GenericClass.<Integer>print(integers); // 调用，实际类型作前缀
        print(integers); // 简化调用，编译器自动发现类型
        print(strings);

        // 使用创建的泛型方法sort
        Integer[] intArray = { 2, 4, 3 };
        print(intArray);
        sort(intArray);
        print(intArray);

        // 使用类中返回泛型的方法minmax
        String[] words = { "Mary", "had", "a", "little", "lamb" };
        Pair<String> mm = ArrayAlgo.minmax(words);
        System.out.println("min = " + mm.getFirst());
        System.out.println("max = " + mm.getSecond());

        LocalDate[] birthdays = {
                LocalDate.of(1906, 12, 9),
                LocalDate.of(1815, 12, 10),
                LocalDate.of(1903, 12, 3),
                LocalDate.of(1910, 6, 22),
        };
        Pair<LocalDate> mmDay = ArrayAlgo.minmax(birthdays);
        System.out.println("min = " + mmDay.getFirst());
        System.out.println("max = " + mmDay.getSecond());

        // 使用类中的泛型方法getMiddle
        String mid = ArrayAlgo.<String>getMiddle(words);
        System.out.println("middle = " + mid);

        // 原生类型(raw type)数组内部可能有不同类型的成员，不安全
        GenericStack stack3 = new GenericStack();
        GenericStack<Object> stack4 = new GenericStack<Object>(); // 大体等价

        // 用通配为泛型类型限制范围
        var intStack = new GenericStack<Integer>();
        intStack.push(1);
        intStack.push(2);
        intStack.push(-2);
        System.out.println("The max number is " + max(intStack));
        printStack(intStack); // 栈被清空

        // 栈合并
        var stackObj1 = new GenericStack<Object>();
        combine(stack1, stackObj1);
        combine(stack2, stackObj1);
        printStack(stackObj1);

        // 使用抑制检查异常实现转化为非检查异常
        try {
            // doWork
        } catch (Throwable T) {
            // Task.<RuntimeException>throwAs(e);
        }
    }

    // 定义一个泛型方法，打印一个泛型数组
    // 非受限情况下<E>等同于<E extends Object>
    public static <E> void print(E[] list) {
        for (int i = 0; i < list.length; i++) {
            System.out.print(list[i] + " ");
        }
        System.out.println();
    }

    // 将泛型指定为另一种类型的子类型，称为受限(bounded)泛型
    // 若扩充多个接口，则用&进行分隔
    // 创建一个能排序的泛型方法(冒泡)，可以对有所Comparable实例的数组进行排序
    public static <E extends Comparable<E>> void sort(E[] list) {
        E currentMin; // 用传入的类E定义一个E的实例
        int currentMinIndex;

        for (int i = 0; i < list.length - 1; i++) {
            // 在list[i+1...list.length-2]中找最小值
            currentMin = list[i];
            currentMinIndex = i;

            for (int j = i + 1; j < list.length; j++) {
                // compareTo可以对Integer, Double, Character, String排序
                if (currentMin.compareTo(list[j]) > 0) {
                    currentMin = list[j];
                    currentMinIndex = j;
                }
            }

            // 如果必要的话，调换list[i]与list[currentMinIndex]
            if (currentMinIndex != i) {
                list[currentMinIndex] = list[i];
                list[i] = currentMin;
            }
        }
    }

    // 为泛型类型指定范围的三种方法: 非受限通配、受限通配、下限通配
    // 使用受限通配的数字最大值搜索
    // 注意如果是GenericStack<Number>的话intStack并非是其实例，所以需要通配扩展
    public static double max(GenericStack<? extends Number> stack) {
        double max = stack.pop().doubleValue(); // 初始化为栈末成员

        while (!stack.isEmpty()) {
            double value = stack.pop().doubleValue();
            if (value > max)
                max = value;
        }
        return max;
    }

    // 使用非受限通配的打印并清空栈，顺序为从栈顶到栈底
    public static void printStack(GenericStack<?> stack) {
        while (!stack.isEmpty()) {
            System.out.print(stack.pop() + " ");
        }
        System.out.println();
    }

    // 使用下限通配的栈合并方法，将栈1合并至栈2，也可以直接定义在类中
    public static <T> void combine(GenericStack<T> stack1,
            GenericStack<? super T> stack2) {
        while (!stack1.isEmpty()) {
            stack2.push(stack1.pop());
        }
    }
}

// 定义一个泛型类
class GenericStack<E> {
    private ArrayList<E> list = new ArrayList<>();

    // 如果有构造方法的话，实际上应当是public GenericStack(){}，没有钻石符号

    public int getSize() {
        return list.size();
    }

    public E peak() {
        return list.get(getSize() - 1);
    }

    public void push(E o) {
        list.add(o);
    }

    public E pop() {
        E o = list.get(getSize() - 1);
        list.remove(getSize() - 1);
        return o;
    }

    public boolean isEmpty() {
        return list.isEmpty();
    }

    @Override
    public String toString() {
        return "stack: " + list.toString();
    }
}

class ArrayAlgo { // ArrayAlg在D04中被定义

    @SuppressWarnings("unchecked") // 该语句可以抑制未检查警告
    /**
     * 获取字符串数组中的最大和最小值
     * 
     * @param 字符串数组
     * @return 最大和最小值的Pair对，若null或空则为null
     */
    // public static <T extends Comparable> Pair<T> minmax(T[] a) {}
    // 上面是最初定义的，未使用下限通配，但仅extend Comparable<T>会出现问题
    // 这是因为LocalDate应用了ChronoLocalDate
    // 而ChronoLocalDate扩展了Comparable<ChronoLocalDate>
    // 因此LocalDate扩展了Comparable<ChronoLocalDate>而不是Comparable<LocalDate>
    // 然而使用下限通配就可以解决这个问题
    public static <T extends Comparable<? super T>> Pair<T> minmax(T[] a) {
        if (a == null || a.length == 0)
            return null;
        T min = a[0];
        T max = a[0];
        for (int i = 1; i < a.length; i++) {
            if (min.compareTo(a[i]) > 0)
                min = a[i];
            if (max.compareTo(a[i]) < 0)
                max = a[i];
        }
        return new Pair<>(min, max);
    }

    // 类变量的限制加载修饰符之后，返回类型之前
    // 这里不能用T...代替T[]，防止堆污染(heap pollution)
    public static <T> T getMiddle(T[] a) {
        return a[a.length / 2];
    }

    // 受限泛型的方法
    public static <T extends Comparable<T>> T min(T[] a) {
        if (a == null || a.length == 0)
            return null;
        T smallest = a[0];
        for (int i = 1; i < a.length; i++)
            if (smallest.compareTo(a[i]) > 0)
                smallest = a[i];
        return smallest;
    }
}