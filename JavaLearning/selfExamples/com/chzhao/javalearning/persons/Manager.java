package com.chzhao.javalearning.persons;

import java.util.*;

/**
 * A specific type of employee - manager.
 * 
 * @version 1.1 2023-06-30
 * @author Zhao Chonghao
 */

/*
 * In this situation, class Employee called superclass/parent class
 * and class Manager called subclass/child class
 * Subclass is the refinement of superclass.
 * 
 * If we use public 'final' class, it means this class cannot be extended
 * Similarly, public 'final' method cannot be overrode
 * Particularly, all methods in a final class are automatically final as well
 * but the fields will not
 */
public class Manager extends Employee {

    private double bonus;

    /**
     * Construct an {@code Manager} object inherit from {@code Employee}.
     * 
     * @param name   Name of the manager.
     * @param salary Salary of the manager.
     * @param year   Hire year.
     * @param month  Hire month.
     * @param day    Hire day.
     */
    public Manager(String name, double salary, int year, int month, int day) {
        // user super() to call superclass constructor.
        super(name, salary, year, month, day);
        bonus = 0;
    }

    /**
     * Construct a manager with only salary.
     * 
     * @param salary Salary of the manager.
     */
    public Manager(double salary) {
        super(salary);
    }

    /**
     * Construct a default manager.
     */
    public Manager() {
        super(-99999.9);
    }

    /**
     * Set the bonus of a manager.
     * 
     * @param bonus manager"s bonus
     */
    public void setBonus(double bonus) {
        this.bonus = bonus;
    }

    /**
     * Get the bonus of a manager.
     * 
     * @return bonus of the manager.
     */
    public double getBonus() {
        return this.bonus;
    }

    /**
     * Get the total salary of a manager.
     * 
     * @return base salary + bonus
     */
    @Override
    public double getSalary() {
        // overrides the getSalary() method in Employee class
        // use keyword 'super' to access getSalary() method in Employee class
        double baseSalary = super.getSalary();
        return baseSalary + bonus;
    }

    /**
     * Check the equality of two Managers.
     * 
     * @return true if {@code name}, {@code salary}, {@code hireDate}
     *         and {@code bonus} are identical.
     */
    @Override
    public boolean equals(Object otherObject) {
        // check whether this and otherObject belong to the same class
        if (!super.equals(otherObject))
            return false;
        // then check the fields
        Manager other = (Manager) otherObject;
        return this.bonus == other.bonus;
    }

    /**
     * Get hash of a Manager object.
     * 
     * @return hash code
     */
    @Override
    public int hashCode() {
        return Objects.hash(super.hashCode(), bonus);
    }

    /**
     * Get basic information of an Manager object.
     * 
     * @return information
     */
    @Override
    public String toString() {
        return super.toString() + "[bonus=" + bonus + "]";
    }
}
