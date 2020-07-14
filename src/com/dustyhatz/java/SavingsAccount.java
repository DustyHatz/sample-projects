// Example program for creating and maintaining a basic savings bank account
// By: Dustin Hatzenbuhler


public class SavingsAccount {

    // Declare variable for account balance
    int balance;


    // Constructor method
    public SavingsAccount(int initialBalance){

        // Set the initial balance
        balance = initialBalance;
    }


    // Method to check and print the current account balance
    public void checkBalance(){

        System.out.println("Hello!");

        System.out.println("Your balance is " + balance);
    }


    // Method to deposit an amount into the account 
    public void deposit(int amountToDeposit){

        // Add the amount to deposit to the current balance
        balance = balance + amountToDeposit;

        // Print the deposited amount
        System.out.println("You just deposited " + amountToDeposit);
    }


    // Method to withdraw and amount from the account
    public void withdraw(int amountToWithdraw){

        // Subtract the amount to withdraw from the current balance 
        balance = balance - amountToWithdraw;

        // Print the withdrawn amount
        System.out.println("You just withdrew " + amountToWithdraw);
    }


    // Main method
    public static void main(String[] args){

        // Create new savings account with initial balance of 2000
        SavingsAccount savings = new SavingsAccount(2000);

        // Check balance, deposit, and withdraw
        savings.checkBalance();
        savings.deposit(200);
        savings.checkBalance();
        savings.withdraw(300);
        savings.checkBalance();

    }
}
