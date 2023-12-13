/**
 * Strings.
 * 
 * @version 1.0 2023-04-22
 * @author Zhao Chonghao
 */

public class A03_Strings {
    public static void main(String[] args) {

        // empty string
        String empty = "";
        System.out.println("->" + empty + "<-");
        System.out.println(empty.length());

        // null string
        String nullString;
        nullString = null;
        System.out.println(nullString == null);

        // substring
        String greeting = "Hello";
        String subGreeting = greeting.substring(0, 3);
        System.out.println(subGreeting); // output "Hel"

        String expletive = "Expletive";
        String PG13 = "deleted";
        String message = expletive + PG13;
        String messageSpace = String.join(" ", expletive, PG13);
        System.out.println(message);
        System.out.println(messageSpace); // use String.join()

        int age = 13;
        String rating = "PG" + age; // auto convert to string
        System.out.println(rating);

        // repeat a string
        String repeated = "Java".repeat(3);
        System.out.println(repeated);

        // Strings are mutable
        String info = "Hello";
        info = info.substring(0, 3) + "p!";
        System.out.println(info);

        System.out.println("Hello".equals(greeting));
        System.out.println("hello".equalsIgnoreCase(greeting));

        // length of string
        String chinese = "𠁼𠁽𠁾𠁿𠂀𠂁𠂂𠂃"; // CJK Ext-B characters
        int n = chinese.length(); // unit length
        int cpCount = chinese.codePointCount(0, chinese.length()); // real length
        System.out.println(n + " " + cpCount);

        // character at str.length() - 1
        String first = Integer.toHexString(chinese.charAt(0));
        String last = Integer.toHexString(chinese.charAt(chinese.length() - 1));
        System.out.println(first + " " + last);

        // get real code point
        int index = chinese.offsetByCodePoints(0, 3);
        int cp = chinese.codePointAt(index);
        System.out.println(index + " " + Integer.toHexString(cp));
        System.out.println(Character.toString(0x5443));

        // strip spaces
        String spaces = " 　    thi s is a tes  t str　ing      　　";
        System.out.println(spaces.stripLeading());
        System.out.println(spaces.stripTrailing());
        System.out.println(spaces.strip());

        // use StringBuilder to save memory
        StringBuilder builder = new StringBuilder();
        builder.append("abc");
        System.out.println(builder);
        builder.append("测试字符串");
        System.out.println(builder);
        builder.setCharAt(5, 'A');
        System.out.println(builder);
        builder.insert(6, "insert");
        System.out.println(builder);
        builder.delete(3, 5);
        System.out.println(builder);
        String completedString = builder.toString(); // after building
        System.out.println(completedString);

        // text block
        String block;
        block = """
                Hello, this is a test programme \
                of String.
                """; // "\" directly connect two lines
        System.out.println(block);

    }
}