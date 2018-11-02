package com.bacazy.learn.sort;

/**
 * 三向切分快速排序，将相等元素单独作为一部分
 */
public class QuickThreeWaySort extends AbstractSort {
    @Override
    void sort(Comparable[] a) {
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
                //可不加下面语句，但可以提高效率，减少交换次数
                while (gt > index && less(pival, a[gt])) {
                    gt--;
                }
            } else if (cmp < 0) {
                exch(a, lt, index);
                lt++;
                index++;
            } else {
                index++;
            }
        }
        sort(a, lo, lt - 1);
        sort(a, gt + 1, hi);
    }
}
