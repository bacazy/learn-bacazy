package com.bacazy.nn;


import java.util.ArrayList;

public abstract class AbstractNeuroGraph implements NeuroGraph {
    ArrayList<double[][]> weights = new ArrayList<double[][]>();
    ArrayList<Neuro[]> layers = new ArrayList<Neuro[]>();

    public NeuroGraph addLayer(Neuro[] neuros) {
        layers.add(neuros);
        if (layers.size() > 1){
            double[][] ws = new double[layers.get(layers.size() - 2).length][neuros.length];
            weights.add(ws);
        }
        return this;
    }


}
