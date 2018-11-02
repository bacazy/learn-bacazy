package com.bacazy.quiz.common;

public class CharTreeNode extends TreeNode<Character> {

    public CharTreeNode createTree(String preOrder, String inOrder) {
        if (preOrder.isEmpty() || inOrder.isEmpty()) {

        }
        char root = preOrder.charAt(0);
        int index = inOrder.indexOf(root);
        CharTreeNode rootNode = new CharTreeNode();
        rootNode.value = root;
        rootNode.left = createTree(
                preOrder.substring(1, index + 1),
                inOrder.substring(0, index));
        rootNode.right = createTree(
                preOrder.substring(1 + index),
                inOrder.substring(index + 1));
        return rootNode;
    }

}
