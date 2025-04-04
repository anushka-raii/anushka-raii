class BankAccount 
{ 
    private int balance = 100;
    public void withdraw(int amount) 
{ 
        if (balance >= amount) 
{          
System.out.println(Thread.currentThread().getName() + " is withdrawing " + amount); 
            balance = balance - amount; 
            System.out.println("Remaining balance: " + balance); 
} 
else 
{   
System.out.println(Thread.currentThread().getName() + " cannot withdraw. Insufficient balance!"); 
        } 
    } 
} 
 
public class ConcurrencyProblem
 { 
    public static void main(String[] args) { 
        BankAccount account = new BankAccount(); 

      
        Thread person1 = new Thread(() -> 
account.withdraw(80), "Person 1"); 
        Thread person2 = new Thread(() -> 
account.withdraw(80), "Person 2"); 
 
        person1.start(); 
        person2.start(); 
} 
} 