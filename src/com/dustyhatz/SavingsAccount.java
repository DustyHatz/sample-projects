public class SavingsAccount {
  
    int balance;
    
    public SavingsAccount(int initialBalance){
      balance = initialBalance;
    }
    
    public void checkBalance(){
      System.out.println("Hello!");
      System.out.println("Your balance is " + balance);
    }
    
    public void deposit(int amountToDeposit){
      balance = balance + amountToDeposit;
      System.out.println("You just deposited " + amountToDeposit);
    }
    
    public int withdraw(int amountToWithdraw){
      balance = balance - amountToWithdraw;
        System.out.println("You just withdrew " + amountToWithdraw);
        return amountToWithdraw;
    }
    
    public static void main(String[] args){
      SavingsAccount savings = new SavingsAccount(2000);
      
        savings.checkBalance();
        savings.deposit(200);
        savings.checkBalance();
        savings.withdraw(300);
        savings.checkBalance();
      
    }       
  }
  