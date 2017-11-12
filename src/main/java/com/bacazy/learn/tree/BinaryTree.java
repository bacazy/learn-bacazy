package com.bacazy.learn.tree;


import java.util.Stack;

public class BinaryTree<T> {

    private TreeNode<T> root;

    public BinaryTree(TreeNode<T> root) {
        this.root = root;
    }

    public BinaryTree() {
    }

    public void visit(TreeNode<T> node){
        System.out.print(node.value);
        System.out.print(" ");
    }

    public void inOrderVisitRecursionImpl(TreeNode<T> node){
        if (node == null){
            return;
        }
        inOrderVisitRecursionImpl(node.left);
        visit(node);
        inOrderVisitRecursionImpl(node.right);
    }

    public TreeNode<T> buildWithPreOrder(T[] sequence){

        return root;
    }

    public void inOrderVisitLoopImpl(TreeNode<T> node){
        Stack<TreeNode<T>> stack = new Stack<TreeNode<T>>();
        TreeNode<T> n = node;
        while (node != null || !stack.isEmpty()) {
            if (n != null){
                stack.push(n);
                n = n.left;
            }else {
                n = stack.pop();
                visit(n);
                n = n.right;
            }
        }
    }
}
