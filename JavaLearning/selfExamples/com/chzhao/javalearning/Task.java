package com.chzhao.javalearning;

/**
 * 将检查异常转换为未检查异常，配合F01_GenericClass.java
 */

interface Task {
    void run() throws Exception;

    // 一般来说，Java异常处理需要为所有检查异常提供处理的句柄
    // 但使用以下方法可以避开这个问题
    // 假设有一个接口Task，一个检查异常e，那么Task.<RuntimeException>throwAs(e);
    // 就会将该异常处理为非检查异常，具体见main
    @SuppressWarnings("unchecked")
    static <T extends Throwable> void throwAs(Throwable t) throws T {
        throw (T) t;
    }

    static Runnable asRunnable(Task task) {
        return () -> {
            try {
                task.run();
            } catch (Exception e) {
                Task.<RuntimeException>throwAs(e);
            }
        };
    }

    public static void main(String[] args) {
        var thread = new Thread(Task.asRunnable(() -> {
            Thread.sleep(1000);
            System.out.println("Hello, world!");
            throw new Exception("Check this out!");
        }));
        thread.start();
    }
}