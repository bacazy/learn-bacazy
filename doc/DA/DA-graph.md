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

