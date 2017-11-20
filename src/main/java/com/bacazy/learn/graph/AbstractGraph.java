package com.bacazy.learn.graph;

import java.io.InputStream;

public abstract class AbstractGraph implements Graph {
    protected int V = 0;
    protected int E = 0;

    public AbstractGraph(int v) {
        V = v;
    }

    public AbstractGraph(InputStream in) {
        construct(in);
    }

    public int V() {
        return V;
    }

    public int E() {
        return E;
    }

    protected abstract void construct(InputStream in);

    public int degree(int v){
        int degree = 0;
        for (int w: adj(v)){
            degree ++;
        }
        return degree;
    }

    public int maxDegree(){
        int max = 0;
        for (int i = 0; i < V(); i++) {
            if (degree(i) > max){
                max = degree(i);
            }
        }
        return max;
    }

    public double avgDegree(){
        return 2.0 * E() / V();
    }

    public int numberOfSelfLoops(){
        int count = 0;
        for (int v = 0; v < V(); v++) {
            for (int w : adj(v)) {
                if (v == w){
                    count++;
                }
            }
        }
        return count / 2;
    }
}
