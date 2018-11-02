package com.bacazy.quiz.renren.c;

import java.util.Scanner;

class Line {
    public int[] p1;
    public int[] p2;

    public Line(int x1, int y1, int x2, int y2) {
        p1 = new int[]{x1, y1};
        p2 = new int[]{x2, y2};
    }

    public boolean onLine(int[] p) {
        if ((p[0] - p1[0]) * (p[0] - p2[0]) >= 0 || (p[1] - p1[1]) * (p[1] - p2[1]) >= 0) {
            return false;
        }

        return (p1[0] - p2[0]) * (p1[1] - p[1]) - (p1[0] - p[0]) * (p1[1] - p2[2]) == 0;
    }

    public boolean canJoint(Line line) {
        if (p1[0] == line.p1[0] && p1[1] == line.p1[1]) {
            return true;
        }

        if (p1[0] == line.p2[0] && p2[1] == line.p2[1]) {
            return true;
        }

        if (p2[0] == line.p2[0] && p1[1] == line.p1[1]) {
            return true;
        }

        return p2[0] == line.p2[0] && p2[1] == line.p2[1];

    }
}

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int groups = scanner.nextInt();
        for (int i = 0; i < groups; i++) {
            Line[] lines = new Line[3];
            for (int j = 0; j < lines.length; j++) {
                lines[j] = new Line(scanner.nextInt(),
                        scanner.nextInt(),
                        scanner.nextInt(),
                        scanner.nextInt());
            }
            System.out.println(identify(lines) ? "YES" : "NO");
        }
    }

    private static boolean identify(Line[] lines) {
        Line l3 = findThirdLine(lines);
        if (l3 == null) {
            return false;
        }
        Line[] jls = jointLines(lines, l3);
        if (CA(jls, l3)) {
            return false;
        }


        return false;
    }

    private static boolean CA(Line[] jls, Line l3) {

        return true;
    }

    private static Line[] jointLines(Line[] lines, Line l3) {
        Line[] ls = new Line[2];
        int index = 0;
        for (Line l : lines) {
            if (l == l3) {
                continue;
            }
            ls[index++] = l;
        }
        return ls;
    }

    private static Line findThirdLine(Line[] lines) {
        for (int i = 0; i < lines.length; i++) {
            for (int j = 1; j < lines.length; j++) {
                if (lines[i].canJoint(lines[j])) {
                    return lines[6 / ((i + 1) * (j + 1)) - 1];
                }
            }
        }

        return null;
    }
}
