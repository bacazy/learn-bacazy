package com.bacazy.learn.sort;


import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class SortBenchmark {
    List<AbstractSort> sorts = new ArrayList<AbstractSort>();
    List<Integer> testArraySize = new ArrayList<Integer>();
    Random random = new Random();

    public void addSortMethod(AbstractSort sort) {
        sorts.add(sort);
    }

    private Integer[] nextArray(int size) {
        if (size <= 0) {
            return null;
        }
        Integer[] array = new Integer[size];
        for (int i = 0; i < array.length; i++) {
            array[i] = random.nextInt(10000);
        }
        return array;
    }

    public void addTestArraySize(int size) {
        testArraySize.add(size);
    }

    public void test() {

        long t = System.currentTimeMillis();
        System.out.print("ArraySize\t\t\t");
        for (int s : testArraySize) {
            System.out.print("\t\t");
            System.out.print(s);
        }
        System.out.println();
        for (AbstractSort sort : sorts) {
            test(sort);
        }
        double ti = 0.001 * (System.currentTimeMillis() - t);
        System.out.println("use :" + ti + "s");
    }

    private void test(AbstractSort sort) {
        long time = 0;
        System.out.printf("%s\t", sort.getClass().getSimpleName());

        for (int size : testArraySize) {
            time = 0;
            for (int i = 0; i < 10; i++) {
                Integer[] array = nextArray(size);
                Integer[] newA = array.clone();
                sort.sort(newA);
                assert sort.isSorted(newA);
                long t = System.currentTimeMillis();
                for (int j = 0; j < 100; j++) {
                    sort.sort(array.clone());
                }
                time = time + System.currentTimeMillis() - t;
            }
            System.out.printf("\t\t%d", time);
        }
        System.out.println();
    }
}
