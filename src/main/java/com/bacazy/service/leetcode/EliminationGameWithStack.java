package com.bacazy.service.leetcode;

import java.util.Stack;

/**
 * There is a list of sorted integers from 1 to n. Starting from left to right, remove the first number and every other number afterward until you reach the end of the list.
 * <p/>
 * Repeat the previous step again, but this time from right to left, remove the right most number and every other number from the remaining numbers.
 * <p/>
 * We keep repeating the steps again, alternating left to right and right to left, until a single number remains.
 * <p/>
 * Find the last number that remains starting with a list of length n.
 */
public class EliminationGameWithStack {

    /**
     * 栈版，超时
     *
     * @param n 个数
     * @return 最终的数据
     */
    public int lastRemaining(int n) {
        if (n == 1) {
            return 1;
        }

        if (n == 2) {
            return 2;
        }

        Stack<Integer> stack = new Stack<Integer>();
        for (int i = 0; i < n; i++) {
            if (i % 2 != 0) {
                stack.push(i + 1);
            }
        }

        Stack<Integer> s = null;
        while (stack.size() > 1) {
            s = new Stack<Integer>();
            int i = 0;
            while (!stack.isEmpty()) {
                int p = stack.pop();
                if (i % 2 != 0) {
                    s.push(p);
                }
                i++;
            }
            stack = s;

        }
        return stack.pop();
    }
}
