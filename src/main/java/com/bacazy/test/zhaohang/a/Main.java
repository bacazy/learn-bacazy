package com.bacazy.test.zhaohang.a;

import java.util.Scanner;

/**
 *
 */
public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int N = in.nextInt();
        int M = in.nextInt();
        int K = in.nextInt();
        System.out.println(toys(N, M, K));
    }

    private static int toys(int n, int m, int k) {
        if (k < 1 || k > n) {
            return 0;
        }

        int i = 0;
        for (i = 1; i < m; i++) {
            if (!accepted(n, m, k, i)) {
                break;
            }
        }

        return i - 1;
    }

    private static boolean accepted(int n, int m, int k, int i) {
        m = m - i;
        if (m < 0) {
            return false;
        }
        int t = i - 1;
        for (int j = k - 1; j > 1; j--) {
            if (t > 0) {
                m = m - t;
                t--;
            }
        }
        int p = i - 1;
        for (int j = k + 1; j < n + 1; j++) {
            if (t > 0) {
                m = m - p;
                p--;
            }
        }

        return m >= 0;
    }


}
