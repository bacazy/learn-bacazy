# 算法-查找算法

## 有序数组中的二分查找
```java
int binarySearch(int[] array, int target){
    int lo = 0;
    int hi = array.length - 1;
    while (lo <= hi){
        int mid = lo + (hi - lo)/2;
        int m = array[mid];
        if (m == target){
            return mid;
        }
        if (m < target){
            lo = mid + 1;
        }else {
            hi = mid - 1;
        }
    }
    return -1;
}
```

## 二叉树的遍历

树结构定义
```java
public class TreeNode<T> {
    public T value;
    public TreeNode<T> left;
    public TreeNode<T> right;

    public TreeNode(T value) {
        this.value = value;
    }
    public TreeNode() {
    }
}
```
中序遍历（递归版本）
```java
public void inOrderVisitRecursionImpl(TreeNode<T> node){
    if (node == null){
        return;
    }
    inOrderVisitRecursionImpl(node.left);
    visit(node);
    inOrderVisitRecursionImpl(node.right);        
}
```
中序遍历（循环版本）
```java
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
```

## 二叉查找树
**定义**：一颗二叉查找树，其中每个节点都含有一个Comparable的键（和相关联的值）且每个节点的键都大于其左子树中任意节点的键值而小于右子树的任意节点的键。

BST的中序遍历结果为一个有序表。使用一个有序符号表的API：
```java
public interface IBinarySearchTree<Key extends Comparable<Key>, Value> {
    void put(Key key, Value value);
    Value get(Key key);
    void delete(Key key);
    boolean contains(Key key);
    boolean isEmpty();
    int size();
    Iterable<Key> keys();
    Key min();
    Key max();
    Key floor(Key key);
    Key ceiling(Key key);
    int rank(Key key);
    Key select(int k);
    void deleteMin();
    void deleteMax();
    int size(Key lo, Key hi);
    Iterator<Key> keys(Key lo, Key hi);
}
```
二叉查找树的声明：
```java
public class BST<Key extends Comparable<Key>, Value> implements SortedST<Key, Value> {
    private class Node {
        Key key;
        Value value;
        int size = 0; //树的大小
        Node left;
        Node right;

        public Node(){}
        public Node(Key key, Value value) {
            this.key = key;
            this.value = value;
        }
    }
    Node root;
}
```
计数器：
```java
public int size() {
    return count(root);
}
private int count(Node root) {
    if (root == null) {
        return 0;
    }
    return root.size;
}
```
查找，插入：
```java
public Value get(Key key) {
    Node node = root;
    while (node != null) {
        int cmp = key.compareTo(node.key);
        if (cmp == 0) {
            return node.value;//相等则返回值
        }
        if (cmp > 0) {//大于0，在右子树查找
            node = node.right;
        } else {//小于0，左子树查找
            node = node.left;
        }
    }
    return null;//没有则返回null
}

public void put(Key key, Value value) {
        root = put(root, key, value);
    }

private Node put(Node node, Key key, Value value) {
    if (node == null){
        return new Node(key,value);//为空则新建节点
    }
    int cmp = key.compareTo(node.key);
    if (cmp < 0){
        node.left = put(node.left,key,value);
    }else if (cmp > 0){
        node.right = put(node.right,key,value);//比根节点大，则在右子树查找
    }else {
        node.value =value;//键相等，更新值即可
    }
    node.size = count(node.left) + count(node.right) + 1;//更新计数器
    return node;
}
```

