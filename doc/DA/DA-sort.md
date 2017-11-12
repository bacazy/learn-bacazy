# 算法-排序算法

## 各种排序算法特征
| 算    法  |  稳定性    |  时间复杂度  |  空间复杂度  | 
| :------: | :--------: |  :--------: |  :--------: |  
| 选择排序 | 不稳定 | N^2 | 1 | 
| 插入排序 | 稳定 | N和N^2之间 | 1 | 
| 希尔排序 | 不稳定 | NlogN | 1 | 
| 快速排序 | 不稳定 | NlogN | logN | 
| 三向切分快速排序 | 不稳定 | N和NlogN之间 | logN | 
| 归并排序 | 稳定 | NlogN | N | 
| 堆排序 | 不稳定 | NlogN | 1 | 

使用统一模板：
```java
public abstract class AbstractSort{
    protected boolean less(Comparable v, Comparable w){
        return v.compareTo(w) < 0;
    }
    protected void exch(Comparable[] a, int i,int j){
        Comparable t = a[i];
        a[i] = a[j];
        a[j] = t;
    }
    protected void print(Comparable[] a){
        System.out.println(Arrays.toString(a));
    }
    public boolean isSorted(Comparable[] a){
        for (int i = 0; i < a.length - 1; i++) {
            if (less(a[i+1],a[i])){
                return false;
            }
        }
        return true;
    }
    abstract void sort(Comparable[] a);
}
```

## 选择排序
### 算法思想
在未排序的部分中，每次将最小的元素与第一个元素交换，逐步后移，直至完成全部排序

### 代码实现
```java
public class SelectionSort extends AbstractSort {
    @Override
    public void sort(Comparable[] a) {
        for (int i = 0; i < a.length-1; i++) {
            Comparable min = a[i];
            int mindex = i;
            for (int j = i+1; j < a.length; j++) {
                if (less(a[j],min)){
                    mindex = j;
                    min = a[j];
                }
            }
            exch(a,i,mindex);
        }
    }
}
```

## 插入排序
### 算法思想
将数组分成两部分，一部分是排好顺序的，一部分是乱序的，每次将乱序中元素插入有序部分中的合适位置，直到全部有序。

### 代码实现
```java
public class InsertionSort extends AbstractSort {
    @Override
    public void sort(Comparable[] a) {
        for (int i = 1; i < a.length; i++) {
            int j = i;
            while (j - 1 >= 0){
                if (less(a[j],a[j-1])){
                    exch(a,j,j-1);
                }else {
                    break;
                }
                j--;
            }
        }
    }
}
```

## 希尔排序
### 算法思想
使得任意间隔为k的元素都是有序的。使用插入排序算法将k序数组单独排序，改变增量使得整个数组有序。
### 代码实现
```java
public class ShellSort extends AbstractSort {
    @Override
    public void sort(Comparable[] a) {
        int N = a.length;
        int h = 1;
        while (h < N /3){
            h = 3*h + 1;
        }

        while (h >= 1){
            for (int i = h; i < N; i++) {
                //符合比前一个大的条件就可以终止了，因为前面的已经排好了
                for (int j = i; j >=h && less(a[j],a[j-h]); j = j-h) {
                    exch(a,j,j-h);
                }
            }
            h = h / 3;
        }
    }
}
```

## 快速排序
### 算法思想
选取某个元素为参照，将比他小的部分放在前面，比他大的部分放在后面，然后分部分再进行xian共同的处理，便可以完成全部的数组排序。
### 代码实现
```java
public class QuickSort extends AbstractSort {
    @Override
    public void sort(Comparable[] a) {
        sort(a, 0 , a.length - 1);
    }

    private void sort(Comparable[] a, int lo, int hi) {
        if (lo >= hi){
            return;
        }
        int lt = lo;
        int gt = hi;
        int index = lo + 1;
        Comparable pival = a[lo];
        while (index <= gt){
            int cmp = a[index].compareTo(pival);
            if (cmp > 0){
                exch(a,index,gt);
                gt--;
                while (gt >= index && less(pival,a[gt])){
                    gt--;
                }
            }else {
                exch(a,index,lt);
                lt++;
                index++;
            }
        }
        sort(a,lo, gt - 1);
        sort(a, gt + 1, hi);
    }
}
```

