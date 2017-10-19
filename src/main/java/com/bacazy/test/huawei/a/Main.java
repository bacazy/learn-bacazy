package com.bacazy.test.huawei.a;


import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int ip = in.nextInt();
        if (ip >= 1 && ip <= 126) {
            print("A");
        } else if (ip >= 128 && ip <= 191) {
            print("B");
        } else if (ip >= 192 && ip <= 223) {
            print("C");
        } else if (ip >= 224 && ip <= 239) {
            print("D");
        } else if (ip >= 240 && ip <= 255) {
            print("E");
        } else if (ip >= 255) {
            print("ERROR");
        }
    }

    private static void print(String str) {
        System.out.println(str);
    }
}
