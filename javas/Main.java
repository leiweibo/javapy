interface Car {
    void drive();
}

public class Main implements Car {
    public static void main(String[]args) {
        System.out.println("hello world!");
    }

    @Override
    public void drive() {
        System.out.println("I am driving.");
    }
}