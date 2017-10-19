package com.bacazy.service.datastructure.tree;


/**
 * @author gc_zc
 */
public class TreeNode<T> {
    public T value = null;
    public TreeNode<T> left = null;
    public TreeNode<T> right = null;

    public TreeNode(T value) {
        this.value = value;
    }

    public TreeNode() {
    }

    @Override
    public String toString() {
        return String.valueOf(value);
    }
}
