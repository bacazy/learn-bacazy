package com.bacazy.quiz.renren.b;


import java.util.Arrays;
import java.util.Scanner;

class Pos implements Comparable<Pos> {
    public int x = 0;
    public int y = 0;

    public Pos(int x, int y) {
        this.x = x;
        this.y = y;
    }


    public int compareTo(Pos o) {
        if (this.y == o.y) {
            return this.x - o.x;
        } else {
            return this.y - o.y;
        }
    }
}


public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int N = in.nextInt();
        int M = in.nextInt();
        int K = in.nextInt();
        Pos[] poses = new Pos[K];
        for (int i = 0; i < K; i++) {
            poses[i] = new Pos(in.nextInt(), in.nextInt());
        }
        findPath(N, M, poses);
    }

    private static void findPath(int n, int m, Pos[] pos) {
        Arrays.sort(pos);
        int i = 1;
        int j = 1;
        int index = 0;
        StringBuilder builder = new StringBuilder("");
        while (index < pos.length && i <= n && j <= m) {
            while (j < pos[index].y) {//move to the row
                builder.append("D");
                j++;
            }

            if (i > pos[index].x) {
                System.out.println("Impossible");
                return;
            }

            while (i < pos[index].x) {
                builder.append("R");
                i++;
            }
            index++;
        }
        while (j < m) {//move to the row
            builder.append("D");
            j++;
        }

        while (i < n) {
            builder.append("R");
            i++;
        }

        System.out.println(builder.toString());
    }


}
