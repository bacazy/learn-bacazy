package com.bacazy.test.tencent.q2;

/**
 * 有四个数a,b,A,B,有两种变换方式
 * 1. a=a+1,b=b+1
 * 2. a=2*a,b=2*b
 * 问是否可以将a,b变换成A,B,若可以则输出最少变换次数，若不可以则输出-1
 */
public class Pay {
    private int min = -1;

    public int cal(int a, int b, int A, int B) {
        System.out.printf("%d,%d,%d,%d\n", a, b, A, B);
        cal(a, b, A, B, 0);
        return min;
    }

    private void cal(int a, int b, int A, int B, int depth) {
//
        if (A == a && b == B) {
            if (min == -1) {
                min = depth;
            } else {
                if (min > depth) {
                    min = depth;
                }
            }
        }
        if (a < A && b < B) {
            cal(2 * a, 2 * b, A, B, depth + 1);
            cal(1 + a, 1 + b, A, B, depth + 1);
        }
    }
}
