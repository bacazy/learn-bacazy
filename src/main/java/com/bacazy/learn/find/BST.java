package com.bacazy.learn.find;

import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

/**
 * 二叉查找树
 *
 * @param <Key>
 * @param <Value>
 */
public class BST<Key extends Comparable<Key>, Value> implements SortedST<Key, Value> {

    Node root;

    public Key min() {
        if (root == null) {
            return null;
        }

        Node node = root;
        while (node.left != null) {
            node = node.left;
        }
        return node.key;
    }

    public Key max() {
        if (root == null) {
            return null;
        }
        Node node = root;
        while (node.right != null) {
            node = node.right;
        }
        return node.key;
    }

    public Key floor(Key key) {
        Node f = floor(root, key);
        if (f == null) {
            return null;
        }
        return f.key;
    }

    private Node floor(Node root, Key key) {
        if (root == null) {
            return null;
        }

        //比较大小
        int cmp = key.compareTo(root.key);
        if (cmp == 0) {
            return root;
        }
        //比根节点小，则一定在左子树中
        if (cmp < 0) {
            return floor(root.left, key);
        } else {
            //比根节点大，则可能在右子树中
            Node f = floor(root.right, key);
            if (f == null) {//右子树中不存在，则根节点则是下取整
                return root;
            }
            return f;
        }
    }

    private int count(Node root) {
        if (root == null) {
            return 0;
        }
        return root.size;
    }

    public Key ceiling(Key key) {
        Node node = ceiling(root, key);
        if (node == null) {
            return null;
        }
        return node.key;
    }

    private Node ceiling(Node node, Key key) {
        if (node == null) {
            return null;
        }

        int cmp = key.compareTo(node.key);
        if (cmp == 0) {
            return node;
        }

        if (cmp > 0) {
            return ceiling(node.right, key);
        } else {
            Node c = ceiling(node.left, key);
            if (c == null) {
                return node;
            }
            return c;
        }
    }

    /**
     * @param key
     * @return
     */
    public int rank(Key key) {
        return rank(root, key);
    }

    private int rank(Node root, Key key) {


        return 0;
    }

    public Key select(int k) {

        return null;
    }

    public void deleteMin() {

    }

    public void deleteMax() {

    }

    public int size(Key low, Key high) {
        return 0;
    }

    public Iterable<Key> keys(Key low, Key high) {
        return null;
    }

    public Iterable<Value> values(Key low, Key high) {
        return null;
    }

    public void put(Key key, Value value) {

    }

    public Value get(Key key) {
        Node node = root;
        while (node != null) {
            int cmp = key.compareTo(node.key);
            if (cmp == 0) {
                return node.value;
            }
            if (cmp > 0) {
                node = node.right;
            } else {
                node = node.left;
            }
        }
        return null;
    }

    public void delete(Key key) {

    }

    public boolean contains(Key key) {
        Node node = root;
        while (node != null) {
            int cmp = key.compareTo(node.key);
            if (cmp == 0) {
                return true;
            }
            if (cmp > 0) {
                node = node.right;
            } else {
                node = node.left;
            }
        }
        return false;
    }

    public boolean isEmpty() {
        return size() == 0;
    }

    public int size() {
        return count(root);
    }

    /**
     * 键集合,循环版本
     *
     * @return 有序
     */
    public Iterable<Key> keys() {
        List<Key> keys = new ArrayList<Key>();
        Stack<Node> stack = new Stack<Node>();
        Node node = root;
        while (node != null) {
            stack.push(node);
            node = node.left;
        }
        while (!stack.isEmpty()) {
            Node n = stack.pop();
            keys.add(n.key);
            if (n.right != null) {
                n = n.right;
                while (n != null) {
                    stack.push(n.left);
                    n = n.left;
                }
            }
        }

        return keys;
    }

    /**
     * 递归版本实现值集合获取，按键有序排列
     *
     * @return
     */
    public Iterable<Value> values() {
        List<Value> values = new ArrayList<Value>();
        InOrderVisit(values, root);
        return values;
    }

    private void InOrderVisit(List<Value> values, Node root) {
        if (root == null) {
            return;
        }
        InOrderVisit(values, root.left);
        values.add(root.value);
        InOrderVisit(values, root.right);
    }

    private class Node {
        Key key;
        Value value;
        int size = 0;
        Node left;
        Node right;

    }
}
