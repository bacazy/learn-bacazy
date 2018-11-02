package com.bacazy.quiz.aiqiyi.c;


class FourLeavesTreeNode {
    public Character value;
    public FourLeavesTreeNode aNode;
    public FourLeavesTreeNode gNode;
    public FourLeavesTreeNode tNode;
    public FourLeavesTreeNode cNode;

    public FourLeavesTreeNode(Character value) {
        this.value = value;
    }

    public FourLeavesTreeNode getChild(char c) {
        switch (c) {
            case 'A':
                return aNode;
            case 'G':
                return gNode;
            case 'T':
                return tNode;
            case 'C':
                return cNode;
        }
        return null;
    }

    public void setChild(char c, FourLeavesTreeNode node) {
        switch (c) {
            case 'A':
                aNode = node;
                break;
            case 'G':
                gNode = node;
                break;
            case 'T':
                tNode = node;
                break;
            case 'C':
                cNode = node;
                break;
        }
    }

    public boolean full() {
        return !(aNode == null || gNode == null || tNode == null || cNode == null);
    }
}

public class Main {
    public static void main(String[] args) {
//        Scanner in = new Scanner(System.in);
//        String str = in.nextLine();
        System.out.println(shortestUniqueSubString("AGGTTCTATGCAGTA"));
    }

    private static int shortestUniqueSubString(String str) {
        int size = 1;
        FourLeavesTreeNode root = new FourLeavesTreeNode('#');
        for (size = 1; size < str.length(); size++) {
            boolean s = complete(root, str, size);
            if (!s) {
                break;
            }
        }
        return size;
    }

    private static boolean complete(FourLeavesTreeNode root, String str, int size) {
        int count = 1;
        for (int i = 0; i < size; i++) {
            count = count * 4;
        }
        int c = 0;
        for (int i = 0; i < str.length() - size; i++) {
            FourLeavesTreeNode node = root;
            for (int j = 0; j < size; j++) {
                char ch = str.charAt(i + j);
                if (node.getChild(ch) == null) {
                    node.setChild(ch, new FourLeavesTreeNode(ch));
                    c++;
                    if (c == count) {
                        return true;
                    }
                } else {
                    node = node.getChild(ch);
                }
            }

        }
        return c == count;
    }
}
