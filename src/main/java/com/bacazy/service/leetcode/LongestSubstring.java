package com.bacazy.service.leetcode;


import java.util.HashSet;
import java.util.LinkedList;

/**
 * Given a string, find the length of the longest substring without repeating characters.
 * <p/>
 * Examples:
 * <p/>
 * Given "abcabcbb", the answer is "abc", which the length is 3.
 * <p/>
 * Given "bbbbb", the answer is "b", with the length of 1.
 * <p/>
 * Given "pwwkew", the answer is "wke", with the length of 3.
 * Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
 */
public class LongestSubstring {
    public int lengthOfLongestSubstring(String s) {
        int start = 0;
        int end = 0;
        int maxLen = 0;
        int len = s.length();
        HashSet<Character> characters = new HashSet<Character>();
        LinkedList<Character> linkedList = new LinkedList<Character>();
        while (start + maxLen <= len && end < len) {
            char e = s.charAt(end);
            if (characters.contains(e)) {
                while (linkedList.size() > 0) {
                    char c = linkedList.getFirst();
                    linkedList.removeFirst();
                    characters.remove(c);
                    start++;
                    if (c == e) {
                        break;
                    }
                }
            }
            characters.add(e);
            linkedList.add(e);
            end++;
            if (characters.size() > maxLen) {
                maxLen = characters.size();
            }
        }

        return maxLen;
    }
}
