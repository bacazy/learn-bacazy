package com.bacazy.learn.graph;



import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

public class BreadthFirstPaths extends Paths {
    private boolean[] marked;
    private int[] edgeTo;

    public BreadthFirstPaths(int source, AbstractGraph g) {
        super(source, g);
        marked = new boolean[G.V()];
        edgeTo = new int[G.V()];
        bfs(source);
    }

    private void bfs(int v) {
        List<Integer> list = new ArrayList<Integer>();
        marked[v] = true;
        list.add(v);
        while (list.size() > 0){
            int w = list.get(list.size() - 1);
            list.remove(list.size() - 1);
            for (int n : G.adj(w)){
                if (!marked[n]){
                    edgeTo[n] = w;
                    marked[n] = true;
                    list.add(n);
                }
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
