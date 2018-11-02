package com.bacazy.learn.graph;

import java.io.InputStream;
import java.util.ArrayList;
import java.util.List;

/**
 * 连接表表示的图
 */
public class AdjListGraph extends AbstractGraph {

    private List<Integer>[] G;

    public AdjListGraph(InputStream in) {
        super(in);
    }

    public AdjListGraph(int v) {
        super(v);
        G = (List<Integer>[]) new AdjListGraph[v];
        for (int i = 0; i < v; i++) {
            G[i] = new ArrayList<Integer>();
        }
    }

    public void addEdge(int v, int w) {
        G[v].add(w);
        G[w].add(v);
        E++;
    }

    public Iterable<Integer> adj(int v) {
        return G[v];
    }

    @Override
    protected void construct(InputStream in) {

    }
}
