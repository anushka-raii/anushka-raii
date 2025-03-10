class Father {
    void drive() {
        System.out.println("Driving the car slowly...");
    }
}

class Son extends Father
 {
    @Override
    void drive() {
        System.out.println("Driving the car very fast...");
    }
}

public class Main 
{
    public static void main(String[] args) {
        Father f = new Father();
        f.drive();  
        
        Son s = new Son();
        s.drive(); 
    }
}
