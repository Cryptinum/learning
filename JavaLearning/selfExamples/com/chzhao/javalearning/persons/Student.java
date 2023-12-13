package com.chzhao.javalearning.persons;

/**
 * Extend Person class to Student class.
 * 
 * @version 1.0 2023-06-28
 * @author Zhao Chonghao
 */

/*
 * 对扩展抽象类的子类，子类中必须定义父抽象类中的抽象方法
 * 因此我们在类中需要定义public String getDescription();
 */
public class Student extends Person {

    private String major;

    /**
     * Construct a {@code Student} object.
     * 
     * @param name  Name of the student.
     * @param major Major of the student.
     */
    public Student(String name, String major) {
        super(name);
        this.major = major;
    }

    /**
     * Construct a default {@code Student}.
     */
    public Student() {
        this("DefaultName", "DefaultMajor");
    }

    /**
     * Get description of a student.
     */
    public String getDescription() {
        return "Student " + super.getName() + " majoring in " + major;
    }
}
