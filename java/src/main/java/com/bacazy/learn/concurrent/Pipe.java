package com.bacazy.learn.concurrent;


import java.util.Queue;
import java.util.concurrent.LinkedBlockingDeque;

public class Pipe<T> {
    Queue<T> queue = new LinkedBlockingDeque<T>();

}
