public class Calculator {
    /*
    This program performs basic calculations.
    By: Dustin Hatzenbuhler
    */

    public Calculator() {

    }

    public int add(int a, int b) {
        int result = a + b;
        return result;
    }

    public int subtract(int a, int b) {
        int result = a - b;
        return result;
    }

    public int multiply(int a, int b) {
        int result = a * b;
        return result;
    }

    public int divide(int a, int b) {
        int result = a / b;
        return result;
    }

    public int modulo(int a, int b) {
        int result = a % b;
        return result;
    }

    public static void main(String[] args) {
        Calculator myCalculator = new Calculator();
        System.out.println(myCalculator.modulo(11, 3));
        System.out.println("Cool! You did basic math.");
    }
}