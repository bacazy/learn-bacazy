package com.bacazy.service.leetcode;


public class PalindromeString {

    /**
     * Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
     *
     * @param s the given string
     * @return the longest palindrome string
     */
    public String longestPalindrome(String s) {

        int size = s.length();
        int len = size;
        while (size > 0) {
            for (int i = 0; i <= len - size; i++) {
                if (isPalindrom(s, i, i + size - 1)) {
                    return s.substring(i, i + size);
                }
            }

            size--;
        }
        return "";
    }

    private boolean isPalindrom(String s, int i, int j) {
        while (i < j) {
            if (!(s.charAt(i) == s.charAt(j))) {
                return false;
            }
            i++;
            j--;
        }
        return true;
    }
}
