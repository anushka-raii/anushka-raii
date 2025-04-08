//fileinput stream(read binary files)
import java.io.*;
public class BinaryRead {
    public static void main(String[] args) {
        try {
            FileInputStream fis = new FileInputStream("image.jpg");
            int i;
            while ((i = fis.read()) != -1) {
                // Read byte by byte (not human readable)
                System.out.print(i + " ");
            }
            fis.close();
        } catch (Exception e) 
        {
            System.out.println("Error reading binary file.");
        }
    }
}
