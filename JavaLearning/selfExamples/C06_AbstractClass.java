import com.chzhao.javalearning.persons.Employee;
import com.chzhao.javalearning.persons.Student;
import com.chzhao.javalearning.persons.Person;

/**
 * Abstract class. (抽象类)
 * 
 * @version 1.0 2023-06-28
 * @author Zhao Chonghao
 */

public class C06_AbstractClass {
    public static void main(String... args) {

        // 考虑对Employee类进行向上拓展，拓展为Person类，并新建并列类Student

        var people = new Person[2];
        people[0] = new Employee();
        people[1] = new Student();

        for (Person p : people) {
            System.out.println(p.getDescription());
        }
    }
}
