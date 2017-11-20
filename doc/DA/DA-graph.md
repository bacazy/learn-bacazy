# 数据结构-图
## 无向图
API：
```java
public interface Graph {
    int V();//顶点数
    int E();//边数
    void addEdge(int v, int w);//添加从v到w的边
    Iterable<Integer> adj(int v);//返回v的邻接顶点
}
```

```java
public abstract class AbstractGraph implements Graph {
    protected int V = 0;
    protected int E = 0;
    public AbstractGraph(int v) { V = v; }
    public int V() {return V;}
    public int E() { return E; }
    public int degree(int v){//度
        int degree = 0;
        for (int w: adj(v)){  degree ++; }
        return degree;
    }

    public int maxDegree(){//最大度
        int max = 0;
        for (int i = 0; i < V(); i++) {
            if (degree(i) > max){ max = degree(i);}
        }
        return max;
    }

    public double avgDegree(){//平均度
        return 2.0 * E() / V();
    }

    public int numberOfSelfLoops(){//自环个数
        int count = 0;
        for (int v = 0; v < V(); v++) {
            for (int w : adj(v)) {if (v == w){ count++;}}
        }
        return count / 2;//重复计算了
    }
}
```

数组表示法：用二维数组表示一幅图，(i,j) > 0表明存在一条从i到j的边，否则不存在
```java
public class MatrixGraph extends AbstractGraph {
    private int[][] G;
    public MatrixGraph(int v) { super(v);}
    public void addEdge(int v, int w) {
        G[v][w] ++;
        G[w][v] ++;
        E++;
    }
    public Iterable<Integer> adj(int v) {
        List<Integer> adjs = new ArrayList<Integer>();
        for (int i = 0; i < V; i++) {
            if (G[v][i] > 0){ adjs.add(i);}
        }
        return adjs;
    }
}
```

邻接链表表示法: 用V个链表存储与v相邻接的顶点，所需的空间为V+E
```java
public class AdjListGraph extends AbstractGraph {
    private List<Integer>[] G;
    public AdjListGraph(int v) {
        super(v);
        G = (List<Integer>[]) new AdjListGraph[v];
        for (int i = 0; i < v; i++) {G[i] = new ArrayList<Integer>();}
    }
    public void addEdge(int v, int w) {
        G[v].add(w);
        G[w].add(v);
        E++;
    }
    public Iterable<Integer> adj(int v) {return G[v];}
}
```
图的搜索：
```java
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
```
深度优先搜索：
```java
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
        for (int w: G.adj(v)){
            if (!marked[w]){
                dfs(w);
            }
        }
    }
    @Override
    public boolean marked(int v) {
        return marked[v];
    }
    @Override
    public int count() {
        return count;
    }
}
```
