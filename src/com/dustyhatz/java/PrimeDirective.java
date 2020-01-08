// This will find and list all prime numbers in an array of integers

import java.util.ArrayList;

class PrimeDirective {

    // Method to determine whether or not the number is a prime number
    public boolean isPrime(int number) {
        if (number == 2) {
            return true;
        }
        else if (number < 2) {
            return false;
        }
        for (int i = 2; i < number; i++) {
            if (number % i == 0) {
                return false;
            }
        }
        return true;
    }

    // Method will create and return an array list of all prime numbers found
    public ArrayList<Integer> onlyPrimes(int[] numbers) {
        ArrayList<Integer> primes = new ArrayList<Integer>();
        for (int number : numbers) {
            if (isPrime(number)) {
                primes.add(number);
            }
        }
        return primes;
    }

    public static void main(String[] args) {

        PrimeDirective pd = new PrimeDirective();
        int[] numbers = {6, 29, 28, 33, 11, 100, 101, 43, 89};
        System.out.println(pd.onlyPrimes(numbers));

    }

}