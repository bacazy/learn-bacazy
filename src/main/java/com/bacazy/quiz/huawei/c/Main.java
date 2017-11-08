package com.bacazy.quiz.huawei.c;


import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
//        String str1 = in.nextLine().trim();
//        String str2 = in.nextLine().trim();
//        System.out.println(longestCommonString(str1, str2));
        System.out.println(LCS("abccade", "dgcadde"));
    }

    private static int LCS(String str1, String str2) {
        boolean[][] chars = new boolean[str1.length() + 1][str2.length() + 1];
        for (int i = 0; i <= str1.length(); i++) {
            for (int j = 0; j <= str2.length(); j++) {
                if (i == 0 || j == 0) {
                    chars[i][j] = false;
                } else {
                    chars[i][j] = str1.charAt(i - 1) == str2.charAt(j - 1);
                }
            }
        }

        int maxNum = 0;
        int[][] len = new int[str1.length() + 1][str2.length() + 1];
        for (int i = 0; i <= str2.length(); i++) {
            for (int j = 0; j <= str2.length(); j++) {
                if (i == 0 || j == 0) {
                    len[i][j] = 0;
                } else if (chars[i - 1][j - 1]) {
                    len[i][j] = len[i - 1][j - 1];

                }
            }
        }

        return maxNum;
    }

    private static int longestCommonString(String str1, String str2) {
        char[] sa = str1.toCharArray();
        char[] sb = str2.toCharArray();
        int maxL = 0;
        for (int i = 0; i < sa.length; i++) {
            for (int j = 0; j < sb.length; j++) {
                if (sa[i] == sb[j]) {
                    int l = 1;
                    int ai = i + 1;
                    int bj = j + 1;
                    while (ai < sa.length && bj < sb.length) {
                        if (sa[ai] == sb[bj]) {
                            ai++;
                            bj++;
                            l++;
                            if (l > maxL) {
                                maxL = l;
                            }
                        }
                    }
                }
                if (j + maxL > sb.length) {
                    break;
                }
            }
            if (i + maxL > sa.length) {
                break;
            }
        }
        return maxL;
    }

}
