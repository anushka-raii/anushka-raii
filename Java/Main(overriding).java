class Car
 {
    String color;
    String brand;
    double mileage;
    double price;
    Car(String color, String brand, double mileage, double price)
     {
        this.color = color;
        this.brand = brand;
        this.mileage = mileage;
        this.price = price;
    }
    void carDetails()
     {
        System.out.println("Brand: " + brand);
        System.out.println("Color: " + color);
        System.out.println("Mileage: " + mileage + " kmpl");
        System.out.println("Price: $" + price);
    }
}

class SportsCar extends Car 
{
    SportsCar(String color, String brand, double mileage, double price) {
        super(color, brand, mileage, price);
    }
    @Override
    void carDetails() {
        System.out.println("🏎️ Sports Car Details:");
        System.out.println("Brand: " + brand);
        System.out.println("Color: " + color);
        System.out.println("Mileage: " + mileage + " kmpl");
        System.out.println("Price: $" + price);
        System.out.println("This is a high-speed luxury car.");
    }
}
public class Main
 {
    public static void main(String[] args) {
        Car sportsCar = new SportsCar("Blue", "Lamborghini", 8.5, 250000);
        sportsCar.carDetails(); 
    }
}
