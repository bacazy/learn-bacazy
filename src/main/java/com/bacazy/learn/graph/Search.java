package com.bacazy.learn.graph;

public abstract class Search {
    /**
     * 源顶点
     */
    protected int source;
    /**
     * 图
     */
    protected AbstractGraph G;

    public Search(AbstractGraph G, int source) {
        this.source = source;
        this.G = G;
    }

    /**
     * 判断v 和 source是否连通
     * @param v 目的顶点
     * @return v 和 source是否连通
     */
    public abstract boolean marked(int v);

    /**
     * 与source连通的顶点总数
     * @return 与source连通的顶点总数
     */
    public abstract int count();
}
