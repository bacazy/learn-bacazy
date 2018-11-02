package com.bacazy.learn.string;

import org.junit.Test;

import static org.junit.Assert.*;


public class ZigZagTest {

    @Test
    public void convert() throws Exception{
        ZigZag zigZag = new ZigZag();
        assertEquals(zigZag.convert("PAYPALISHIRING", 3), "PAHNAPLSIIGYIR");
        assertEquals(zigZag.convert("PAYPALISHIRING", 4), "PINALSIGYAHRPI");
    }
}