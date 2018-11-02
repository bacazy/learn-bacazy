package com.bacazy.learn.string;

import java.util.ArrayList;
import java.util.List;

public class ZigZag {
    public String convert(String s, int numRows) {
        if (numRows == 0){
            return s;
        }
        List<List<Character>> charTable = new ArrayList<List<Character>>(numRows);
        for (int i = 0; i < numRows; i++) {
            charTable.add(new ArrayList<Character>());
        }
        StringBuilder builder = new StringBuilder();
        int row = 0;
        boolean direction = true;
        for (char c: s.toCharArray()){
            charTable.get(row).add(c);
            if (row == 0){
                direction = true;
                row = 1;
                continue;
            }

            if (row == numRows - 1){
                direction = false;
                row = numRows - 2;
                continue;
            }

            if(direction){
                row++;
            }else {
                row--;
            }
        }

        for (List<Character> r: charTable){
            for(char c: r){
                builder.append(c);
            }
        }

        return builder.toString();
    }
}
