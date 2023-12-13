import com.chzhao.javalearning.persons.Employee;
import com.chzhao.javalearning.persons.Manager;

import java.util.*;

/**
 * Interface. (接口)
 * 
 * @version 1.0 2023-06-29
 * @author Zhao Chonghao
 */

public class D01_Interface {

    public static void main(String[] args) {

        /*
         * 接口(interface)是一种描述类"需要"做什么而无需描述"如何"做的方法
         * 一个类可以实现(implement)一个或多个接口，这是相比由抽象类进行继承
         * 的一个最明显的优势，类似C++的multiple inheritance
         * 
         * 所有接口中的方法都是自动被识别为public的，因此无需添加该关键词
         * 但添加也是格式合法的，可以是为了清晰或习惯，Java官方建议省略
         * 接口没有实例域，但接口可以添加常数，详见后文
         * Java 8以后接口可以添加实方法
         * Java 9以后接口的方法可以是private的
         * 
         * 接口不是类，因此不能用new来新建接口的实例，但可以直接声明
         * 错误：x = new Comparable();
         * 允许：Comparable x; x = new Employee(); (若Employee应用了Comparable)
         * 
         * 记录类(Record)和枚举类(Enum)不能继承但是可以应用接口
         * 接口可以是密封的
         */

        /*
         * 考虑我们想对Arrays类的一组Employee实例用一个sort方法进行排序
         * 且Employee需要应用Comparable接口，我们需要做以下两点：
         * 1. 声明类使用接口：class XX implements XX
         * 2. 使用接口中的所有方法：public int compareTo(T o);
         * 
         * 具体见Employee.java
         * 
         * 接口的意义在于Java是一个强类型语言，对一个类的实例，如果类没有
         * compareTo这个方法，实例就无法对这个方法进行应用，因此需要明确
         * 实例确实是一种Comparable的对象
         */

        /*
         * 最后一部分介绍Comparator和Clonable接口
         */

        // 通过直接声明来间接建立一个使用接口的类的实例
        Comparable testE;
        testE = new Employee();

        var staff = new Employee[3];
        staff[0] = new Employee(35000);
        staff[1] = new Employee(75000);
        staff[2] = new Employee(38000);

        // 若小于则输出-1，若大于则输出1，若等于则输出0
        System.out.println(staff[0].compareTo(staff[1]));
        // 如果两个实例为不同的类，那么将不满足compareTo的交换律
        try {
            System.out.println(staff[0].compareTo(new Manager(50000)));
        } catch (ClassCastException e) {
            System.out.println("These two instances cannot be compared!");
        }

        // 使用Arrays.sort()必须保证数组里的所有元素都是Comparable的
        Arrays.sort(staff);
        for (Employee e : staff) {
            System.out.println(e.getSalary());
        }

        // 用instanceof查看对象是否是应用了某个接口的类的实例
        if (staff[0] instanceof Comparable) {
            System.out.println("Congrats! staff[0] is an instance of Comparable!");
        }

        // 使用Comparator接口实现长度比较
        String[] words = { "Long", "Longer" };
        var comp = new LengthComparator();
        if (comp.compare(words[0], words[1]) > 0) {
            System.out.printf("Word '%s' is longer than '%s'!\n", words[0], words[1]);
        } else {
            System.out.printf("Word '%s' is shorter than '%s'!\n", words[0], words[1]);
        }

        // Arrays.sort可以自定义排序方法
        String[] friends = { "Peter", "Paul", "Mary" };
        System.out.println(Arrays.toString(friends));
        Arrays.sort(friends, new LengthComparator());
        System.out.println(Arrays.toString(friends));

        /*
         * Java里不定义指针，但处处都是指针，因此需要明确复制到底是'引用'还是'创建副本'
         * 引用使得两个不同名称的对象指向同一个内存
         * 创建副本使两个不同名称的对象有同样的内容，但指向不同的内存
         * 
         * 然而Object中的.clone()方法受保护，不能直接cast为Employee
         * 用户需要应用Cloneable接口然后重新定义public的clone方法
         * 
         * 除非需要否则不必使用该方法，见Core Java 1 Page 482
         */
        var original = new Employee();
        Employee copy = original;
        System.out.println(original == copy); // 判断内存是否相等
        // Employee copy = original.clone();
    }
}

/*
 * 一个接口的例子，这里compareTo是一个抽象方法
 * 所有应用Comparable1接口的类必须有compareTo这个方法，且参数也需要一致
 * 除非应用这个接口的类也是抽象类
 * 
 * 所有接口中的方法都是public的，因此无需添加该关键词
 */
interface Comparable1 {
    int compareTo(Object other);
}

/*
 * 上面的例子也可以长这样，此处应用Comparable2<Employee>的类
 * 必须有int compareTo(Employee other)这个方法
 * T代表了一种抽象的类，应用接口时在此处填写类名
 */
interface Comparable2<T> {
    // int compareTo(T o);

    /*
     * 可以在接口中设置默认方法，此处的方法默认两个对象都是全等的
     * 由于一般来说使用接口的类都会重载方法，这种默认方法一般不太常用且有些过时
     * 
     * 默认方法的最大意义在于在接口随版本更新扩充时，默认方法可以使
     * 实现接口的所有类无需重新部署或定义新扩充进接口的方法，实现向上兼容
     */
    default int compareTo(T o) {
        return 0;
    }
}

/*
 * 接口不是类，但接口也可以继承，可以说是从高程度的普遍性到高程度的特殊性
 * 尽管不能在接口中放置实例域，但是可以添加常数，该常数被自动识别为public static final
 */
interface Moveable {
    void move(double x, double y);
}

interface Powered extends Moveable {
    double milesPerGallon();

    double SPEED_LIMIT = 95; // 自动为public static final
}

/*
 * 一个类可以应用多个接口
 * 注意到其中Cloneable是一个空接口，空接口的意义在于一是进行标记
 * 二是在于由于public static final等都是自动声明的，因此可以简化代码编写
 */
class Test implements Cloneable, Comparable<Test> {
    public int compareTo(Test o) {
        return 0;
    }
}

/*
 * 接口的方法可能存在冲突问题
 * 
 * 1. 对一个父类，其子类从父类继承的方法与子类应用的接口的方法有相同名称
 * Java默认：优先使用从父类继承的方法(类优先原则)
 * 
 * 2. 对一个类，其应用的多个接口存在相同名称的方法
 * Java默认：报错，用户必须在类中重载方法并手动定义
 * 
 * 第一个问题不存在歧义，下面针对第二个问题进行解决
 * Person和Named中含有同名方法，考虑一个名为Student的类同时应用了两个方法
 * Java会自动报错，并提示编写者重新在类中定义该名称冲突的函数
 * 
 * 需要注意的是，如果一个是实默认函数，另一个是抽象函数，Java仍会报错
 */
interface PersonD01 {
    default String getName() {
        return "";
    }
}

interface NamedD01 {
    default String getName() {
        return getClass().getName() + "_" + hashCode();
    }
}

class StudentD01 implements PersonD01, NamedD01 {
    public String getName() {
        return PersonD01.super.getName();
    }
}

/*
 * String类中的compareTo是根据字典顺序排序的，假设我们想根据字符串长度排序
 * 然而我们无法再改动String.compareTo()方法
 * 
 * 但是可以用Arrays.sort来排序，使用实例化Comparator接口的方法
 */
class LengthComparator implements Comparator<String> {
    public int compare(String first, String second) {
        return first.length() - second.length();
    }
}