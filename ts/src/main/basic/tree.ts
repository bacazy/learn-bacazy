


class BinaryTreeNode<T> {
    left: BinaryTreeNode<T> = null;
    right: BinaryTreeNode<T> = null;
    value: Comparable<T> = null;

    setValue(value: Comparable<T>): void {
        this.value = value;
    }

    setRight(child: BinaryTreeNode<T>): void {
        this.right = child;
    }

    setLeft(child: BinaryTreeNode<T>): void {
        this.left = child;
    }
}


class BinaryTree<T> {
    node: BinaryTreeNode<T> = null;

    constructor(tree: BinaryTreeNode<T>){
        this.node = tree;
    }

    inorderTraverse(): BinaryTreeNode<T>[]{
        let seq:BinaryTreeNode<T>[] = [];
        this._inorderTraverse(this.node, seq);
        return seq;
    }

    _inorderTraverse(node:BinaryTreeNode<T>, seq:BinaryTreeNode<T>[]){
        if(node){
            seq.push(node);
            this._inorderTraverse(node.left, seq);
            this._inorderTraverse(node.right, seq);
        }
    }
}

