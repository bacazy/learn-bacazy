package com.bacazy.learn.sort;

/**
 * 等间隔先排序，然后缩小间距再排序
 */
public class ShellSort extends AbstractSort {
    @Override
    public void sort(Comparable[] a) {
        int N = a.length;
        int h = 1;
        while (h < N / 3) {
            h = 3 * h + 1;
        }

        while (h >= 1) {
            for (int i = h; i < N; i++) {
                //符合比前一个大的条件就可以终止了，因为前面的已经排好了
                for (int j = i; j >= h && less(a[j], a[j - h]); j = j - h) {
                    exch(a, j, j - h);
                }
            }
            h = h / 3;
        }
    }
}
