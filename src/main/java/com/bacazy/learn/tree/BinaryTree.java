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
        while (node!=null){
            stack.push(node);
            if (node.left != null){
                node = node.left;
            }else {
                break;
            }
        }
        while (!stack.isEmpty()){
            TreeNode<T> n = stack.pop();
            visit(n);
            if (n.right != null){
                n = n.right;
                while (true){
                    stack.push(n);
                    if (n.left != null){
                        n = n.left;
                    }else {
                        break;
                    }
                }
            }
        }
    }
}
