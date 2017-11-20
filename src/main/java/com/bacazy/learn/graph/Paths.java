package com.bacazy.learn.graph;


public abstract class Paths {
    protected int source;
    protected AbstractGraph G;

    public Paths(int source, AbstractGraph g) {
        this.source = source;
        G = g;
    }

    /**
     * 是否存在从source到v的路径
     * @param v 目的顶点
     * @return 是否存在从source到v的路径
     */
    abstract boolean hasPathTo(int v);

    /**
     * 从source到v的路径
     * @param v 目的顶点
     * @return 从source到v的路径，不存在，则返回null
     */
    abstract Iterable<Integer> pathTo(int v);
}
