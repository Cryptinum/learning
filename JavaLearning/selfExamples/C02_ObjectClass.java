import com.chzhao.javalearning.persons.Manager;
import com.chzhao.javalearning.persons.Employee;

/**
 * The most general class - Object.
 * Introduce Object class method override, hashCode and toString method.
 * 
 * @version 1.0 2023-05-05
 * @author Zhao Chonghao
 */

public class C02_ObjectClass {
    public static void main(String[] args) {

        // use a variable of type Object to refer any type of objects
        Object obj1 = new Employee();
        System.out.println(obj1.getClass());

        // but need to be casted for accessing specific methods.
        Employee e = (Employee) obj1;
        System.out.println(e.getSalary());

        // all array types are extended Object
        Object obj2;
        Employee[] staff = new Employee[10];
        obj2 = staff;
        System.out.println(obj2.getClass());
        obj2 = new int[10];
        System.out.println(obj2.getClass());

        // hashCode method
        String[] str = { "Hello", "Harry", "Hacker" };
        for (String s : str) {
            System.out.print(s.hashCode() + " ");
        }

        System.out.println("\n" + e.hashCode());

        // toString method
        Manager m = new Manager();
        System.out.println(m.toString());
    }
}
