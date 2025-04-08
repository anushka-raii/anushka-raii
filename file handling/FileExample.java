//creating and using file class
import java.io.File;
public class FileExample 
{
    public static void main(String[] args) 
    {
        File myFile = new File("example.txt");
        
        try
         {
            if (myFile.createNewFile()) 
            {
                System.out.println("File created: " + myFile.getName());
            } else 
            
            {
                System.out.println("File already exists.");
            }
        } catch (Exception e) 
        {
            System.out.println("An error occurred.");
        }
    }
}
