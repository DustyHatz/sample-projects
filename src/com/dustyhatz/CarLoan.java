/*
This is a basic car loan calculator!
By: Dustin Hatzenbuhler
*/
public class CarLoan {
  public static void main(String[] args) {
  int carLoan = 10000; //dollars
  int loanLength = 3; //years
  int interestRate = 5; //percent
  int downPayment = 200; //dollars
  
  if(loanLength <= 0 || interestRate <= 0) {
			System.out.println("Error! You must take out a valid car loan.");
  } 
  
  	else if(downPayment >= carLoan) {
    	System.out.println("No loan required. The car can be paid in full.");
  } 
  
  	else {
    	int remainingBalance = carLoan - downPayment;
  		int months = loanLength * 12;
  		int monthlyBalance = remainingBalance / months;
  		int interest = (monthlyBalance * interestRate) / 100;
  		int monthlyPayment = monthlyBalance + interest;
  		System.out.println(monthlyPayment);
      
  } 
 }
}