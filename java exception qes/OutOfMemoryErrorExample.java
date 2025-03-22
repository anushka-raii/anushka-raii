public class OutOfMemoryErrorExample 
{
    public static void main(String[] args)
     {
        try 
        {
            int[] largeArray = new int[1_000_000_000];
            System.out.println("Array created successfully.");

        } 
        catch (OutOfMemoryError e) 
        {
            System.out.println("The program has run out of memory. Please try with a smaller size.");
        }
        System.out.println("Program execution continues...");
    }
}
