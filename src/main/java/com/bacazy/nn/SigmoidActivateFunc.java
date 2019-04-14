package com.bacazy.nn;

import static java.lang.Math.exp;

public class SigmoidActivateFunc implements ActivateFunc {
    public double activate(double x) {
        return 1.0 / (1 + exp(-x));
    }
}
