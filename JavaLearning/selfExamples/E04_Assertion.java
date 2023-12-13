
/**
 * Assertion. (断言)
 * 
 * @version 1.0 2023-07-23
 * @author Zhao Chonghao
 */

import java.nio.charset.StandardCharsets;

public class E04_Assertion {
    public static void main(String[] args) {

        /*
         * 断言(assertion)允许在运行中测试程序并在测试后自动移除
         * 
         * 两种格式：
         * 1. assert condition;
         * 2. assert condition : expression;
         * 均判断了condition，若为false则抛出AssertionError
         * 其中expression部分主要为了显示未通过时的提示文本
         * 
         * 断言功能默认关闭
         * 用-enableassertions或-ea选项开启
         * 用-disableassertions或-da选项关闭
         * java -ea .\selfExamples\E04_Assertion.java
         * 本质上是个类加载器(class loader)
         * 
         * 断言判断失败一般出现在致命的、无法恢复的错误中
         * 断言只在开发测试中开启，产品下线时则关闭，只用于测试程序错误
         */

        String hint = new String("这不是非负罢".getBytes(), StandardCharsets.UTF_8);
        double x = -1;

        // 一个标准的断言
        assert x >= 0 : hint;

        // 也可以通过用一个静态变量控制
        if (asserts)
            assert x >= 0 : hint;
    }

    // 在产品下线时重新编译为false
    public static final boolean asserts = true;
}
