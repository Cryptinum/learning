/**
 * Sealed class. (密封类)
 * Since Java 17.
 * 
 * @version 1.0 2023-06-28
 * @author Zhao Chonghao
 */

public class C08_SealedClass {
    public static void main(String... args) {

        /*
         * 密封类控制哪些子类可以从父类中继承
         * 
         * 例如我们public abstract sealed class JSONValue permits
         * JSONArray, JSONNumber, JSONString, ...
         * 那么我们就无法进行
         * public class JSONComment extends JSONValue {...}
         * 
         * 如果不加permits关键词，那么其所有的子类都必须定义在同一个文件中
         * 
         * 暂时搁置，见Core Java 1 Page 404
         */
    }

}