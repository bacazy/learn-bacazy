package com.bacazy.learn.search;

import junit.framework.TestCase;


public class SearchTest extends TestCase {

    public void testBinarySearch() throws Exception {
        assertEquals(new Search().binarySearch(new int[]{1,2,5,7,11,15,19,25,35,36,78}, 19),6);
        assertEquals(new Search().binarySearch(new int[]{1,2,5,7,11,15,19,25,35,36,78}, 13),-1);
    }
}