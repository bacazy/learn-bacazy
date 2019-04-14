package com.bacazy.nn;

public abstract class Neuro {
    private double result = 0;

    public abstract double update();

    public double getResult() {
        return result;
    }

    public void setResult(double result) {
        this.result = result;
    }
}
