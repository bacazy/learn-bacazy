package com.bacazy.test.ify.one;

import java.util.Scanner;

/**
 * 时间限制：C/C++语言 2000MS；其他语言 4000MS
 * 内存限制：C/C++语言 65536KB；其他语言 589824KB
 * 题目描述：
 * 有 n 个人排成了一行队列，每个人都有一个站立的方向：面向左或面向右。由于这 n 个人中每个人都很讨厌其他的人，
 * 所以当两个人面对面站立时，他们会发生争吵，然后其中一个人就会被踢出队列，谁被踢出队列都是有可能的。
 * <p/>
 * 我们用字符 L 来表示一个面向左站立的人，用字符 R 来表示一个面向右站立的人，那么这个队列可以用一个字符串描述。
 * 比如 RLLR 就表示一个四个人的队列，其中第一个人和第二个人是面对面站立的。他们发生争吵后队列可能会变成 LLR，
 * 也可能变成 RLR；若变成 RLR，则第一个人与第二个人还会发生争吵，队列会进一步变成 LR 或者 RR。
 * <p/>
 * 若在某个时刻同时可能有很多的争吵会发生时，接下来只会发生其中的一个，且任意一个都是有可能发生的。
 * <p/>
 * 你想知道经过一系列的争吵后，这个队列最少会剩下多少人？
 */

public class Main {
    private static int count = 0;

    private static int compute(char[] a) {
        count = a.length;

        kick(a.clone(), a.length);

        return count;
    }

    private static void kick(char[] chars, int size) {
        if (size < count) {
            count = size;
        }

        for (int i = 0; i < chars.length - 1; i++) {
            if (chars[i] == 'R' && chars[i + 1] == 'L') {
                char[] cs = new char[chars.length - 1];
                System.arraycopy(chars, 0, cs, 0, i);
                System.arraycopy(chars, i + 1, cs, i, chars.length - 1 - i);
                cs[i] = 'R';
                kick(cs, size - 1);
                char[] csa = cs.clone();
                csa[i] = 'L';
                kick(csa, size - 1);
            }
        }
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        System.out.println(compute(in.nextLine().toCharArray()));
    }
}
