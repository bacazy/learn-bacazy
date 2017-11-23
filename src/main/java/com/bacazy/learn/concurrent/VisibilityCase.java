package com.bacazy.learn.concurrent;


public class VisibilityCase {
    public static void main(String[] args){
        TimeConsumingTask timeConsumingTask = new TimeConsumingTask();
        Thread thread = new Thread(timeConsumingTask);
        thread.start();
        System.out.println(VisibilityCase.class.getName());
        try {
            Thread.sleep(10000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        timeConsumingTask.cancel();
    }
}
