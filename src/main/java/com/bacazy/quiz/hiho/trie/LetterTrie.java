package com.bacazy.quiz.hiho.trie;


public class LetterTrie {
    char letter;
    int count = 0;
    LetterTrie[] children = new LetterTrie[26];

    public LetterTrie(char letter) {
        this.letter = letter;
    }

    public void add(String s){
        char[] cs = s.toCharArray();
        LetterTrie lt = this;
        for(char c:cs){
            if (lt.children[index(c)] == null){
                lt.children[index(c)] = new LetterTrie(c);
                lt = children[index(c)];
                lt.count++;
            }
        }
    }

    private static int index(char c) {
        return (byte)c - (byte)'a';
    }

    public int getCount(String s){
        char[] cs = s.toCharArray();
        LetterTrie lt = this;
        int lc = 0;
        for(char c:cs){
            if (lt.children[index(c)] == null){
                return 0;
            }else {
                lt = lt.children[index(c)];
                lc = lt.count;
            }
        }
        return lc;
    }
}
