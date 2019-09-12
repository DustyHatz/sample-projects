public class Droid{
    String name;
    int batteryLevel;
    
    public Droid(String droidName){
      name = droidName;
      batteryLevel = 100;
    }
    
    public String toString(){
      return "Hello, my name is " + name + " and I'm ready to perform some tasks! Current battery level: "+ batteryLevel;
    }
    
    public void performTask(String task){
      if (batteryLevel >= 10) {
        batteryLevel = batteryLevel - 10;
        System.out.println(name + " is now performing task: " + task);
    } else {
        System.out.println("R.I.P " + name + " is dead...please charge battery."); 
        }
    }  
  
    public void checkBattery(){
        System.out.println("Current battery level is " + batteryLevel);
      }
    
    public void chargeBattery(){
      batteryLevel = 100;
      System.out.println("Battery recharged!");
    }
      
    public static void main(String[] args){
      
      Droid codey = new Droid("Codey");
      
      System.out.println(codey);
      codey.performTask("hopping");
      codey.performTask("skipping");
      codey.performTask("jumping");
      codey.performTask("hopping");
      codey.performTask("skipping");
      codey.checkBattery();
      codey.performTask("jumping");
      codey.performTask("hopping");
      codey.performTask("skipping");
      codey.performTask("jumping");
      codey.performTask("hopping");
      codey.checkBattery();
      codey.performTask("skipping");
      codey.chargeBattery();
    
    }
  }