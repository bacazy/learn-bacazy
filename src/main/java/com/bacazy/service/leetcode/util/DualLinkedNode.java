package com.bacazy.service.leetcode.util;

public class DualLinkedNode<T> {
    public T value;
    public DualLinkedNode<T> prev = null;
    public DualLinkedNode<T> next = null;

    public DualLinkedNode(T value) {
        this.value = value;
    }

    public DualLinkedNode(T value, DualLinkedNode<T> prev, DualLinkedNode<T> next) {
        this.value = value;
        this.prev = prev;
        this.next = next;
    }
}
