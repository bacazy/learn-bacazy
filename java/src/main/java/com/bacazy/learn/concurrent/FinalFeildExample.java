package com.bacazy.learn.concurrent;


public class FinalFeildExample implements Runnable{
    final int x;
    int y;

    static FinalFeildExample instance;

    public FinalFeildExample() {
        x=1;
        y=2;
    }

    public static void writer(){
        instance = new FinalFeildExample();
    }

    public static void reader(){
        final FinalFeildExample theInstance = instance;
        if (theInstance != null){
            int diff = theInstance.y - theInstance.x;
            System.out.println(diff);
        }
    }

    public static void main(String[] args){
        int tns = 1000;
        Thread[] ts = new Thread[tns];
        for (int i = 0; i < tns; i++) {
            ts[i] = new Thread(new FinalFeildExample());
        }

        int a = 0;
        for (Thread t:ts){
            t.start();
            if (a == 4){
                writer();
            }
            a++;
        }
    }

    public void run() {

    }
}
