package com.bacazy.learn.math;

public class ReverseInteger {
    public int reverse(int x) {
        int result = 0;
        int newV = 0;
        int t = x > 0 ? x : -x;
        boolean positive = x > 0;
        while (t > 0) {
            newV = result * 10 + t % 10;
            if(newV > Integer.MAX_VALUE ){
                return 0;
            }
            result = newV;
            t = t / 10;
        }

        return positive ? result : -result;
    }
}
