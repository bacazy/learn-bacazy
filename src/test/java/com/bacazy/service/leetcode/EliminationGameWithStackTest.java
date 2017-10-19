package com.bacazy.service.leetcode;

import junit.framework.TestCase;

/**
 * Created by ZhangCheng on 2017/10/17.
 */
public class EliminationGameWithStackTest extends TestCase {

    public void testLastRemaining() throws Exception {
        assertEquals(6, new EliminationGameWithStack().lastRemaining(9));
    }
}