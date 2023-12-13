
/**
 * Interfaces and callbacks. (接口与回调)
 * 
 * @version 1.0 2023-06-30
 * @author Zhao Chonghao
 */

import java.awt.event.*;
import java.awt.*;
import java.time.*;
import javax.swing.*;

public class D02_Callback {
    public static void main(String[] args) {

        /*
         * 回调(callback)是一种检测特定事件发生时采取行动的方法
         * 我们调用系统的方法叫调用(call)，但当我们写的方法被系统调用时就叫回调
         * 例如当点击某个按钮时程序需要做些什么
         * 
         * javax.swing包中的Timer给出了一个解决方式(因为还没有介绍图形用户界面)
         * 比如我们想做一个时钟程序，间隔一段时间就提醒一次
         * 
         * 我们想要做的：设定时间间隔、每段时间间隔结束后程序需要做什么
         * 一般来说我们需要定义一个函数，然后每隔一段时间调用一次
         * 但是Java有面向对象的解决方案，调用一个对象然后调用对象的方法
         * 
         * 调用的对象需要对ActionListener这个接口进行实现，该接口用于侦听事件
         * ActionListener的实现需要加载java.awt.event包
         * 该接口内只有一个抽象方法actionPerformed，我们需要在类中定义
         * 特别地，我们称这种只有一个抽象方法的接口为函数式接口(functional interface)
         */

        /*
         * 有了回调方法(actionPerformed)之后，我们需要建立包含这个方法的实例
         * 然后把实例转移(pass)给Timer构建Timer的实例
         * 
         * 语法：Timer t = new Timer(int delay, ActionListener listener);
         * 
         * 最后开启计时器，t.start();
         */

        var listener = new TimePrinter();
        Timer timer = new Timer(1000, listener);

        timer.start();

        // 展示一个对话框，保持计时器运行直到用户点击确定
        JOptionPane.showMessageDialog(null, "Quit program?");
        System.exit(0);

    }
}

// 类名不重要，我们的目的是通过类的实例调用里面的方法
class TimePrinter implements ActionListener {

    /*
     * 在时间间隔末尾，定时器调用该方法，此处我们打算实现展示一条信息加播放一个哔声
     * 
     * ActionEvent event 参数传递了事件的信息
     * event.getWhen() 返回事件发生时的时间戳(长整型 单位毫秒)，然后
     * 用Instant.ofEpochMilli() 转换为常用的时间格式
     */
    public void actionPerformed(ActionEvent event) {
        System.out.println("At the tone, the time is " + Instant.ofEpochMilli(event.getWhen()));
        Toolkit.getDefaultToolkit().beep();
    }
}