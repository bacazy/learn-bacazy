package com.bacazy.service.datastructure.tree;


import java.util.Iterator;

/**
 * @author gc_zc
 */
public interface SortedST<Key extends Comparable<Key>, Value> extends ST<Key, Value> {
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
