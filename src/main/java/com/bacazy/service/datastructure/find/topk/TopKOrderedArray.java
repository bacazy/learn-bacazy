package com.bacazy.service.datastructure.find.topk;


import java.util.ArrayList;
import java.util.Collection;
import java.util.List;

public class TopKOrderedArray<T extends Comparable> {
    private LinkedNode<T> head;
    private LinkedNode<T> tail;
    private int capacity = 0;
    private int size = 0;


    public TopKOrderedArray(int k) {
        capacity = k;
        head = new LinkedNode<T>();
    }

    public List<T> getTopk(Collection<T> array) {
        if (array.size() <= capacity) {
            return new ArrayList<T>(array);
        }

        head.next = tail;
        head.parent = null;
        tail.parent = head;
        tail.next = null;

        size = 0;

        for (T e : array) {
            validateAndAdd(e);
        }

        LinkedNode<T> node = head.next;
        List<T> list = new ArrayList<T>();
        while (node != null) {
            list.add(node.data);
            node = node.next;
        }
        return list;
    }

    private void validateAndAdd(T e) {
        T first = head.next.data;
        T last = tail.parent.data;
        if (size < capacity) {
            LinkedNode<T> prev = findPrev(e);
        } else {


        }
    }

    private LinkedNode<T> findPrev(T e) {
        LinkedNode node = head;

        return node;
    }
}
