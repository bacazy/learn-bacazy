package com.bacazy.learn.concurrent;

import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReadWriteLock;
import java.util.concurrent.locks.ReentrantReadWriteLock;

/**
 * Created by gc_zc on 2017/11/22.
 */
public class ReadWriteLockUsage {
    private final ReadWriteLock readWriteLock = new ReentrantReadWriteLock();
    private final Lock readLock = readWriteLock.readLock();
    private final Lock writeLock = readWriteLock.writeLock();

    public void read(){
        readLock.lock();
        try {
            //在此处读取共享变量
        }finally {
            readLock.unlock();
        }
    }

    public void write(){
        writeLock.lock();
        try {
            //在此处读写共享变量
        }finally {
            writeLock.unlock();
        }
    }
}
