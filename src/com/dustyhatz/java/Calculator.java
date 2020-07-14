
// Example of a basic calculator program
// By: Dustin Hatzenbuhler



public class Calculator {

    public Calculator() {

    }

    // Method for addition
    public int add(int a, int b) {

        int result = a + b;

        return result;
    }


    // Method for subtraction
    public int subtract(int a, int b) {

        int result = a - b;

        return result;
    }


    // Method for multiplication
    public int multiply(int a, int b) {

        int result = a * b;

        return result;
    }


    // Method for division
    public int divide(int a, int b) {

        int result = a / b;

        return result;
    }


    // Method for finding the remainder
    public int modulo(int a, int b) {

        int result = a % b;

        return result;
    }


    // Main method
    public static void main(String[] args) {

        // Create new calculator
        Calculator myCalculator = new Calculator();

        // Print example calculation to find remainder of 11 % 3
        System.out.println(myCalculator.modulo(11, 3));

        // Print a nice message
        System.out.println("Cool! You did basic math.");
    }
}