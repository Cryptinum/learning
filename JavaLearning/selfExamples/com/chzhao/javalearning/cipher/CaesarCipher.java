package com.chzhao.javalearning.cipher;

/*
 * 服务提供者根据Cipher这个服务提供一个或多个类，以下就是其中一个例子
 * 这种基于服务的类可以不与服务在同一个包中，可以在任何包内
 * 实现类需要含有无参构造器
 */
public class CaesarCipher implements Cipher {
    
    public byte[] encrypt(byte[] source, byte[] key) {
        var result = new byte[source.length];
        for (int i = 0; i < source.length; i++)
            result[i] = (byte) (source[i] + key[0]);
        return result;
    }

    public byte[] decrypt(byte[] source, byte[] key) {
        return encrypt(source, new byte[] { (byte) -key[0] });
    }

    public int strength() {
        return 1;
    }
}
