package com.chzhao.javalearning.persons;

import java.util.Objects;

/**
 * An abstract function to include Employee and Student.
 * 
 * @version 1.0 2023-06-28
 * @author Zhao Chonghao
 */

public abstract class Person {

    /*
     * 使用关键词'abstract'可以只定义方法的返回类型、方法名称，而不定义方法主体
     * 包含抽象方法的类必须也被定义为抽象类，正如上面的abstract class Person
     * 值得注意的是，抽象类也可以包含域以及具体方法
     */
    public abstract String getDescription();

    private String name;

    /*
     * 需要注意，抽象类的构造器无法实例化
     * 也就是说，使用Person p = new Person("Name"); 会返回错误，详见主函数
     * 但是如果用抽象类的非抽象子类构造则不会出现问题
     * 比如Person p = new Student("Name", "Major");
     */
    /**
     * An abstract class {@code Person} to include all types of person.
     * 
     * @param name name of the person
     */
    public Person(String name) {
        // deal with null object
        this.name = Objects.requireNonNullElse(name, "unknown");
    }

    /**
     * Return {@code name} of the {@code Person}.
     * 
     * @return Person's name
     */
    public String getName() {
        return name;
    }

    public static void main(String... args) {

        /*
         * 丢出错误：Cannot instantiate the type Person
         * 当类是private/protected/abstract时，实例无法构造
         * 但是可以构造类的向量
         */
        // Person p = new Person("name"); // 不可
        // var ps = new Person[2]; // 可
    }

}
