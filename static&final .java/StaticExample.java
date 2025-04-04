class StaticExample 
{
    static int count = 0;
    static void display() 
    {
        System.out.println("Static Method Called");
    }
    static
     {
        System.out.println("Static Block Executed");
    }
    StaticExample() 
    {
        count++;
        System.out.println("Instance Created, Count: " + count);
    }
    public static void main(String[] args) 
    {
        StaticExample obj1 = new StaticExample();
        StaticExample obj2 = new StaticExample();
        StaticExample.display();
    }
}
