package com.bacazy.service.leetcode;

/**
 * Given two non-negative integers num1 and num2 represented as
 * strings, return the product of num1 and num2.
 * <p/>
 * Note:
 * <p/>
 * The length of both num1 and num2 is < 110.
 * Both num1 and num2 contains only digits 0-9.
 * Both num1 and num2 does not contain any leading zero.
 * You must not use any built-in BigInteger library or convert the
 * inputs to integer directly..
 */
public class MultiplyStrings {
    public int char2digit(char c) {
        switch (c) {
            case '0':
                return 0;
            case '1':
                return 1;
            case '2':
                return 2;
            case '3':
                return 3;
            case '4':
                return 4;
            case '5':
                return 5;
            case '6':
                return 6;
            case '7':
                return 7;
            case '8':
                return 8;
            case '9':
                return 9;
            default:
                return 0;
        }
    }

    public String multiply(String num1, String num2) {
        StringBuilder builder = new StringBuilder();
        int l1 = num1.length() - 1;
        int l2 = num2.length() - 1;
        int up = 0;
        while (l1 >= 0 || l2 >= 0) {
            int a = 0;
            int b = 0;
            if (l1 >= 0) {
                a = char2digit(num1.charAt(l1));
            }
            if (l2 >= 0) {
                b = char2digit(num2.charAt(l2));
            }
            int sum = up + a * b;
            up = sum / 10;
            builder.append(sum % 10);
            l1--;
            l2--;
        }
        if (up > 0) {
            builder.append(up);
        }
        builder.reverse();
        return builder.toString();
    }
}
