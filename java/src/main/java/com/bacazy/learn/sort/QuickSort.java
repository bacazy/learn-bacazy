package com.bacazy.learn.sort;

/**
 * 快速排序算法
 */
public class QuickSort extends AbstractSort {
    @Override
    public void sort(Comparable[] a) {
        sort(a, 0, a.length - 1);
    }

    private void sort(Comparable[] a, int lo, int hi) {
        if (lo >= hi) {
            return;
        }
        int lt = lo;
        int gt = hi;
        int index = lo + 1;
        Comparable pival = a[lo];
        while (index <= gt) {
            int cmp = a[index].compareTo(pival);
            if (cmp > 0) {
                exch(a, index, gt);
                gt--;
                while (gt >= index && less(pival, a[gt])) {
                    gt--;
                }
            } else {
                exch(a, index, lt);
                lt++;
                index++;
            }
        }
        sort(a, lo, gt - 1);
        sort(a, gt + 1, hi);
    }

}
