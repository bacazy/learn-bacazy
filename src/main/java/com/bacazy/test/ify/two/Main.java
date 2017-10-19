package com.bacazy.test.ify.two;

import java.io.StringReader;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

class Team implements Comparable<Team> {
    public String name = "";
    public int score = 0;
    public int m = 0;//
    public int all = 0;//

    public Team(String name) {
        this.name = name;
    }

    @Override
    public int compareTo(Team o) {
        if (this.score != o.score) {
            return o.score - this.score;
        } else if (this.m != o.m) {
            return this.m - o.m;
        } else {
            return this.all - o.all;
        }
    }
}

public class Main {

    public static void main(String[] args) {
        Scanner in = new Scanner(new StringReader(
                "4\n" +
                        "A\n" +
                        "B\n" +
                        "C\n" +
                        "D\n" +
                        "A-B 1:1\n" +
                        "A-C 2:2\n" +
                        "A-D 1:0\n" +
                        "B-C 1:0\n" +
                        "B-D 0:3\n" +
                        "C-D 0:3\n" +
                        "2\n" +
                        "a\n" +
                        "A\n" +
                        "a-A 2:1"));
        while (in.hasNext()) {
            int tc = in.nextInt();
            Map<String, Team> tmap = new HashMap<String, Team>(tc);
            in.nextLine();
            for (int i = 0; i < tc; i++) {
                String name = in.nextLine();
                tmap.put(name, new Team(name));
            }
            for (int i = 0; i < tc * (tc - 1) / 2; i++) {
                String line = in.nextLine();
                String[] ls = line.split(" ");
                String[] tns = ls[0].split("-");
                String[] scs = ls[1].split(":");
                int[] scores = new int[2];
                scores[0] = Integer.parseInt(scs[0]);
                scores[1] = Integer.parseInt(scs[1]);
                Team a = tmap.get(tns[0]);
                Team b = tmap.get(tns[1]);
                a.all = a.all + scores[0];
                b.all = b.all + scores[1];
                if (scores[0] == scores[1]) {
                    a.score = a.score + 1;
                    b.score = b.score + 1;
                } else if (scores[0] > scores[1]) {
                    a.score = a.score + 3;
                    a.m = a.m + scores[0] - scores[1];
                } else {
                    b.score = b.score + 3;
                    b.m = b.m + scores[1] - scores[0];
                }
            }
            Team[] teams = new Team[tc];
            int j = 0;
            for (Team t : tmap.values()) {
                teams[j] = t;
                j++;
            }
            Arrays.sort(teams);
            for (int i = 0; i < teams.length / 2; i++) {
                System.out.println(teams[i].name);
            }
        }
    }
}
