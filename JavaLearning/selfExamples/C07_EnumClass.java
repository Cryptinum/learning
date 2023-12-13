import java.util.*;

/**
 * Enumeration class. (枚举类)
 * 
 * @version 1.01 2023-07-01
 * @author Zhao Chonghao
 */

public class C07_EnumClass {

    /*
     * 参考在A02中的代码，enumerated类型其实也是一种类，此处的enum类就有四个实例
     * 对enum类中的值进行比较不必使用obj.equals(obj2)，只需使用'=='
     * 这种类不支持构造新object，但是我们可以添加构造器、方法和域
     * 构造器指的是对enum中实例本身进行构造解释
     * 
     * 所有的enumerated类型都是Enum的子类，扩展自Enum<Size>
     * 其中继承了一些函数
     * 如.toString(), Enum.valueOf(Size.class, "SMALL"), .values(), .ordinal()
     */
    public enum Size {
        SMALL("S"),
        MEDIUM("M"),
        LARGE("L"),
        EXTRA_LARGE("XL");

        private String abbreviation;

        // enum的构造器总被自动识别为private，因此也不能标注为public/protected
        Size(String abbreviation) {
            this.abbreviation = abbreviation;
        }

        public String getAbbreviation() {
            return abbreviation;
        }
    }

    public static void main(String... args) {

        try (var in = new Scanner(System.in)) {
            System.out.print("Enter a size: (SMALL, MEDIUM, LARGE, EXTRA_LARGE) ");
            String input = in.next().toUpperCase();
            // 将size设置为输入的值
            Size size = Enum.valueOf(Size.class, input);

            System.out.println("size=" + size);
            System.out.println("abbreviation=" + size.getAbbreviation());
            if (size == Size.EXTRA_LARGE) {
                System.out.println("Good job-- you paid attention to the '_'!");
            }
        } catch (IllegalArgumentException e) {
            System.out.println("Illegal size :(");
        }

        // 遍历输出所有Size，先把值存储进一个array然后再分别toString输出值
        // .ordinal()可以输出其指标
        Size[] values = Size.values();
        System.out.print("All of the sizes are: " + Arrays.toString(values));
    }
}
