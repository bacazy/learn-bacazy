package com.bacazy.learn.find;

import java.util.ArrayList;
import java.util.List;
import java.util.Queue;
import java.util.Stack;

/**
 * 二叉查找树
 *
 * @param <Key>
 * @param <Value>
 */
public class BST<Key extends Comparable<Key>, Value> implements SortedST<Key, Value> {

    private class Node {
        Key key;
        Value value;
        int size = 1;
        Node left;
        Node right;

        public Node(){}

        public Node(Key key, Value value) {
            this.key = key;
            this.value = value;
        }
    }

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
     * 升序的顺序
     * @param key 目标键值
     * @return 排名
     */
    public int rank(Key key) {
        return rank(root, key);
    }

    private int rank(Node root, Key key) {
        if (root == null){
            return 0;
        }
        int cmp = key.compareTo(root.key);
        if (cmp == 0){
            return count(root.left);
        }
        if (cmp > 0){
            return 1 + count(root.left) + rank(root.right, key);
        }

        return rank(root.left, key);
    }

    public Key select(int k) {
        Node node = select(root,k);
        if (node == null){
            return null;
        }
        return node.key;
    }

    private Node select(Node node, int k) {
        if (node == null){
            return null;
        }
        int s = count(node.left);
        if (s == k){
            return node;
        }

        if (s > k){
            return select(node.left,k);
        }else {
            return select(node.right, k - s - 1);
        }
    }

    /**
     * 若树为空，则直接返回不处理
     */
    public void deleteMin() {
        if (root == null){
            return;
        }
        if (root.left == null){
            root = root.right;
            return;
        }

        Node node = root;
        Stack<Node> route = new Stack<Node>();
        while (node.left != null){
            route.add(node);
            node = node.left;
        }

        //父节点的左连接 指向 最小值的 右子树，这样就删除了最小值
        Node leaf = route.pop();
        Node parent = route.peek();
        parent.left = leaf.right;

        while (!route.isEmpty()){//更新节点计数器
            Node n = route.pop();
            n.size = count(n.left) + count(n.right) + 1;
        }
    }

    public void deleteMax() {
        if (root == null){
            return;
        }
        if (root.right == null){
            root = root.left;
            return;
        }

        Node node = root;
        Stack<Node> route = new Stack<Node>();
        while (node.right != null){
            route.add(node);
            node = node.right;
        }

        //父节点的右连接 指向 最大值的 左子树，这样就删除了最大值
        Node leaf = route.pop();
        Node parent = route.peek();
        parent.right = leaf.left;

        while (!route.isEmpty()){//更新节点计数器
            Node n = route.pop();
            n.size = count(n.left) + count(n.right) + 1;
        }
    }

    /**
     * 闭区间
     * @param low 下限
     * @param high 上限
     * @return 数量
     */
    public int size(Key low, Key high) {
        List<Key> ls = new ArrayList<Key>();
        keys(root, ls, low, high);
        return ls.size();
    }

    private void keys(Node node, List<Key> list, Key low, Key high) {
        if (node == null){
            return;
        }
        int cmplow = low.compareTo(node.key);
        int cmphigh = high.compareTo(node.key);
        if (cmplow < 0){
            keys(node.left,list,low,high);
        }
        if (cmplow >= 0 && cmphigh >= 0){
            list.add(node.key);
        }
        if (cmphigh > 0){
            keys(node.right, list, low, high);
        }
    }

    public Iterable<Key> keys(Key low, Key high) {
        List<Key> ls = new ArrayList<Key>();
        keys(root, ls, low, high);
        return ls;
    }

    public Iterable<Value> values(Key low, Key high) {
        List<Value> ls = new ArrayList<Value>();
        values(root, ls, low, high);
        return ls;
    }

    private void values(Node node, List<Value> list, Key low, Key high) {
        if (node == null){
            return;
        }
        int cmplow = low.compareTo(node.key);
        int cmphigh = high.compareTo(node.key);
        if (cmplow < 0){
            values(node.left, list, low, high);
        }
        if (cmplow >= 0 && cmphigh >= 0){
            list.add(node.value);
        }
        if (cmphigh > 0){
            values(node.right, list, low, high);
        }
    }

    public void put(Key key, Value value) {
        root = put(root, key, value);
    }

    private Node put(Node node, Key key, Value value) {
        if (node == null){
            return new Node(key,value);
        }

        int cmp = key.compareTo(node.key);
        if (cmp < 0){
            node.left = put(node.left,key,value);
        }else if (cmp > 0){
            node.right = put(node.right,key,value);
        }else {
            node.value =value;
        }
        node.size = count(node.left) + count(node.right) + 1;
        return node;
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
        root = delete(root, key);
    }

    private Node delete(Node node, Key key) {
        if (node == null){
            return null;
        }

        int cmp = key.compareTo(node.key);
        if (cmp < 0){
            node.left = delete(node.left,key);
        }else if (cmp > 0){
            node.right = delete(node.right,key);
        }else {
            if (node.right == null){
                return node.left;
            }
            if (node.left == null){
                return node.right;
            }
            Node t = node;
            node = min(t.right);
            node.right = deleteMin(t.right);
            node.left = t.left;
        }
        node.size = count(node.left) + count(node.right) + 1;
        return node;
    }

    private Node deleteMin(Node x) {
        if (x.left == null){
            return x.right;
        }
        x.left = deleteMin(x.left);
        x.size = count(x.left) + count(x.right) + 1;
        return x;
    }

    private Node min(Node node) {
        if (node == null){
            return null;
        }

        while (node.left != null){
            node = node.left;
        }
        return node;
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
        //TODO:BUG

        while (node == null || !stack.isEmpty()) {
            if (node != null){
                stack.push(node);
                node = node.left;
            }else {
                node = stack.pop();
                keys.add(node.key);

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

    public void print(){
        if (root == null){
            System.out.println("Empty Tree");
            return;
        }
        int depth = Math.max(depth(root.left),depth(root.right)) + 1;
        Key[] keys = (Key[]) new Object[1<<(depth-1)];
        fill(keys,root,0);

    }



    private void fill(Key[] keys, Node node, int index) {
        if (node == null){
            return;
        }
        keys[index] = node.key;
        fill(keys,node.left, 2*index + 1);
        fill(keys,node.right, 2*index + 2);
    }

    private int depth(Node node) {
        if (node == null){
            return 1;
        }
        return Math.max(depth(node.left), depth(node.right)) + 1;
    }
}
