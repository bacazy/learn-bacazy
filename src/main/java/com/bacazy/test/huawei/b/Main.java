package com.bacazy.test.huawei.b;


import java.util.Scanner;
import java.util.TreeSet;

/**
 * 根据给定的工程依赖情况，计算工程所有的依赖工程列表。
 * <p/>
 * 注：
 * （1）全部工程都由单个的小写字母表示。
 * （2） a:b 表示 a项目依赖于b
 * 输入描述:
 * 输入两个参数：1.需要计算的目标工程2.工程依赖关系，如a:b|a:c
 * 输出描述:
 * 输出工程的所有依赖工程，按照字母顺序排列，如b:c
 */

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner("a,a:b|a:c|a:x|a:f");
        String line = in.nextLine();
        TreeSet<Character> chars = new TreeSet<Character>();
        String[] linesplit = line.split(",");
        char target = linesplit[0].charAt(0);
        int index = linesplit[1].indexOf("|");
        String part = linesplit[1];

        while (index > 0) {
            String dep = part.substring(0, index);
            String[] tp = dep.split(":");
            char t = tp[0].charAt(0);
            char p = tp[1].charAt(0);
            if (t == target) {
                chars.add(p);
            }
            part = part.substring(index + 1);
            index = part.indexOf("|");
        }

        String[] tp = part.split(":");
        char t = tp[0].charAt(0);
        char p = tp[1].charAt(0);
        if (t == target) {
            chars.add(p);
        }


        StringBuilder builder = new StringBuilder();
        for (Character c : chars) {
            builder.append(":" + c);
        }
        builder.deleteCharAt(0);
        System.out.println(builder.toString());
    }


}
