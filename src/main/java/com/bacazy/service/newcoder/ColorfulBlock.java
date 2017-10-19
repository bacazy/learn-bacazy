package com.bacazy.service.newcoder;

import java.util.HashSet;

public class ColorfulBlock {
    static int arrange(String str) {
        HashSet<Character> characters = new HashSet<Character>();
        for (int i = 0; i < str.length(); i++) {
            characters.add(str.charAt(i));
        }

        int size = characters.size();
        if (size == 1) {
            return 1;
        } else if (size == 2) {
            return 2;
        }
        return 0;
    }
}
