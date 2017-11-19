package com.bacazy.learn.java;

/**
 * find out the order of the members in Class
 */

class ClassParent{
    private String m1 = "parent m1";
    private static String m2 = "parent static m2";

    {
        m1 = "Parent m1";
        print();
    }

    static {
        System.out.println(m2);
    }

    public ClassParent(String m1) {
        this.m1 = m1;
        System.out.println("parent construtor:" + m1);
        System.out.println("parent construtor:" + m2);
    }

    public void print(){
        System.out.println("Parent:" + m1);
    }
}

public class InitialSequence extends ClassParent{

    private String m1 = "Child m1";
    private static String m2 = "Child static m2";

    {
        System.out.println("child block");
        print();
    }

    static {
        System.out.println("child static block");
        System.out.println(m2);
    }

    public InitialSequence(String m1) {
        super(m1);
    }
}
