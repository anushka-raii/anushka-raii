class UncheckedExceptionExample {
    public static void main(String[] args) {
        int a = 10, b = 0;
        try {
            int result = a / b; // Division by zero
            System.out.println(result);
        } catch (ArithmeticException e) {
            System.out.println("Cannot divide by zero.");
        }
    }
}
