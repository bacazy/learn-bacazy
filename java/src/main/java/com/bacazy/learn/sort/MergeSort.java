package com.bacazy.learn.sort;

/**
 * 自顶向下，递归方式实现
 */
public class MergeSort extends AbstractSort {
    private Comparable[] aux;

    @Override
    void sort(Comparable[] a) {
        aux = new Comparable[a.length];
        sort(a, 0, a.length - 1);
    }

    private void sort(Comparable[] a, int low, int high) {
        if (high <= low) {
            return;
        }
        int mid = low + (high - low) / 2;//求平均值方法，避免求和溢出
        sort(a, low, mid);
        sort(a, mid + 1, high);
        merge(a, low, mid, high);
    }

    private void merge(Comparable[] a, int low, int mid, int high) {
        System.arraycopy(a, low, aux, low, high + 1 - low);
        int first = low;
        int sec = mid + 1;
        for (int i = low; i <= high; i++) {
            if (first > mid) {
                a[i] = aux[sec];
                sec++;
            } else if (sec > high) {
                a[i] = aux[first];
                first++;
            } else if (less(a[first], a[sec])) {
                a[i] = a[first];
                first++;
            } else {
                a[i] = a[sec];
                sec++;
            }
        }

    }
}
