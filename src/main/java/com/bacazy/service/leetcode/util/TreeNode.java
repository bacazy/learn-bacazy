package com.bacazy.service.leetcode.util;


public class TreeNode<T> {
    public TreeNode<T> left = null;
    public TreeNode<T> right = null;
    T value;

    public TreeNode(T value) {
        this.value = value;
    }

    public T getValue() {
        return value;
    }

    public void setValue(T value) {
        this.value = value;
    }
}
