package com.bacazy.service.datastructure.tree;


import java.util.Arrays;

public class BinaryTree<T extends Comparable> {
    private TreeNode<T> root = null;

    public BinaryTree(TreeNode<T> root) {
        this.root = root;
    }

    public static BinaryTree<Integer> genIntegerTreeFromPreAndInOrder(int[] pre, int[] in) throws Exception {
        if (pre.length != in.length) {
            throw new Exception("length should be the same");
        }
        TreeNode<Integer> root = createFromPreAndInOrder(pre, in);
        return new BinaryTree<Integer>(root);
    }

    private static TreeNode<Integer> createFromPreAndInOrder(int[] pre, int[] in) {
        if (pre.length > 0) {
            TreeNode<Integer> root = new TreeNode<Integer>(pre[0]);
            int splitor = pre[0];
            int len = 0;
            for (int i = 0; i < in.length; i++) {
                if (splitor == in[i]) {
                    len = i;
                    break;
                }
            }
            root.left = createFromPreAndInOrder(Arrays.copyOfRange(pre, 1, len + 1),
                    Arrays.copyOfRange(in, 0, len));
            root.right = createFromPreAndInOrder(Arrays.copyOfRange(pre, len + 1, pre.length),
                    Arrays.copyOfRange(in, len + 1, in.length));

            return root;
        } else {
            return null;
        }
    }


    public void preOrderTraverse() {
        preOrderTraverse(root);
    }

    public void inOrderTraverse() {
        inOrderTraverse(root);
    }

    private void inOrderTraverse(TreeNode<T> root) {
        if (root == null) {
            return;
        }
        preOrderTraverse(root.left);
        System.out.println(root);
        preOrderTraverse(root.right);
    }

    public void postOrderTraverse() {
        postOrderTraverse(root);
    }

    private void postOrderTraverse(TreeNode<T> root) {
        if (root == null) {
            return;
        }
        preOrderTraverse(root.left);
        preOrderTraverse(root.right);
        System.out.println(root);
    }

    private void preOrderTraverse(TreeNode<T> root) {
        if (root == null) {
            return;
        }
        System.out.println(root);
        preOrderTraverse(root.left);
        preOrderTraverse(root.right);
    }


}
