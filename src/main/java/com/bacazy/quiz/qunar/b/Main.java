package com.bacazy.quiz.qunar.b;

import java.io.StringReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Scanner;

public class Main {
    static int[] weight = null;
    static int[][] st = null;
    static LinkedList<Integer> nodes = new LinkedList<Integer>();
    private static int n;
    private static int e;

    public static void main(String[] args) {
        Scanner in = new Scanner(new StringReader(
                "4 4\n" +
                        "1 2\n" +
                        "2 3\n" +
                        "3 5\n" +
                        "4 4\n" +
                        "1 2\n" +
                        "1 3\n" +
                        "2 4\n" +
                        "3 4"));
        n = in.nextInt();
        e = in.nextInt();
        weight = new int[n];
        st = new int[e][2];

        for (int i = 0; i < n; i++) {
            int node = in.nextInt();
            int w = in.nextInt();
            weight[node - 1] = w;
        }

        for (int i = 0; i < e; i++) {
            int s = in.nextInt();
            int t = in.nextInt();
            st[i][0] = s - 1;
            st[i][1] = t - 1;
        }

        print(topSort());
    }

    private static void print(List<Integer> list) {
        for (int i : list) {
            System.out.printf("%d ", i + 1);
        }
        System.out.println();
    }

    private static List<Integer> topSort() {
        nodes.clear();
        int[] visit = new int[n];

        List<Integer> list = new ArrayList<Integer>();
        for (int i = 0; i < e; i++) {
            visit[st[i][1]] = 1;
        }

        for (int i = 0; i < n; i++) {
            if (visit[i] < 1) {
                list.add(i);
            } else {
                visit[i] = 0;
            }
        }

        List<Integer> next = new ArrayList<Integer>();

        while (nodes.size() < n) {
            //sort the level and push to nodes and mark it
            int[] sorted = sort(list);
            push(sorted, nodes);
            mark(list, visit);
            //find next level
            list = findNextLevel(visit, list);
        }

        return nodes;
    }

    private static List<Integer> findNextLevel(int[] visit, List<Integer> list) {
        List<Integer> integers = new ArrayList<Integer>();
        int[] v = new int[n];
        for (int node : list) {
            for (int i = 0; i < e; i++) {
                if (st[i][0] == node && visit[st[i][1]] == 0) {
                    if (v[st[i][1]] == 0) {
                        integers.add(st[i][1]);
                        v[st[i][1]] = 1;
                    }
                }
            }
        }

        return integers;
    }

    private static void mark(List<Integer> list, int[] visit) {
        for (int i : list) {
            visit[i] = 1;
        }
    }

    private static void push(int[] ns, LinkedList<Integer> nodes) {
        for (int i : ns) {
            nodes.addLast(i);
        }
    }

    private static int[] sort(List<Integer> list) {
        if (list.size() == 1) {
            return new int[]{list.get(0)};
        }
        int[] s = new int[list.size()];
        for (int i = 0; i < s.length; i++) {
            s[i] = list.get(i);
        }
        int size = s.length;
        for (int i = 0; i < size; i++) {
            int max = weight[i];
            int maxIndex = i;
            for (int j = i; j < size; j++) {
                if (max < weight[j]) {
                    max = weight[j];
                    maxIndex = j;
                }
            }
            int t = s[i];
            s[i] = s[maxIndex];
            s[maxIndex] = t;
        }

        return s;
    }
}
