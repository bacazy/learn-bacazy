package com.bacazy.quiz.hiho.trie;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        LetterTrie p = new LetterTrie('#');
        Scanner in = new Scanner(System.in);
        int num = in.nextInt();
        for (int i = 0; i < num; i++) {
            String s= in.nextLine();
            p.add(s);
        }
        num = in.nextInt();
        for (int i = 0; i < num; i++) {
            String s= in.nextLine();
            System.out.println(p.getCount(s));
        }
    }
}