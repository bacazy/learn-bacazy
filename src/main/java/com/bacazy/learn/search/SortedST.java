package com.bacazy.learn.search;

public interface SortedST<Key extends Comparable<Key>, Value> extends ST<Key, Value> {
    Key min();

    Key max();

    Key floor(Key key);

    Key ceiling(Key key);

    int rank(Key key);

    Key select(int k);

    void deleteMin();

    void deleteMax();

    int size(Key low, Key high);

    Iterable<Key> keys(Key low, Key high);

    Iterable<Value> values(Key low, Key high);
}
