package com.bacazy.learn.concurrent;

import java.util.concurrent.locks.Lock;

/**
 * Created by gc_zc on 2017/11/22.
 */
public class TickCounter {
    static class Counter implements Runnable {
        public void run() {

            tick();
        }

        private void tick() {
            synchronized (this) {
                if (count > 100) {
                    count = 0;
                } else {
                    count = count + 1;
                }
                System.out.println("count: " + count);
            }
        }
        private Integer count=0;
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
