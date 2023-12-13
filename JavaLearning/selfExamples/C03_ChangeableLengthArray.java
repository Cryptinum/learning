import java.util.*;

import com.chzhao.javalearning.persons.Employee;

/**
 * Introduce a kind of array that have a changeable length.
 * Generic Array Lists and ArrayList class.
 * 
 * @version 1.0 2023-05-06
 * @author Zhao Chonghao
 */
public class C03_ChangeableLengthArray {
    public static void main(String[] args) {

        // declare and construct an array list in 3 ways
        // ArrayList<Employee> staff = new ArrayList<Employee>();
        // ArrayList<Employee> staff = new ArrayList<>();
        var staff = new ArrayList<Employee>(); // holds no elements yet
        var elements = new ArrayList<>(); // yields an ArrayList<Object>
        var test = new ArrayList<Employee>(100); // 初始化大小
        Employee[] emps = new Employee[100];

        // use .size() to return the 'actual' size
        System.out.println(staff.getClass().getName() + " " + staff.size());
        System.out.println(elements.getClass().getName() + " " + elements.size());
        System.out.println(test.getClass().getName() + " " + test.size());
        System.out.println(emps.getClass().getName() + " " + emps.length);

        // 按当前的元素数量固定array list的大小
        test.trimToSize();
        System.out.println(test.getClass().getName() + " " + test.size());

        // The .add() method creates a bigger array and copies all the
        // objects from the smaller to the bigger array.
        // We can use .ensureCapacity(); to prevent this before a certain value.
        staff.ensureCapacity(100);

        // use add method to add new elements
        staff.add(new Employee(0));
        staff.add(new Employee(1000));

        // allocate a specific length
        staff.ensureCapacity(100);
        System.out.println("Now the size is: " + staff.size());
        for (int i = 2; i < 100; i++)
            staff.add(new Employee(i * 1000));
        System.out.println("Now the size is: " + staff.size()); // 100
        staff.add(new Employee(90909));
        System.out.println("Now the size is: " + staff.size()); // 101
        staff.trimToSize(); // adjust memory size
        System.out.println("Now the size is: " + staff.size()); // 101
        staff.add(new Employee(99999));
        System.out.println("Now the size is: " + staff.size()); // 102

        // get and set the ith element (zero-based)
        // .add() .set() .get() .remove()
        // 对规模太大的array list效率较低，建议使用linked list
        System.out.println(staff.get(50)); // return E.toString()
        staff.add(40, new Employee(114514)); // it will insert
        System.out.println(staff.get(50));
        staff.remove(40); // remove and down the exceeding objs
        System.out.println(staff.get(50));
        staff.set(50, new Employee(114514)); // it also reset ID due to a new obj
        System.out.println(staff.get(50));

        // 对array list里的元素进行遍历，以下两种效果一样，注意第二种需要先获取员工状态
        for (Employee e : staff) {
            e.raiseSalary(5);
        }
        for (int i = 0; i < staff.size(); i++) {
            Employee e = staff.get(i);
            e.raiseSalary(5);
        }
    }
}
