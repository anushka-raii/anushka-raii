//Write File
import java.io.*;

public class WriteFile 
{
    public static void main(String[] args) 
    {
        try
         {
            FileWriter fw = new FileWriter("example.txt");
            BufferedWriter bw = new BufferedWriter(fw);
            
            bw.write("Hello Java!");c
            bw.newLine();
            bw.write("File handling is easy.");
            
            bw.close();
            fw.close();
        } catch (Exception e) 
        {
            System.out.println("Error writing to file.");
        }
    }
}



