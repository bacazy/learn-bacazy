package com.bacazy.learn.graph;

/**
 * 无向图
 */
public interface Graph {
    int V();
    int E();
    void addEdge(int v, int w);
    Iterable<Integer> adj(int v);
}
