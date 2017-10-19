package com.bacazy.service.datastructure.sort;


/**
 * 排序算法
 */
public class Sort {

    /**
     * 选择排序
     * 每次选择最小的元素放在前面
     */
    public static int[] selectionSort(int[] array) {
        for (int i = 0; i < array.length; i++) {
            int min = array[i];
            int minIndex = i;
            for (int j = i + 1; j < array.length; j++) {
                if (min > array[j]) {
                    min = array[j];
                    minIndex = j;
                }
            }
            array[minIndex] = array[i];
            array[i] = min;
        }
        return array;
    }

    /**
     * 插入排序
     * 将记录插入到一个排好序的有序表中
     * 时间：n^2
     * 空间：1
     */
    public static int[] insertionSort(int[] array) {
        for (int i = 1; i < array.length; i++) {
            int e = array[i];
            int j = i;
            while (j > 0 && (array[j - 1] > e)) {
                array[j] = array[j - 1];
                j--;
            }
            array[j] = e;
        }
        return array;
    }

    /**
     * 希尔排序
     */
    public static int[] shellSort(int[] array) {
        int i;
        int j;
        int gap;
        for (gap = array.length / 3; gap > 0; gap /= 3) {
            for (i = gap; i < array.length; i++) {
                for (j = i - gap; j >= 0 && array[j] > array[j + gap]; j -= gap) {
                    int jv = array[j + gap];
                    array[j + gap] = array[j];
                    array[j] = jv;
                }
            }
        }
        return array;
    }

    /**
     * 归并排序
     */
    public static int[] mergingSort(int[] array) {
        int section = 1;
        int[] as = null;
        while (section < array.length) {
            as = new int[array.length];


            array = as;
            section = section * 2;
        }
        return array;
    }

    /**
     * 快速排序
     */
    public static int[] quickSort(int[] array) {

        return array;
    }

    /**
     * 堆排序
     */
    public static int[] heapSort(int[] array) {
        return array;
    }

    /**
     * 基数排序
     */
    public static int[] radixSort(int[] array) {
        return array;
    }


}
