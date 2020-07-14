
// Example solution to the "FizzBuzz" problem:
// Print numbers 1-100
// replace multiples of 3 with "Fizz"
// multiples of 5 with "Buzz"
// and multiples of 3 and 5 with "FizzBuzz".


class FizzBuzz {

    public static void main(String[] args) {

        // Iterate over list of numbers 1 through 100
        for (int i = 1; i <= 100; i++) {

            // If the number is a multiple of 15 print "FizzBuzz"
            if (i % 15 == 0) {

                System.out.println("FizzBuzz");
            }

            // If the number is a multiple of 5 print "Buzz"
            else if (i % 5 == 0) {

                System.out.println("Buzz");

            }

            // If the number is a multiple of 3 print "Fizz"
            else if (i % 3 == 0) {

                System.out.println("Fizz");

            }

            // Else print the number
            else {

                System.out.println(i);

            }
        }

    }
}