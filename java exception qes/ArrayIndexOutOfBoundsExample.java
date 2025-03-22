import java.util.Scanner;
public class ArrayIndexOutOfBoundsExample 
{
    public static void main(String[] args)
     {
        int[] numbers = {10, 20, 30, 40, 50};
        Scanner scanner = new Scanner(System.in);
        try 
        {
            System.out.print("Enter an index (0 to 4): ");
            int index = scanner.nextInt(); 

         
            System.out.println("Value at index " + index + ": " + numbers[index]);

        } 
        catch (ArrayIndexOutOfBoundsException e)
         {
            System.out.println("Invalid index. Please enter a number between 0 and 4.");
        } finally 
        {
           
            scanner.close();
        }
    }
}

