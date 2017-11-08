package com.bacazy.quiz.newcoder;

/**
 * 一个由小写字母组成的字符串可以看成一些同一字母的最大碎片组成的。
 * 例如,"aaabbaaac"是由下面碎片组成的:'aaa','bb','c'。牛牛现在给定
 * 一个字符串,请你帮助计算这个字符串的所有碎片的平均长度是多少。
 */
public class StringFragement {

    public static void main(String[] args) {
//        Scanner in = new Scanner(System.in);
        System.out.printf("%.2f\n", averageLength("aaabbaaac"));
    }

    private static double averageLength(String str) {
        int total = 0;
        int frag = 1;
        int frag_num = 0;
        char[] chars = str.toCharArray();

        for (int i = 1; i < chars.length; i++) {
            if (chars[i] == chars[i - 1]) {
                frag++;
            } else {
                frag_num++;
                total = total + frag;
                frag = 1;
            }
        }

        total = total + frag;
        frag_num++;
        return 1.0 * total / frag_num;
    }


}
