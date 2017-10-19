package com.bacazy.test.oppo.list;


public class SwapList {
    public static ListNode swap(ListNode head) {
        ListNode f = new ListNode(12);

        if (head != null && head.next != null) {
            swap(f, head, head.next, head.next.next);
        }
        return f.next;
    }

    private static void swap(ListNode prev, ListNode p, ListNode next, ListNode subList) {
        p.next = subList;
        next.next = p;
        prev.next = next;
        if (subList != null && subList.next != null) {
            swap(p, subList, subList.next, subList.next.next);
        }
    }

    public static void main(String[] args) {

    }
}
