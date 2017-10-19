package com.bacazy.service.datastructure.tree;


/**
 * @param <Key>
 * @param <Value>
 */
public interface ST<Key extends Comparable<Key>, Value> {

    void put(Key key, Value value);

    Value get(Key key);

    void delete(Key key);

    boolean contains(Key key);

    boolean isEmpty();

    int size();

    Iterable<Key> keys();
}
