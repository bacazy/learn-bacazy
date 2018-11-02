package com.bacazy.learn.sort;

public class HeapSort extends AbstractSort {
    @Override
    void sort(Comparable[] a) {
        int N = a.length;
        for (int k = (N - 2) / 2; k >= 0; k--) {
            sink(a, k, N);
        }
        while (N > 0) {
            exch(a, 0, --N);
            sink(a, 0, N);
        }
    }

    private void sink(Comparable[] a, int k, int n) {
        while (2 * (k + 1) <= n) {
            int j = 2 * k + 1;
            if (j < n - 1 && less(a[j], a[j + 1])) {
                j++;
            }
            if (less(a[k], a[j])) {
                exch(a, k, j);
                k = j;
            } else {
                break;
            }
        }
    }
}
