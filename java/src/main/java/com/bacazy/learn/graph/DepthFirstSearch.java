package com.bacazy.learn.graph;


public class DepthFirstSearch extends Search {
    private boolean[] marked;
    private int count = 0;

    public DepthFirstSearch(AbstractGraph G, int source) {
        super(G, source);
        marked = new boolean[G.V()];
        dfs();
    }

    private void dfs() {
        dfs(source);
    }

    private void dfs(int v) {
        marked[v] = true;
        count++;
        for (int w : G.adj(v)) {
            if (!marked[w]) {
                dfs(w);
            }
        }
    }

    public boolean marked(int v) {
        return marked[v];
    }

    public int count() {
        return count;
    }
}
