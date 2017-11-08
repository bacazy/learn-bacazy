package com.bacazy.learn.sort;

/**
 * 每次选择最小的元素与第一个交换
 */
public class SelectionSort extends AbstractSort {
    @Override
    public void sort(Comparable[] a) {
        for (int i = 0; i < a.length - 1; i++) {
            Comparable min = a[i];
            int mindex = i;
            for (int j = i + 1; j < a.length; j++) {
                if (less(a[j], min)) {
                    mindex = j;
                    min = a[j];
                }
            }
            exch(a, i, mindex);
        }
    }
}
