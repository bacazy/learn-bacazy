package com.bacazy.service.newcoder;

import java.util.Scanner;


public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        System.out.println(length(in.nextLine().trim()));
    }

    static int length(String str) {
        int maxL = 1;
        int l = 1;
        for (int i = 1; i < str.length(); i++) {
            if (str.charAt(i) == str.charAt(i - 1)) {
                l = 1;
            } else {
                l++;
                if (l > maxL) {
                    maxL = l;
                }
            }
        }

        return maxL;
    }
}
