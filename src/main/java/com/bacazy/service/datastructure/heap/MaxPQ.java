package com.bacazy.service.datastructure.heap;


public interface MaxPQ<Key extends Comparable<Key>> {
    int size();

    boolean isEmpty();

    Key max();

    void insert(Key key);

    Key delMax();
}
