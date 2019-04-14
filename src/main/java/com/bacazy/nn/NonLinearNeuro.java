package com.bacazy.nn;


public class NonLinearNeuro extends Neuro{

    private ActivateFunc activateFunc;

    public NonLinearNeuro(ActivateFunc activateFunc) {
        this.activateFunc = activateFunc;
    }

    @Override
    public double update() {
        return activateFunc.activate(getResult());
    }
}
