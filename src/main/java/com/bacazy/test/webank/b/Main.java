package com.bacazy.test.webank.b;


import java.util.Scanner;

/**
 * 给出一个非负整数 n，我们可以用各种进制来表示它。比如说数 23，它在十进制表示
 * 下就是 23，在二进制表示下是 10111，在八进制表示下是 27，在十二进制表示下 1B(B
 * 表示 11)。 n 在某种进制表示下的权值为将其各位数字相加的和，比如 23 在二进制
 * 表示下的权值为1+0+1+1+1=4，23 在八进制表示下的权值为 2+7=9，23 在十二进制
 * 表示下的权值为1+11=12。
 * <p/>
 * 现在给出一个非负整数n，你可以用p进制去表示它(2 ≤p≤n )，同时你要使得它在这种进
 * 制表示下的权值最大。
 */

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        int a = in.nextInt();
        System.out.println(maxWeight(a));
    }

    private static int maxWeight(int a) {
        int maxW = 0;
        for (int i = 2; i <= a; i++) {
            int weight = weight(a, i);
            if (weight > maxW) {
                maxW = weight;
            }
        }
        return maxW;
    }

    private static int weight(int a, int p) {
        int w = 0;
        while (a > 0) {
            w += a % p;
            a /= p;
        }
        return w;
    }
}
