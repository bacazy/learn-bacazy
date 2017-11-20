package com.bacazy.learn.search;

import java.util.ArrayList;

/**
 * 链表实现的符号表
 *
 * @param <Key>   键
 * @param <Value> 值
 */
public class SequentialSearchST<Key extends Comparable<Key>, Value> implements ST<Key, Value> {
    private Node head = null;
    private int size = 0;

    public SequentialSearchST() {
    }

    public void put(Key key, Value value) {
        if (head == null) {
            head = new Node(key, value);
        } else {
            Node node = head;
            while (node.next != null) {
                if (node.key.compareTo(key) == 0) {
                    node.value = value;
                    return;
                } else {
                    node = node.next;
                }
            }
            size++;
            node.next = new Node(key, value);
        }
    }

    public Value get(Key key) {
        if (head == null) {
            return null;
        }
        Node node = head;
        while (node.next != null) {
            if (node.key.compareTo(key) == 0) {
                return node.value;
            } else {
                node = node.next;
            }
        }
        return null;
    }

    public void delete(Key key) {
        if (head == null) {
            return;
        }
        Node node = head;
        while (node.next != null) {
            if (node.key.compareTo(key) == 0) {
                node.next = node.next.next;
                size--;
                return;
            } else {
                node = node.next;
            }
        }
    }

    public boolean contains(Key key) {
        if (head == null) {
            return false;
        }
        Node node = head;
        while (node.next != null) {
            if (node.key.compareTo(key) == 0) {
                return true;
            } else {
                node = node.next;
            }
        }
        return false;
    }

    public boolean isEmpty() {
        return size == 0;
    }

    public int size() {
        return size;
    }

    public Iterable<Key> keys() {
        ArrayList<Key> keys = new ArrayList<Key>();
        Node node = head;
        while (node != null) {
            keys.add(node.key);
            node = node.next;
        }
        return keys;
    }

    public Iterable<Value> values() {
        ArrayList<Value> vs = new ArrayList<Value>();
        Node node = head;
        while (node != null) {
            vs.add(node.value);
            node = node.next;
        }
        return vs;
    }

    private class Node {
        Key key;
        Value value;
        Node next;

        public Node(Key key, Value value) {
            this.key = key;
            this.value = value;
        }
    }
}
