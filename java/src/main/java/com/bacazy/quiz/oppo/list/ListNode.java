package com.bacazy.quiz.oppo.list;

public class ListNode {
    ListNode next;
    int val = 0;

    public ListNode(int val) {
        this.val = val;
        next = null;
    }

    public void print() {
        ListNode node = this;
        while (node != null) {
            System.out.print(node.val);
            System.out.print(" ");
            node = node.next;
        }
        System.out.println();
    }
}
