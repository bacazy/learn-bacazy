package com.bacazy.service.leetcode.util;


public class LinkedList<T> {
    public LinkedList<T> next = null;
    T value;

    public LinkedList(T value) {
        this.value = value;
    }

    public T getValue() {
        return value;
    }

    public void setValue(T value) {
        this.value = value;
    }
}
