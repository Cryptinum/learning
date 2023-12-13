import com.chzhao.javalearning.persons.Manager;
import com.chzhao.javalearning.persons.Employee;

/**
 * Example of subclass, defined in the imported package.
 * 
 * @version 1.0 2023-05-04
 * @author Zhao Chonghao
 */

public class C01_Subclass {
    public static void main(String[] args) {

        var staff = new Employee[4];

        // attention: staff[0].getBonus(); will lead to error
        staff[0] = new Manager("Fred Boss", 80000, 1987, 12, 15);
        staff[1] = new Employee("Mark Tester", 50000, 1989, 10, 1);
        staff[2] = new Employee("Simon Tester", 40000, 1990, 3, 15);
        staff[3] = new Manager("Anthony Boss", 85000, 1988, 11, 1);

        for (int i = 0; i < staff.length; i++) {
            // use instanceof to specify whether a instance of a class
            // mainly used when need to apply a subclass method
            if (staff[i] instanceof Manager boss) {
                // Employee class does not have setBonus() method
                // shorten the code and avoid casting, since Java 16
                boss.setBonus(5000);
            }
        }

        for (Employee e : staff) {
            // it will pick correct getSalary method
            // the loop will specify Employee and Manager
            System.out.println(e.getName() + " " + e.getSalary());
        }

        // it's ok to assign a subclass object to a superclass variable
        Employee e;
        e = new Manager();
        System.out.println(e.getSalary());
    }
}
