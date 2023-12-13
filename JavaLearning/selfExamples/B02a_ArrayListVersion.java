import java.util.*;

import com.chzhao.javalearning.persons.Employee;

import static java.lang.System.*;

/**
 * Define own classes, written in ArrayList.
 * 
 * @version 1.0 2023-05-06
 * @author Zhao Chonghao
 */
public class B02a_ArrayListVersion {

    public static void main(String[] args) {

        // Employee[] staff = new Employee[3];

        // staff[0] = new Employee("Carl Cracker", 75000, 1987, 12, 15);
        // staff[1] = new Employee("Harry Hacker", 50000, 1989, 10, 1);
        // staff[2] = new Employee("Tony Tester", 40000, 1990, 3, 15);

        // ArrayList is a generic class with a type parameter
        // which can automatically adjusts its capacity.
        var staff = new ArrayList<Employee>();
        staff.add(new Employee("Carl Cracker", 75000, 1987, 12, 15));
        staff.add(new Employee("Harry Hacker", 50000, 1989, 10, 1));
        staff.add(new Employee("Tony Tester", 40000, 1990, 3, 15));

        // raise everyone's salary by 5%
        for (Employee e : staff)
            e.raiseSalary(5);

        // print out info about all Employee objs.
        for (Employee e : staff)
            out.println("name=" + e.getName() + ",salary=" + e.getSalary() + ",hireDay=" + e.getHireDay());
    }
}