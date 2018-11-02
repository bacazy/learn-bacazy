package com.bacazy.learn.math;

import org.junit.Test;

import static org.junit.Assert.*;

public class ReverseIntegerTest {

    @Test
    public void reverse() {
        ReverseInteger instance = new ReverseInteger();
        assertEquals(instance.reverse(1534236469), 0);
        assertEquals(instance.reverse(110), 11);
        assertEquals(instance.reverse(120), 21);
        assertEquals(instance.reverse(-120), -21);
    }
}