package com.bacazy.learn.graph;

/**
 * 无向图
 */
public interface Graph {
    int V();//顶点数
    int E();//边数
    void addEdge(int v, int w);//添加从v到w的边
    Iterable<Integer> adj(int v);//返回v的邻接顶点
}
