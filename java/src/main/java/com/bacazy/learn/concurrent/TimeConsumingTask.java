package com.bacazy.learn.concurrent;

import java.util.Random;


public class TimeConsumingTask implements Runnable{
    private boolean toCancel = false;
    Random random = new Random();
    public void run() {
        while (!toCancel){
            if (doExecute()){
                break;
            }
        }
        if (toCancel){
            System.out.println("Task was canceled");
        }else {
            System.out.println("Task done.");
        }
    }

    private boolean doExecute() {
        boolean isDone = false;
        System.out.println("executing......");
        try {

            Thread.sleep(random.nextInt(100));
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        return isDone;
    }

    public void cancel() {
        toCancel = true;
        System.out.println(this + "canceled.");
    }
}
