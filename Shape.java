class Shape
 {
    public void area(int length, int breadth)
     {
        int area = length * breadth;
        System.out.println("Area of Rectangle: " + area);
    }

    public void area(int side)
     {
        int area = side * side;
        System.out.println("Area of Square: " + area);
    }
    public void area(double base, double height) {
        double area = 0.5 * base * height;
        System.out.println("Area of Triangle: " + area);
    }
    public static void main(String[] args) 
    {
        Shape shape = new Shape();
        shape.area(4, 3);
        shape.area(2);
        shape.area(2.0, 5.0);
    }
}