## 三向切分快速排序算法
### 算法思想
与快速排序类似，这里考虑到重复元素对性能的影响，将与参照元素相等的元素放在数组的中段，小于参照元素的部分放在前段，大于参照元素的部分放在后段，然后分别在前段和后段进行相同的操作即可，不需要考虑中间段的部分。
### 代码实现
```java
public class QuickThreeWaySort extends AbstractSort {
    @Override
    void sort(Comparable[] a) {
        sort(a,0,a.length-1);
    }
    private void sort(Comparable[] a, int lo, int hi) {
        if (lo >= hi){
            return;
        }
        int lt = lo;
        int gt = hi;
        int index = lo + 1;
        Comparable pival = a[lo];
        while (index <= gt){
            int cmp = a[index].compareTo(pival);
            if (cmp > 0){
                exch(a,index,gt);
                gt--;
                //可不加下面语句，但可以提高效率，减少交换次数
                while (gt > index && less(pival,a[gt])){
                    gt--;
                }
            }else if (cmp < 0){
                exch(a,lt,index);
                lt++;
                index++;
            }else {
                index++;
            }
        }
        sort(a,lo, lt-1);
        sort(a,gt + 1,hi);
    }
}
```

## 归并排序
### 算法思想
将两个有序的数组归并到一个数组中。有两种实现方法，一种是自上而下基于递归实现，一种是自下而上更改子数组大小的方法实现（1，2，4，...）。
### 算法实现
```java
public class MergeSort extends AbstractSort {
    private Comparable[] aux;
    @Override
    void sort(Comparable[] a) {
        aux = new Comparable[a.length];
        sort(a,0,a.length-1);
    }

    private void sort(Comparable[] a, int low, int high) {
        if (high <= low) {
            return;
        }
        int mid = low + (high-low)/2;//求平均值方法，避免求和溢出
        sort(a,low,mid);
        sort(a,mid + 1,high);
        merge(a,low,mid,high);
    }

    private void merge(Comparable[] a, int low, int mid, int high) {
        System.arraycopy(a, low, aux, low, high + 1 - low);
        int first = low;
        int sec = mid + 1;
        for (int i = low; i <= high; i++) {
            if (first > mid){
                a[i] = aux[sec];
                sec++;
            }else if (sec > high){
                a[i] = aux[first];
                first++;
            }else if (less(a[first],a[sec])){
                a[i] = a[first];
                first++;
            }else {
                a[i] = a[sec];
                sec++;
            }
        }
    }
}
```

## 堆排序
### 算法思想
利用完全二叉树建立大顶堆，然后将堆顶元素与最后一个元素交换，那么最后一个元素就是最大的，将最后一个元素排除在外，再进行调整形成新的大顶堆，如此周而复始，完成所有元素的排序过程。
完全二叉树有n个元素，那么第一个非叶子节点的下标是(n-2)/2，从它开始，依次向0，惊醒调整。调整的策略是，与孩子节点中的较大元素交换（比他小的时候），直到叶子节点为止。
### 代码实现
```java
public class HeapSort extends AbstractSort {
    @Override
    void sort(Comparable[] a) {
        int N = a.length;
        for (int k = (N-2) / 2;k >= 0;k--){
            sink(a,k,N);
        }
        while (N > 0){
            exch(a,0,--N);
            sink(a,0,N);
        }
    }

    private void sink(Comparable[] a, int k, int n) {
        while (2*(k + 1) <= n){
            int j = 2 * k + 1;
            if (j < n-1 && less(a[j],a[j+1])){
                j++;
            }
            if (less(a[k],a[j])){
                exch(a,k,j);
                k = j;
            }else {
                break;
            }
        }
    }
}
```

## 总结

排序算法的改进主要思想就是将数组分成两个或者多个部分分别进行排序，各种性能较好的算法分区的方式不一样，分区之后需要比较的元素个数就降低了，那么就可以提高算法的效率。
快速排序算法跟据参照元素大小分成两部分，希尔排序根据增量分成多个部分，归并排序两个有序数组归并成一个数组，每个子数组为一部分，堆排序是利用树的结构特点，可以看作是将数组分成从叶子节点上行到根节点为一部分的多个分区。