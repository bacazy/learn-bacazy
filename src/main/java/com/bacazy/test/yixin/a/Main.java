package com.bacazy.test.yixin.a;

import java.util.Scanner;

/**
 * 银行有编号为1到W的W个贷款窗口，且每个窗口都有一个贷款申请人。
 * 现银行提供N种贷款方式供给贷款申请人，每个申请人可以选择其中
 * 一种方式。如果相邻两个窗口的申请人的贷款方式一样，则将可能
 * 产生坏账，求有多少种状态可能产生坏账？
 * <p/>
 * 输入两个整数N，W。其中1<=N<=10^8, 1<=W<10^12
 * <p/>
 * 可能产生坏账的状态数除以100003后取余
 */
public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        long N = in.nextLong();
        long W = in.nextLong();
        System.out.println(badStates(N, W) % 100003);
    }

    private static long badStates(long n, long w) {
        return (pow(n, w) % 100003 - n * pow(n - 1, w - 1) % 100003 + 100003) % 100003;
    }

    private static long pow(long d, long p) {
        long m = 1;
        for (long i = p; i > 0; i--) {
            m = m * d;
        }
        return m;
    }
}
