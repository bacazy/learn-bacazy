package com.bacazy.learn.sort;

/**
 * 将元素插入到已排序的排序的部分中的合适位置
 */
public class InsertionSort extends AbstractSort {
    @Override
    public void sort(Comparable[] a) {
        for (int i = 1; i < a.length; i++) {
            int j = i;
            while (j - 1 >= 0) {
                if (less(a[j], a[j - 1])) {
                    exch(a, j, j - 1);
                } else {
                    break;
                }
                j--;
            }
        }
    }
}
