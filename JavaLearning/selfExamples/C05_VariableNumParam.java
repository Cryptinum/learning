import java.util.*;

/**
 * 变量数量可变的函数
 * 
 * @version 1.0 2023-06-28
 * @author Zhao Chonghao
 */

public class C05_VariableNumParam {
    public static void main(String[] args) {

        // 以System.out.printf()为例，其中用到了'...'作为函数的一部分
        // 实际上里面的Object...就等同于Object[]
        double dx = 1.0;
        int ix = 2;
        System.out.printf("%f %d\n", dx, ix);
        System.out.printf("%f %s\n",
                new Object[] { Double.valueOf(100), "test string" });

        // 可以自定义变量数量可变的函数
        double[] doubles = new double[10];
        Random rd = new Random();
        
        for (int i = 0; i < doubles.length; i++) {
            doubles[i] = rd.nextDouble(1, 100);
            System.out.printf("%.2f ", doubles[i]);
        }
        System.out.printf("max=%.2f", max(doubles));
    }

    public static double max(double... values) {
        double largest = Double.NEGATIVE_INFINITY;
        for (double v : values)
            if (v > largest)
                largest = v;
        return largest;
    }
}
