import java.util.*;

/**
 * Introduce wrappers.
 * 
 * @version 1.0 2023-06-28
 * @author Zhao Chonghao
 */

public class C04_ObjectWrappers {
    public static void main(String[] args) {

        // 有时候我们需要把基本类型转换为object
        // 对应的类型有Integer, Long, Float, Double, Short, Byte, Character, Boolean
        // 前六个继承自Number, 这八个都是immutable且final的

        // 比如我们想要一个整型的array list，但是<>里不能是基本类型
        // 我们可以用wrappers替代
        var list = new ArrayList<Integer>();
        // 这种定义比 int[] list = new int[] {}; 低效

        // 同样用.add()添加元素
        // 这与list.add(Integer.valueOf(3)); 效果相同
        // 这种转换称为auto-boxing
        list.add(3);

        // 同样用.get()获取元素
        // 这与int n = list.get(0).intValue(); 效果相同
        // 这种转换称为auto-unboxing
        int n = list.get(0);
        System.out.println("The number is " + n + ".");

        // 这也是一种auto-unboxing
        // 省去了int aa = a.intValue(); 的步骤
        Integer a = 3;
        System.out.println("The number is " + a + ".");
        a++;
        System.out.println("The number is " + a + ".");

        // 但需要注意包装类与原始类并不完全等同
        // 由于在判断'=='时只会判断内存是否一致
        // 然而如果包装类的值在-128~127之间，进行比较仍会输出true
        // 因此！！！不要用'=='判断包装类的相等，而用obj.equals(obj2)
        // 另外！！！不要用包装类构造器例如new Integer(0);
        Integer x = 1000;
        Integer y = 1000;
        int z = 1000;
        System.out.println(x); // 自动调用.toString()
        System.out.println(x == y);
        System.out.println(x == z); // int和Integer比较会自动unboxing并比较值
        System.out.println(x.intValue() == y.intValue());
        System.out.println(x.equals(y)); // 用obj.equals(obj2)可以比较值

        // 比较微妙的一点，此处在条件语句中Integer被unboxed并转换为double
        // 然后被autoboxed为Double
        Integer i = 1;
        Double d = 2.0;
        System.out.println(true ? i : d); // 输出1.0

        // 包装类在转换字符串为数字时比较简便
        int sInt=Integer.parseInt("AAAA", 16);
        System.out.println(sInt);
    }
}
