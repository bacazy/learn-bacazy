package com.bacazy.learn.concurrent;

import java.util.concurrent.Executor;

/**
 * Join使用案例
 */
public class JoinUsageCase implements Runnable {
    public void run() {
        print("ss");
        try {
            Thread.sleep(6000);//模拟耗时6s的任务
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        print("se");
    }

    private static void print(String msg) {
        System.out.print(msg + " ");
    }

    public static void main(String[] args) throws InterruptedException {
        print("ms");

        Thread sub = new Thread(new JoinUsageCase());
        sub.start();//启动子线程
        sub.join(1000);//在主线程中调用子线程的join方法，等待子线程结束再继续执行
        print("me");
    }
}
