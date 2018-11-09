interface Node<T> {
    value: T;
    prev: Node<T>,
    next: Node<T>
}

export class LinkedList<T> {
    head: Node<T> = {prev: null, next: null, value: null};
    length:number = 0;
    
}