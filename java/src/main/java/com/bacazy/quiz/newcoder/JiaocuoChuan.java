package com.bacazy.quiz.newcoder;

/**
 * Created by ZhangCheng on 2017/10/10.
 */
public class JiaocuoChuan {
    static int length(String str) {
        int maxL = 1;
        int l = 1;
        for (int i = 1; i < str.length(); i++) {
            if (str.charAt(i) == str.charAt(i - 1)) {
                l = 1;
            } else {
                l++;
                if (l > maxL) {
                    maxL = l;
                }
            }
        }

        return maxL;
    }
}
