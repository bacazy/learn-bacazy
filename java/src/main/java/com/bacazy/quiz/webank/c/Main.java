package com.bacazy.quiz.webank.c;

/**
 * 回文串是无论正着读还是反着读都一样的字符串，比如“level”或者“noon”就是回文串。
 * 若将某个十进制非负整数N，转换成二进制后得到的 01 序列具有回文串的性质，则称该数
 * 为回文数，比如十进制非负整数 9 表示成二进制后得到 1001，“1001”具有回文串的性质，
 * 则称十进制整数 9 为回文数。
 * 现给你一个十进制整数N，请计算小于等于N的回文数的数量。
 */

public class Main {
    public static void main(String[] args) {
//        Scanner in = new Scanner(System.in);
//        long N = in.nextLong();
        System.out.println(simpleCount(1 << 2));
        System.out.println(simpleCount(1 << 3));
        System.out.println(simpleCount(1 << 4));
        System.out.println(simpleCount(1 << 5));
        System.out.println(simpleCount(1 << 6));
        System.out.println(simpleCount(1 << 7));
        System.out.println(count((1 << 7) + (1 << 5)));
//        System.out.println(count(N));
    }

    public static long simpleCount(long n) {
        long sum = 0;
        for (long i = 0; i <= n; i++) {
            if (check(i)) {
                sum++;
            }
        }
        return sum;
    }

    private static boolean check(long n) {
        long w = 0, num = n;
        while (num > 0) {
            w++;
            num /= 2;
        }

        for (int i = 0; i < w / 2; i++) {
            long h = (n & (1 << i)) > 0 ? 1 : 0;
            long l = (n & (1 << (w - i - 1))) > 0 ? 1 : 0;
            if (h != l) {
                return false;
            }
        }

        return true;
    }


    private static long count(long n) {
        //先求出最大位数
        int num = 1;
        while ((1 << num) < n) {
            num++;
        }

        //maxW以下位数的个数和
        long low = 0;
        for (int i = 0; i < num; i++) {
            low = low + (1 << ((i - 1) / 2));
        }

        int[] ws = new int[num];
        for (int i = 0; i < num; i++) {
            ws[i] = (n & (1 << i)) > 0 ? 1 : 0;
        }

        int[] hi = new int[num / 2];
        int j = 0;
        for (int i = num - 1; i > num / 2; i--) {
            hi[j] = ws[i];
        }

        int c = 0;
        for (int i = 1; i < hi.length; i++) {
            if (hi[i] > 0) {
                c += (1 << hi.length);
            }
        }


        for (int i = 1 << (num - 1) + 1; i <= n; i++) {
            if (i % 2 != 1) {
                continue;
            }
            if (check(i)) {
                low++;
            }
        }

        return low;
    }
}
