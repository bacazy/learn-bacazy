package com.bacazy.learn.sort;


import java.util.Arrays;

public abstract class AbstractSort {

    protected boolean less(Comparable v, Comparable w) {
        return v.compareTo(w) < 0;
    }

    protected void exch(Comparable[] a, int i, int j) {
        Comparable t = a[i];
        a[i] = a[j];
        a[j] = t;
    }

    protected void print(Comparable[] a) {
        System.out.println(Arrays.toString(a));
    }

    public boolean isSorted(Comparable[] a) {
        for (int i = 0; i < a.length - 1; i++) {
            if (less(a[i + 1], a[i])) {
                return false;
            }
        }
        return true;
    }

    abstract void sort(Comparable[] a);
}
