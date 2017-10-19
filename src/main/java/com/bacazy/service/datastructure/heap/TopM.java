package com.bacazy.service.datastructure.heap;


public class TopM implements MaxPQ<Integer> {

    int[] heap = null;
    int size = 0;
    int capacity = 10;

    public TopM() {
        heap = new int[capacity];
    }

    public TopM(int capacity) {
        this.capacity = capacity;
        heap = new int[capacity];
    }

    public synchronized int size() {
        return size;
    }

    public synchronized boolean isEmpty() {
        return size == 0;
    }

    public synchronized Integer max() {
        return heap[0];
    }

    public synchronized void insert(Integer integer) {
        if (size >= capacity - 1) {
            capacity = capacity * 2;
            resize(capacity);
        }
        heap[size++] = integer;
        swim(size - 1);
    }

    private synchronized void resize(int capacity) {
        int[] els = new int[capacity];
        System.arraycopy(heap, 0, els, 0, size);
        heap = els;
    }

    public synchronized Integer delMax() {
        if (size < capacity / 2 - 2 && capacity > 20) {
            capacity = capacity / 2;
            resize(capacity);
        }
        return null;
    }

    private synchronized void sink(int k) {

    }

    private synchronized void swim(int index) {
        while (index > 1 && heap[index / 2] < heap[index]) {
            exchange(index / 2, index);
            index = index / 2;
        }
    }

    private synchronized void exchange(int a, int b) {
        int t = heap[a];
        heap[a] = heap[b];
        heap[b] = t;
    }

}
