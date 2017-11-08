package com.bacazy.quiz.zhaohang.b;

import java.util.Scanner;


public class Main {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int[] counts = new int[3];
        for (int i = 0; i < 3; i++) {
            counts[i] = in.nextInt();
        }

        solution(counts);

    }

    private static void solution(int[] counts) {
        int[] cs = new int[3];
        for (int i = 0; i < counts.length; i++) {
            if (counts[i] == 0) {
                cs[0]++;
            } else if (counts[i] == 1) {
                cs[1]++;
            } else {
                cs[2]++;
            }
        }

        if (counts[1] == 2 && counts[0] == 1) {
            System.out.println(1);
            return;
        }

        if (counts[1] == 1 && counts[2] == 2) {
            System.out.println(1);
            return;
        }
    }
}

