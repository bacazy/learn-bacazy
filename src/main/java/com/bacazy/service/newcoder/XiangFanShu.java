package com.bacazy.service.newcoder;

import java.util.Scanner;
import java.util.Stack;

/**
 * 为了得到一个数的"相反数",我们将这个数的数字顺序颠倒,然后再加上原先的数得到
 * "相反数"。例如,为了得到1325的"相反数",首先我们将该数的数字顺序颠倒,我们得
 * 到5231,之后再加上原先的数,我们得到5231+1325=6556.如果颠倒之后的数字有前
 * 缀零,前缀零将会被忽略。例如n = 100, 颠倒之后是1.
 */

public class XiangFanShu {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        System.out.println(n + reverse(n));
    }

    static int reverse(int n) {
        Stack<Integer> ws = new Stack<Integer>();
        while (n > 0) {
            ws.push(n % 10);
            n = n / 10;
        }

        int r = 0;
        int p = 1;
        while (!ws.empty()) {
            r = r + p * ws.pop();
            p = p * 10;
        }

        return r;
    }
}
