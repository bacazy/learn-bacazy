package com.bacazy.learn.search;


public class Search {
    /**
     * 二分查找
     * @param array 数组
     * @param target 目标值
     * @return 目标值的索引
     */
    public int binarySearch(int[] array, int target){
        int lo = 0;
        int hi = array.length - 1;
        while (lo <= hi){
            int mid = lo + (hi - lo)/2;
            int m = array[mid];
            if (m == target){
                return mid;
            }
            if (m < target){
                lo = mid + 1;
            }else {
                hi = mid - 1;
            }
        }
        return -1;
    }
}
