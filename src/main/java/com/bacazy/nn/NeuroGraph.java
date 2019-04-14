package com.bacazy.nn;


public interface NeuroGraph {
    NeuroGraph addLayer(Neuro[] neuros);
    NeuroGraph train(double[][] trainData, double[][] expect,float learn_rate, int epochs);
    double[] predict(double[] input);
}
