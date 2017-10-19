package com.bacazy.service.newcoder;

import java.util.Scanner;

/**
 * 魔法王国一共有n个城市,编号为0~n-1号,n个城市之间的道路连接起来恰好构成一棵树。
 * 小易现在在0号城市,每次行动小易会从当前所在的城市走到与其相邻的一个城市,小易最多能行动L次。
 * 如果小易到达过某个城市就视为小易游历过这个城市了,小易现在要制定好的旅游计划使他能游历最多
 * 的城市,请你帮他计算一下他最多能游历过多少个城市(注意0号城市已经游历了,游历过的城市不重复计算)。
 */
public class TravelKindom {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
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
