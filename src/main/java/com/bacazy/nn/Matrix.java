package com.bacazy.nn;


import java.util.ArrayList;
import java.util.List;

public class Matrix<T> {
    T[] array = null;
    List<Integer> shape= new ArrayList<Integer>();

    public int[] shape(){
        int[] sa = new int[shape.size()];
        for (int i = 0; i < sa.length; i++) {
            sa[i] = shape.get(i);
        }
        return sa;
    }

    public int dim(){
        return shape.size();
    }


}
