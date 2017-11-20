package com.bacazy.learn.search;

import junit.framework.TestCase;

import java.util.Arrays;
import java.util.Random;

public class BSTTest extends TestCase {
    BST<Integer,Integer> bst = null;
    static Random random = new Random();
    int[] list = null;
    int size = 0;
    private final static int SIZE = 100;

    public void setUp() throws Exception {
        super.setUp();
        size = 0;
        bst = new BST<Integer, Integer>();
        list = new int[SIZE];
        for (int i = 0; i < SIZE; i++) {
            int key = random.nextInt(SIZE * 3);
            bst.put(key,random.nextInt(SIZE * 3));
            list[i] = key;
        }
        Arrays.sort(list);
        int[] ne = new int[SIZE];
        ne[0] = list[0];
        size++;
        for (int i = 1; i < SIZE; i++) {
            if (list[i] == list[i-1]){
                continue;
            }
            ne[size] = list[i];
            size++;
        }
        list = new int[size];
        for (int i = 0; i < size; i++) {
            list[i]  = ne[i];
        }
    }

    public void testMin() throws Exception {
        assertEquals((int)bst.min(),list[0]);
    }

    public void testMax() throws Exception {
        assertEquals((int)bst.max(),list[size-1]);
    }

    public void testFloor() throws Exception {
        int a = 0;
        for (int i : list){
            if (a == 0 || list[a-1] == list[a] - 1){
                a++;
                continue;
            }
            a++;
            assertEquals(i,(int) bst.ceiling(i-1));
        }
    }

    public void testCeiling() throws Exception {

    }

    public void testRank() throws Exception {
        for (int i = 0; i < list.length; i++) {
            assertEquals(i , bst.rank(list[i]));
        }
    }

    public void testSelect() throws Exception {
        for (int i = 0; i < list.length; i++) {
            assertEquals((Integer)list[i] , bst.select(i));
        }
    }

    public void testDeleteMin() throws Exception {

    }

    public void testDeleteMax() throws Exception {

    }

    public void testSize() throws Exception {
        Iterable<Integer> keys = bst.keys();
        int i = 0;

        for (int k:keys){
            i++;
        }
        if (size != i){
            System.out.println("cuol");
        }
    }

    public void testKeys() throws Exception {

    }

    public void testValues() throws Exception {

    }

    public void testPut() throws Exception {

    }

    public void testGet() throws Exception {

    }

    public void testDelete() throws Exception {

    }

    public void testContains() throws Exception {

    }

    public void testIsEmpty() throws Exception {

    }

    public void testSize1() throws Exception {

    }

    public void testKeys1() throws Exception {

    }

    public void testValues1() throws Exception {

    }
}