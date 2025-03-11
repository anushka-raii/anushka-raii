// Parent class (Superclass)
class Animal {
    void makeSound() {
        System.out.println("Animals make sounds");
    }
}
class Dog extends Animal {
    void bark() {
        System.out.println("Dog barks");
    }
}

public class Inheritance {
    public static void main(String[] args) {
        Dog myDog = new Dog();
        myDog.makeSound(); 
        myDog.bark(); 
    }
}
