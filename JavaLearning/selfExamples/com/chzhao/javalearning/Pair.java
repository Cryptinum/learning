package com.chzhao.javalearning;

import java.util.function.*;

public class Pair<T> {
    private T first;
    private T second;

    public Pair() {
        first = null;
        second = null;
    }

    public Pair(T first, T second) {
        this.first = first;
        this.second = second;
    }

    public static <T> Pair<T> makePair(Supplier<T> constr) {
        return new Pair<>(constr.get(), constr.get());
    }

    public T getFirst() {
        return first;
    }

    public T getSecond() {
        return second;
    }

    public void setFirst(T newValue) {
        first = newValue;
    }

    public void setSecond(T newValue) {
        second = newValue;
    }

    // 注意由于Object类中有equals()的定义，类擦除时就会产生冲突
    // 因此在方法继承时需要注意名称冲突问题，此时用@Override无法解决，只能改名
    // 此处将equals()改名为pairEquals()
    // Name clash: The method equals(T) of type Pair<T>
    // has the same erasure as equals(Object) of type Object
    // but does not override it [Java(67109424)]
    public boolean pairEquals(T value) {
        return first.equals(value) && second.equals(value);
    }

    public static boolean hasNulls(Pair<?> p) {
        return p.getFirst() == null || p.getSecond() == null;
    }

    // 通过一个中介函数绕过非受限通配无法访问参数内部的弊端
    public static <T> void swapHelper(Pair<T> p) {
        T t = p.getFirst();
        p.setFirst(p.getSecond());
        p.setSecond(t);
    }

    public static void swap(Pair<?> p) {
        swapHelper(p);
    }

    public static void main(String[] args) {

        // 通过makePair方法绕过不能建立泛型实例的限制
        Pair<String> p = Pair.makePair(String::new);
        p.setFirst("First");
        p.setSecond("Second");
        System.out.println(p.getFirst() + ", " + p.getSecond());
    }
}
