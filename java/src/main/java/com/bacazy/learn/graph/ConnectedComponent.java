package com.bacazy.learn.graph;

/**
 * 连通分量，在无向图中，如果从顶点vi到顶点vj有路径，则称vi和vj连通。
 * 如果图中任意两个顶点之间都连通，则称该图为连通图，否则，称该图为非连通图，
 * 则其中的极大连通子图称为极大连通分量，这里所谓的极大是指子图中包含的顶点个数极大。
 */
public class ConnectedComponent {
    public boolean[] marked;
    private int[] id;
    private int count;

    public ConnectedComponent(AbstractGraph G) {
        marked = new boolean[G.V()];
        id = new int[G.V()];
        count = 0;
        for (int i = 0; i < G.V(); i++) {
            if (!marked[i]){
                dfs(G, i);
                count++;
            }
        }
    }

    private void dfs(AbstractGraph G, int s) {
        marked[s] = true;
        id[s] = count;
        for (int w : G.adj(s)){
            if (!marked[w]){
                dfs(G,w);
            }
        }
    }

    public boolean connected(int v,int w){
        return id[v] == id[w];
    }

    public int id(int v){
        return id[v];
    }

    public int count(){
        return count;
    }
}
