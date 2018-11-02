package com.bacazy.learn.graph;

import java.io.InputStream;
import java.util.ArrayList;
import java.util.List;

/**
 * 矩阵表示的图
 */
public class MatrixGraph extends AbstractGraph {
    private int[][] G;
    public MatrixGraph(int v) {
        super(v);
    }
    public MatrixGraph(InputStream in) {
        super(in);
    }
    public void addEdge(int v, int w) {
        G[v][w] ++;
        G[w][v] ++;
        E++;
    }
    public Iterable<Integer> adj(int v) {
        List<Integer> adjs = new ArrayList<Integer>();
        for (int i = 0; i < V; i++) {
            if (G[v][i] > 0){
                adjs.add(i);
            }
        }
        return adjs;
    }
    @Override
    protected void construct(InputStream in) {

    }
}
