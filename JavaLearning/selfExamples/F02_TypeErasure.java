import java.io.Serializable;
import java.time.LocalDate;
import java.util.ArrayList;
import com.chzhao.javalearning.*;

/**
 * Type erasure. (类型擦除)
 * 类型擦除与泛型使用过程中的一系列限制
 * 
 * @version 1.01 2023-09-25
 * @author Zhao Chonghao
 */

public class F02_TypeErasure {
    public static void main(String[] args) {
        /*
         * 泛型通过类型擦除(type erasure)实现
         * 
         * 编译器使用泛型类型信息编译代码，但随后会擦除，因此泛型信息在运行时不可用
         * 若编译器确认泛型类型能安全使用，就会将其转换为原生类型
         * 
         * 因此，在使用泛型中存在着一些限制:
         * 1. 不能使用new E()
         * 不能使用泛型类型参数创建实例，如E object = new E();错误
         * 
         * 2. 不能使用new E[]
         * 不能使用泛型类型参数创建数组，如E[] array = new E[max];错误
         * 试图强制转换也不可行，如E[] array = (E[])new Object[max];错误
         * 不能使用泛型类创建泛型数组，如ArrayList<String>[] list = new ArrayList<String>[10];错误
         * 可以先创建通配然后转换，但很不安全，如var table = (Pair<String>[]) new Pair<?>[10];
         * 用ArrayList存储参数化类型对象，如ArrayList<Pair<String>>;
         * 
         * 通过@SafeVarargs或@SuppressWarnings("unchecked")可以抑制错误信息
         * 
         * @SafeVarargs只能用于static, final, private
         * 
         * 3. 含有静态关键词就不能用E o
         * 静态上下文中不允许类的参数是泛型类型，如：
         * 静态方法不能用泛型，public static void m(E o1) {} 错误
         * 静态参数不能用泛型，public static E o1 错误
         * 静态域不能用泛型，static { E o2; } 错误
         * 
         * 4. 异常类不能是泛型
         * 泛型类不能扩展java.lang.Throwable，如：
         * public class MyException<T> extends Exception {} 错误
         * 这是因为若允许，MyException<T>就需要添加catch语句，而JVM需要检查try中的
         * 异常类型是否与指定的类型匹配，但因类型擦除，运行时MyException<T>的类不可获得
         * 
         * 5. if中不能判断实例是否是特定接口或类的泛型
         * if (a instanceof Class<T>)是不被允许的，只能判断if (a instanceof Class)
         * 因此.getClass()也只会返回原始类Class
         * 
         * 6. 需要考虑类型擦除带来的方法名称冲突问题
         * 见Pair.java，equals(T)擦除为equals(Object)，因此Pair<String>将产生冲突
         * 此时只能更改我们定义的方法的名称
         * 类似的，我们不能让同一个类同时继承自同一个接口的不同参数化
         */

        // 以下两种形式对编译器等价
        ArrayList<String> list1 = new ArrayList<>();
        list1.add("Oklahoma");
        String state1 = list1.get(0);

        ArrayList list2 = new ArrayList(); // 这里创建的是ArrayList<Object>
        list2.add("Oklahoma");
        String state2 = (String) (list2.get(0)); // 编译器中强制转换

        // JVM中加载的是原生类型，都是ArrayList
        ArrayList<String> list3 = new ArrayList<>();
        ArrayList<Integer> list4 = new ArrayList<>();
        System.out.println(list3 instanceof ArrayList);
        System.out.println(list4 instanceof ArrayList);

        // 泛型使用中的限制
        // 会提示可能类型转换异常
        ArrayList<String>[] list = (ArrayList<String>[]) new ArrayList[10];
    }

    // 最终被擦除为public static Comparable min(Comparable[] a)，只留下被扩充的接口
    public static <T extends Comparable> T min(T[] a) {
        return a[0];
    }
}

// 最终被擦除为class DateInterval extends Pair
class DateInterval extends Pair<LocalDate> {

    @Override
    // 然而LocalDate被擦除，这里需要擦除为setSecond(Object second)作为桥梁
    // 当编译时，JVM寻找调用方法的变量的类型，若为DateInterval则调用以下方法
    public void setSecond(LocalDate second) {
        if (second.compareTo(getFirst()) >= 0)
            super.setSecond(second);
    }

    @Override
    // 父类中LocalDate被擦除，这里需要擦除为Object getSecond()，这个是父类的方法
    // 但class DateInterval中还有同名方法LocalDate getSecond()
    // 这种称为协变返回类型(covariant return type)
    public LocalDate getSecond() {
        return (LocalDate) super.getSecond();
    }
}

// extend多个接口或类时擦除为第一个
class IntervalTest<T extends Comparable & Serializable> implements Serializable {

    private T lower; // 擦除为private Comparable lower;
    private T upper; // 擦除为private Comparable upper;

    // 擦除为public IntervalTest(Comparable first, Comparable second){...}
    public IntervalTest(T first, T second) {
        if (first.compareTo(second) <= 0) {
            lower = first;
            upper = second;
        } else {
            lower = second;
            upper = first;
        }
    }
}