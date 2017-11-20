package com.bacazy.learn.graph;


import java.util.Stack;

public class DepthFirstPaths extends Paths{
    private boolean[] marked;
    private int[] edgeTo;


    public DepthFirstPaths(int source, AbstractGraph g) {
        super(source, g);
        marked = new boolean[G.V()];
        edgeTo = new int[G.V()];
        dfs(source);
    }

    private void dfs(int source) {
        marked[source] = true;
        for (int w : G.adj(source)){
            if (!marked[w]){
                edgeTo[w] = source;
                dfs(w);
            }
        }
    }

    @Override
    boolean hasPathTo(int v) {
        return marked[v];
    }

    @Override
    Iterable<Integer> pathTo(int v) {
        if (!hasPathTo(v)) {
            return null;
        }
        Stack<Integer> path = new Stack<Integer>();
        for (int i = v; i != source; i = edgeTo[i]) {
            path.push(i);
        }
        path.push(source);
        return path;
    }
}
