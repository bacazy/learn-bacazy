package com.bacazy.service.newcoder;


import java.util.LinkedList;

public class OperateSequence {
    static int[] operate(int[] array) {
        int i = 0;
        boolean reverse = false;
        LinkedList<Integer> list = new LinkedList<Integer>();
        while (i < array.length) {
            if (reverse) {
                list.addFirst(array[i]);
            } else {
                list.addLast(array[i]);
            }
            reverse = !reverse;
            i++;
        }
        int[] nAs = new int[array.length];


        return nAs;
    }
}
