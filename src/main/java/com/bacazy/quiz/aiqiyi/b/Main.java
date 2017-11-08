package com.bacazy.quiz.aiqiyi.b;


import java.util.Scanner;
import java.util.Stack;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String str = in.nextLine();
        System.out.println(minBraket(str));
    }

    private static int minBraket(String str) {
        Stack<Character> brakets = new Stack<Character>();
        for (int i = 0; i < str.length(); i++) {
            if (brakets.empty()) {
                brakets.push(str.charAt(i));
            } else if (str.charAt(i) == ')' && brakets.peek() == '(') {
                brakets.pop();
            } else {
                brakets.push(str.charAt(i));
            }
        }
        return brakets.size();
    }
}
