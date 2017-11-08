package com.bacazy.quiz.aiqiyi.a;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int[] array = new int[n];
        for (int i = 0; i < n; i++) {
            array[i] = in.nextInt();
        }
        System.out.println(digitGame(array));
    }

    private static int digitGame(int[] array) {
        int max = 0;
        for (int num : array) {
            int d = convert(num);
            if (d > max) {
                max = d;
            }
        }
        return max;
    }

    private static int convert(int num) {
        int value = 0;
        ArrayList<Integer> digits = new ArrayList<Integer>();
        while (num != 0) {
            digits.add(num % 10);
            num = num / 10;
        }
        Collections.sort(digits);
        for (int i : digits) {
            value = value * 10 + i;
        }
        return value;
    }
}
