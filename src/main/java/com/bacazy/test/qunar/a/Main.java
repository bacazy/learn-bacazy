package com.bacazy.test.qunar.a;


import java.util.Scanner;

public class Main {
    private static final int[] V = new
            int[]{1, 5, 10, 50, 100, 500};

    static int min = -1;

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int[] count = new int[6];
        for (int i = 0; i < 6; i++) {
            count[i] = in.nextInt();
        }
        int price = in.nextInt();
        int result = compute(count, price);
        if (result <= 0) {
            System.out.println("NOWAY");
        } else {
            System.out.println(result);
        }

    }

    private static int compute(int[] count, int price) {
        int[] selected = new int[6];
        int n = 5;

        while (count[n] <= 0) {
            n--;
        }


        int c = select(count, price, selected, n);

        return c;
    }

    private static int select(int[] count, int price, int[] selected, int n) {
        if (price == 0) {
            if (min < 0) {
                min = countIt(selected);
            } else {
                int c = countIt(selected);
                if (c < min) {
                    min = c;
                }
            }
            return min;
        }

        if (countIt(count) == 0) {
            return min;
        }


        if ((count[n] <= 0 || price < V[n]) && n > 0) {
            select(count, price, selected, n - 1);
        } else {
            selected[n] = selected[n] + 1;
            price = price - V[n];
            count[n] = count[n] - 1;
            select(count, price, selected, n);
            if (n > 0) {
                selected[n] = selected[n] - 1;
                price = price + V[n];
                count[n] = count[n] + 1;
                select(count, price, selected, n - 1);
            }
        }
        return min;
    }

    private static int countIt(int[] count) {
        int sum = 0;
        for (int i : count) {
            sum += i;
        }
        return sum;
    }
}
