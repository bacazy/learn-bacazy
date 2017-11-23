package com.bacazy.learn.concurrent;

public class TickCounter {
    static class Counter implements Runnable {
        private Integer count=0;

        public void run() { tick(); }
        private void tick() {
            synchronized (count) {
                if (count > 100) {
                    count = 0;
                } else {
                    count = count + 1;
                }
                System.out.println("count: " + count);
            }
        }
    }

    public static void main(String[] args){
        int count = 5;
        Thread[] threads = new Thread[count];
        Counter counter = new Counter();
        for (int i = 0; i < count; i++) {
            threads[i] = new Thread(counter);
        }
        for (int i = 0; i < count; i++) {
            threads[i].start();
        }
    }
}