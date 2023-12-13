/**
 * How command line works.
 * Use java .\A08_HowCommandWorks -h/-g args* to see what happens.
 * e.g. java A08_HowCommandWorks -h Zhao Chonghao
 * 
 * @version 1.0 2023-04-27
 * @author Zhao Chonghao
 */

public class A08_HowCommandWorks {
    public static void main(String[] args) {
        
        if (args.length == 0 || args[0].equals("-h"))
            System.out.print("Hello,");
        else if (args[0].equals("-g"))
            System.out.print("Goodbye,");

        for (int i = 1; i < args.length; i++)
            System.out.print(" " + args[i]);
        System.out.println("!");
    }
}
