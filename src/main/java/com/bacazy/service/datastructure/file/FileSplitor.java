
package com.bacazy.service.datastructure.file;

import java.io.*;

public class FileSplitor {
    public static void split(String in, String out, int skip, int interval) throws IOException {
        BufferedReader reader = new BufferedReader(new FileReader(in));
        BufferedWriter writer = new BufferedWriter(new FileWriter(out));
        int line = 0;
        while (line < skip) {
            line++;
            reader.readLine();
        }

        int intv = 0;
        String str = null;
        while ((str = reader.readLine()) != null) {
            if (intv % interval == 0) {
                writer.write(str);
                writer.newLine();
            }
            intv++;
        }

        reader.close();
        writer.close();
    }
}
