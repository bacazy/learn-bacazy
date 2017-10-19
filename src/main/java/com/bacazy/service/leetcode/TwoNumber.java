package com.bacazy.service.leetcode;

class ListNode {
    int val = 0;
    ListNode next;

    public ListNode(int val) {
        this.val = val;
    }
}

public class TwoNumber {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode result = new ListNode(0);
        ListNode next = result;
        while ((l1 != null) && (l2 != null)) {
            next.next = new ListNode(l1.val + l2.val);
            next = next.next;
            l1 = l1.next;
            l2 = l2.next;
            if (l1 == null) {
                next.next = l2;
            } else if (l2 == null) {
                next.next = l1;
            }
        }

        next = result;
        int up = 0;
        while (next != null) {
            int val = up + next.val;
            up = val / 10;
            next.val = val % 10;
            if (up != 0 && next.next == null) {
                next.next = new ListNode(up);
                next = next.next;
            }
            next = next.next;
        }

        return result.next;
    }

}
