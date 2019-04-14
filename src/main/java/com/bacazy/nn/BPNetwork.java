package com.bacazy.nn;

import java.util.Random;

public class BPNetwork extends AbstractNeuroGraph {

    public BPNetwork(int[] layers) {
        for (int l : layers) {
            Neuro[] neuros = new Neuro[l];
            addLayer(neuros);
        }
        int layer = 0;
        for (Neuro[] neuros : this.layers) {
            for (int i = 0; i < neuros.length; i++) {
                if (layer == 0) {
                    neuros[i] = new NonLinearNeuro(new SigmoidActivateFunc());
                } else {
                    neuros[i] = new NonLinearNeuro(new PassbyFunc());
                }
            }
            layer++;
        }
    }

    public NeuroGraph train(double[][] trainData, double[][] expect, float learn_rate, int epochs) {
        init_weights();
        int epoch = 0;
        while (epoch++ < epochs) {
            double err = 0;
            for (double[] x : trainData) {
                setInputLayer(x);

//                计算各层输出
                for (int i = 1; i < layers.size(); i++) {
                    for (int j = 0; j < this.layers.get(i).length; j++) {
                        double sum = 0;
                        for (int k = 0; k < this.layers.get(i-1).length; k++) {
                            sum = sum + weights.get(i-1)[j][k] * this.layers.get(i-1)[k].getResult();
                        }
                        this.layers.get(i)[j].setResult(sum);
                        this.layers.get(i)[j].update();
                    }
                }
                // 计算误差
                err += computeError(expect);

                updateWeights(learn_rate, expect);

            }
            err = err/trainData.length;
            System.out.println("epoch:" + epoch + "\t Error:" +err);
        }

        return null;
    }

    private void updateWeights(float learn_rate, double[][] expect) {
        
    }

    private double computeError(double[][] expect) {

        return 0;
    }

    private void setInputLayer(double[] x) {
        Neuro[] layer = layers.get(0);
        for (int i = 0; i < x.length; i++) {
            layer[i].setResult(x[i]);
        }
    }

    private void init_weights() {
        Random random = new Random();
        for (double[][] ws : weights) {
            for (int i = 0; i < ws.length; i++) {
                for (int j = 0; j < ws[i].length; j++) {
                    ws[i][j] = random.nextDouble() / 100;
                }
            }
        }
    }

    public double[] predict(double[] input) {
        return new double[0];
    }
}
