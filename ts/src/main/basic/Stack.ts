

export class Stack<T> {
    list: T[] = [];
    length: number = 0;
    pop(): T {
        if (this.length === 0) {
            throw "out of bounds of stack";
        }
        else return this.list.pop();
    }

    push(e: T): void {
        this.list.push(e);
    }
}