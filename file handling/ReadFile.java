//read file

import java.io.*;

public class ReadFile
 {
    public static void main(String[] args) 
    {
        try
         {
            FileReader fr = new FileReader("example.txt");
            BufferedReader br = new BufferedReader(fr);
            String line;

            while ((line = br.readLine()) != null) 
            {
                System.out.println(line);
            }

            br.close();
            fr.close();
        } catch (Exception e) 
        {
            System.out.println("Error reading file.");
        }
    }
}
