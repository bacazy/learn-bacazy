package com.bacazy.service.leetcode;

public class LeetCode {

    public boolean isPalindrome(int x) {
        String s = String.valueOf(x);
        int a = 0, b = s.length() - 1;
        while (b > a) {
            if (s.charAt(b) != s.charAt(a)) {
                return false;
            }
            b--;
            a++;
        }
        return true;
    }
}
