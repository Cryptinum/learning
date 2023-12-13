package com.chzhao.javalearning.persons;

import java.time.*;
import java.util.*;

/**
 * A class stores basic information of employees.
 * 
 * @version 1.12 2023-06-30
 * @author Zhao Chonghao
 */

public class Employee extends Person implements Comparable<Employee> {

    // instance fields
    private static int nextId;

    private int id;
    private double salary;
    private LocalDate hireDay;

    private static Random generator = new Random();

    // static initialization block
    static {
        // set nextId to a random number between 0 and 9999
        nextId = generator.nextInt(10000);
    }

    // object initialization block
    {
        id = nextId;
        nextId++;
    }

    /**
     * Construct an {@code Employee} object.
     * 
     * @param name   Name of the employee.
     * @param salary Salary of the employee.
     * @param year   Hire year.
     * @param month  Hire month.
     * @param day    Hire day.
     */
    public Employee(String name, double salary, int year, int month, int day) {
        // extend by super(name);
        super(name);
        this.salary = salary;
        this.hireDay = LocalDate.of(year, month, day);
    }

    /**
     * Construct an employee with only name and salary.
     * 
     * @param name   Name of the employee.
     * @param salary Salary of the employee.
     */
    public Employee(String name, double salary) {
        this(name, salary, 1900, 1, 1);
    }

    /**
     * Construct an employee with only salary.
     * 
     * @param salary Salary of the employee.
     */
    public Employee(double salary) {
        this("Default Employee #" + nextId, salary);
    }

    /**
     * Construct a default Employee.
     */
    public Employee() {
        this(-99999.9);
    }

    /**
     * Get salary of the employee.
     */
    public double getSalary() {
        return this.salary;
    }

    /**
     * Get hire day of the employee.
     */
    public LocalDate getHireDay() {
        return this.hireDay;
    }

    /**
     * Get random id of the employee.
     */
    public int getId() {
        return this.id;
    }

    /**
     * Get description of an employee.
     */
    public String getDescription() {
        return "Employee's description: " + "[name=" + super.getName() + ",salary="
                + this.salary + ",hireDay=" + this.hireDay + "]";
    }

    /**
     * Raise {@code salary} by percent of input.
     * 
     * @param byPercent Percentage of salary.
     */
    public void raiseSalary(double byPercent) {
        double raise = this.salary * byPercent / 100;
        this.salary += raise;
    }

    /**
     * Compares employees by salary.
     * 
     * @param other another Employee object
     * @return a negative value if this employee has a lower salary than
     *         otherObject, 0 if the salaries are the same, a positive value
     *         otherwise
     */
    public int compareTo(Employee other) {
        if (this.getClass() != other.getClass())
            throw new ClassCastException();
        else
            return Double.compare(salary, other.salary);
    }

    /**
     * Check the equality of two Employees, including Managers.
     * 
     * @return true if {@code name}, {@code salary} and {@code hireDate} are
     *         identical.
     */
    /*
     * Steps for writing a perfect 'equals()' method
     * 1. name te explicit parameter 'otherObject' to override the
     * equals() method in Object class
     * 2. check 'this == otherObject'
     * 3. check 'otherObject == null'
     * 4. check 'this.getClass() != otherObject.getClass()'
     * 5. cast 'ClassName other = (ClassName) otherObject'
     * 6. compare fields
     */
    @Override
    public boolean equals(Object otherObject) {
        // a quick test to check identicality
        if (this == otherObject)
            return true;
        // if explicit parameter is null, return false
        if (otherObject == null)
            return false;
        // if classes don't match, return false
        if (this.getClass() != otherObject.getClass())
            return false;
        // for a non-null Employee, check fields
        Employee other = (Employee) otherObject;
        return Objects.equals(super.getName(), other.getName()) && this.salary == other.salary
                && Objects.equals(this.hireDay, other.hireDay);
    }

    /**
     * Get hash of an Employee object.
     * 
     * @return hash code
     */
    @Override
    public int hashCode() {
        // return 7 * name.hashCode() + 11 * Double.valueOf(salary).hashCode() + 13 *
        // hireDay.hashCode();
        // return 7 * Objects.hashCode(name) + 11 * Double.hashCode(salary) + 13 *
        // Objects.hashCode(hireDay);
        return Objects.hash(super.getName(), this.salary, this.hireDay);
    }

    /**
     * Get basic information of an Employee object.
     * 
     * @return information
     */
    // better to add toString() method to each class for logging support
    @Override
    public String toString() {
        return getClass().getName() + "[name=" + super.getName() + ",salary=" + this.salary + ",hireDay=" + this.hireDay
                + "]";
    }

    // unit test
    // we can see the demo by calling java Employee
    public static void main(String[] args) {
        // var staff = new Employee[4];
        // staff[0] = new Employee("First Employee", 20000, 1989, 6, 4);
        // staff[1] = new Employee("Second Employee", 30000);
        // staff[2] = new Employee(40000);
        // staff[3] = new Employee();

        var staff = new ArrayList<Employee>();
        staff.add(new Employee("First Employee", 20000, 1989, 6, 4));
        staff.add(new Employee("Second Employee", 30000));
        staff.add(new Employee(40000));
        staff.add(new Employee());

        // staff[2].raiseSalary(10);
        for (Employee e : staff) {
            e.raiseSalary(10);
        }

        for (Employee e : staff) {
            System.out.println(e.getName() + " " + e.getId() + " " + e.getSalary() + " " + e.getHireDay());
        }
    }
}
