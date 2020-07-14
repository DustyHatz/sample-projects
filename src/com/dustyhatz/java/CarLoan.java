
// Example of a basic car loan calculator!
// By: Dustin Hatzenbuhler


public class CarLoan {

    public static void main(String[] args) {

        int carLoan = 10000; //dollars
        int loanLength = 3; //years
        int interestRate = 5; //percent
        int downPayment = 200; //dollars

        // Ensure the loan length and interest rate are valid
        if (loanLength <= 0 || interestRate <= 0) {

            System.out.println("Error! You must take out a valid car loan.");

        // If the down payment is greater than or equal to the loan, then no loan is required
        } else if (downPayment >= carLoan) {

            System.out.println("No loan required. The car can be paid in full.");

        // Calculate and print the monthly car loan payment
        } else {

            int remainingBalance = carLoan - downPayment;

            int months = loanLength * 12;

            int monthlyBalance = remainingBalance / months;

            int interest = (monthlyBalance * interestRate) / 100;

            int monthlyPayment = monthlyBalance + interest;

            System.out.println(monthlyPayment);

        }
    }
}