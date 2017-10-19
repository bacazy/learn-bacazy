package com.bacazy.test.webank.a;


import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        int a = in.nextInt();
        int b = in.nextInt();
        int c = in.nextInt();

        System.out.println(countOne(a, b, c));
    }

    private static int countOne(int a, int b, int c) {
        return 1 + b - c;
    }
}
