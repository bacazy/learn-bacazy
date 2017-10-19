package com.bacazy.test.ify;


import java.io.StringReader;
import java.util.Scanner;

class Lesson {
    public Lesson next = null;
    public int id = 0;
}


public class Main {


    public static void main(String[] args) {
        Scanner in = new Scanner(new StringReader(
                "5\n" +
                        "01 204521\n" +
                        "23 204523\n" +
                        "22 204526\n" +
                        "01 204528\n" +
                        "22 204527"
        ));

        Lesson[][] lessons = new Lesson[5][10];
        int count = in.nextInt();
        int size = 0;
        for (int i = 0; i < count; i++) {
            int t = in.nextInt();
            int lid = in.nextInt();
            Lesson lesson = new Lesson();
            lesson.id = lid;

            if (lessons[t / 10][t % 10] == null) {
                lessons[t / 10][t % 10] = lesson;
            } else {
                size++;
                Lesson l = lessons[t / 10][t % 10];
                while (l.next != null) {
                    l = l.next;
                }
                l.next = lesson;
            }
        }
        if (size == 0) {
            System.out.println("YES");
        } else {
            for (int i = 0; i < 5; i++) {
                for (int j = 0; j < 10; j++) {
                    if (lessons[i][j] != null && lessons[i][j].next != null) {
                        System.out.printf("%d%d ", i, j);
                        Lesson l = lessons[i][j];
                        System.out.printf("%d ", l.id);
                        while (l.next != null) {
                            System.out.printf("%d ", l.next.id);
                            l = l.next;
                        }
                        System.out.println();
                    }

                }
            }
        }

    }
}
