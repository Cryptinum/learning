package com.chzhao.javalearning.cipher;

/**
 * 服务加载器的一个示例
 * 
 * @version 1.0 2023-07-13
 * @author Zhao Chonghao
 */

public interface Cipher {

    byte[] encrypt(byte[] source, byte[] key);

    byte[] decrypt(byte[] source, byte[] key);
    
    int strength();
}
