package com.bacazy.service.leetcode;

import com.bacazy.service.leetcode.util.DualLinkedNode;

/**
 * There is a list of sorted integers from 1 to n. Starting from left to right, remove the first number and every other number afterward until you reach the end of the list.
 * <p/>
 * Repeat the previous step again, but this time from right to left, remove the right most number and every other number from the remaining numbers.
 * <p/>
 * We keep repeating the steps again, alternating left to right and right to left, until a single number remains.
 * <p/>
 * Find the last number that remains starting with a list of length n.
 */


public class EliminationGameWithLinkedList {


    /**
     * 链表，超时
     *
     * @param n 个数
     * @return 最终的数据
     */
    public int lastRemaining(int n) {
        DualLinkedNode<Integer> head = new DualLinkedNode<Integer>(0);
        DualLinkedNode<Integer> tail = new DualLinkedNode<Integer>(0);
        tail.prev = head.next;

        for (int i = 1; i <= n; i++) {
            if (i % 2 == 0) {
                DualLinkedNode<Integer> node = new DualLinkedNode<Integer>(i);
                tail.prev.next = node;
                node.prev = tail.prev;
                node.next = tail;
                tail.prev = node;
            }
        }

        boolean reverse = true;

        while (head.next != tail) {

        }

        return head.next.value;
    }
}
