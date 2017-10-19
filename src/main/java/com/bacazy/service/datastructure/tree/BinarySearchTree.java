package com.bacazy.service.datastructure.tree;


public class BinarySearchTree<T extends Comparable> {
    TreeNode<T> root = null;

    public BinarySearchTree(TreeNode<T> root) {
        this.root = root;
    }

    public boolean contains(T object) {
        return false;
    }
}
