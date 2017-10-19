package com.bacazy.test.qunar.c;


import java.util.HashMap;
import java.util.LinkedList;
import java.util.Scanner;


public class Main {
    static HashMap<String, String> set = new HashMap<String, String>();
    static int size = 0;
    static int capacity = 10;
    static LinkedList<String> keys = new LinkedList<String>();

    static void put(String key, String value) {
        if (set.containsKey(key)) {
            set.put(key, value);
            keys.remove(keys.indexOf(key));
            keys.addFirst(key);
        } else {
            keys.addFirst(key);
            set.put(key, value);
            if (size == capacity) {
                String k = keys.removeLast();
                set.remove(k);
            } else {
                size++;
            }
        }
    }

    static void get(String key) {
        if (set.containsKey(key)) {
            keys.remove(keys.indexOf(key));
            keys.addFirst(key);
            System.out.println(set.get(key));
        } else {
            System.out.println("null");
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        capacity = scanner.nextInt();
        int n = scanner.nextInt();
        scanner.nextLine();
        for (int i = 0; i < n; i++) {
            String line = scanner.nextLine();
            if (line.startsWith("put")) {
                String[] kv = line.substring(4).split(" ");
                put(kv[0], kv[1]);
            } else {
                String[] k = line.split(" ");
                get(k[1]);
            }
        }
    }

}
