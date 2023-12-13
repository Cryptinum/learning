
/**
 * Service loader. (服务加载器)
 * 
 * @version 1.0 2023-07-13
 * @author Zhao Chonghao
 */

import com.chzhao.javalearning.cipher.*;

import java.io.*;
import java.nio.charset.StandardCharsets;
import java.util.*;

public class D05_ServiceLoader {

    // 初始化一个服务加载器
    public static ServiceLoader<Cipher> cipherLoader = ServiceLoader.load(Cipher.class);

    public static void main(String[] args) throws UnsupportedEncodingException {

        /*
         * 有时我们会基于服务框架开发应用，例如OSGi (http://osgi.org)
         * 
         * JDK提供了加载服务的简单方法，具体见Core Java 2 Chapter 9
         * 服务加载器给了开发者基于服务接口进行开发的方法
         * 
         * 实现类需要含有无参构造器
         */

        Cipher cipher = getCipher(1);
        String message = "Meet me at the toga party.";
        byte[] bytes = cipher.encrypt(message.getBytes(), new byte[] { 3 });
        var encrypted = new String(bytes, StandardCharsets.UTF_8);
        System.out.println(encrypted);

    }

    public static Cipher getCipher(int minStrength) {
        // 隐式调用一个迭代器(Iterator)：cipherLoader.iterator()遍历所有提供的解码服务
        // 具体见Core Java 1 Chapter 9
        for (Cipher cipher : cipherLoader)
            if (cipher.strength() >= minStrength)
                return cipher;
        return null;
    }

    // 用stream处理，具体见Core Java 2 Chapter 1
    // 这种情况下用Optional<Cipher> cipher = cipherLoader.findFirst(); 构建服务实例
    public static Optional<Cipher> getCipher2(int minStrength) {
        return cipherLoader.stream()
                .filter(descr -> descr.type() == CaesarCipher.class)
                .findFirst()
                .map(ServiceLoader.Provider::get);
    }
}
