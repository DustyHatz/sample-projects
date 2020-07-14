// This will find and list all prime numbers in an array of integers
// By: Dustin Hatzenbuhler


import java.util.ArrayList;


class PrimeDirective {

    // Method to determine whether or not the number is a prime number
    public boolean isPrime(int number) {

        // If the number is 2 it is a prime number
        if (number == 2) {

            return true;
        }

        // If the number is less than 2 it is not a prime number
        else if (number < 2) {

            return false;
        }

        // For numbers greater than two, check whether or not i factors evenly into that number
        for (int i = 2; i < number; i++) {
            
            if (number % i == 0) {

                return false;
            }
        }
        return true;
    }


    // Method will create and return an array list of all prime numbers found
    public ArrayList<Integer> onlyPrimes(int[] numbers) {

        // Create a new empty list for the prime numbers
        ArrayList<Integer> primes = new ArrayList<Integer>();

        // Iterate through the list of numbers
        for (int number : numbers) {

            // If the number is a prime number add it to the primes list
            if (isPrime(number)) {

                primes.add(number);
            }
        }

        // Return the list of prime numbers
        return primes;
    }

    // Main method
    public static void main(String[] args) {

        // Create new Prime Directive as pd
        PrimeDirective pd = new PrimeDirective();

        //Create 
        int[] numbers = {6, 29, 28, 33, 11, 100, 101, 43, 89};

        // Print the result of calling onlyPrimes method on numbers
        System.out.println(pd.onlyPrimes(numbers));

    }

}