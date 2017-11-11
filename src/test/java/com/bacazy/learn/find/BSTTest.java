package com.bacazy.learn.find;

import junit.framework.TestCase;

import java.util.Arrays;
import java.util.Random;

public class BSTTest extends TestCase {
    BST<Integer,Integer> bst = null;
    static Random random = new Random();
    int[] list = null;
    int size = 0;

    public void setUp() throws Exception {
        super.setUp();
        size = 0;
        bst = new BST<Integer, Integer>();
        list = new int[100];
        for (int i = 0; i < 100; i++) {
            int key = random.nextInt(200);
            bst.put(key,random.nextInt(200));
            list[i] = key;
        }
        Arrays.sort(list);
        int[] ne = new int[100];
        ne[0] = list[0];
        size++;
        for (int i = 1; i < 100; i++) {
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

    }

    public void testCeiling() throws Exception {

    }

    public void testRank() throws Exception {

    }

    public void testSelect() throws Exception {

    }

    public void testDeleteMin() throws Exception {

    }

    public void testDeleteMax() throws Exception {

    }

    public void testSize() throws Exception {
        Iterable<Integer> keys = bst.keys();
        int i = 0;
        for (int k:keys){
            System.out.printf("%d ", k);
            System.out.println(list[i++]);
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