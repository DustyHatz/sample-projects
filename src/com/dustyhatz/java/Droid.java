package com.dustyhatz;


// This program will create a droid, Carl, make him perform some tasks until his battery is drained, and then recharge his battery.
// By: Dustin Hatzenbuhler

public class Droid {

    // Declare variables
    String name;

    int batteryLevel;

    // Constructor method
    public Droid(String droidName) {

        name = droidName;
        
        batteryLevel = 100;
    }

    // Droid's first response
    public String toString() {

        return "Hello, my name is " + name + " and I'm ready to perform some tasks! Current battery level: " + batteryLevel;
    }

    // Method for performing a task. Each tasks drains battery by 10
    public void performTask(String task) {

        if (batteryLevel >= 10) {

            batteryLevel -= 10;

            System.out.println(name + " is now performing task: " + task);

        } else {

            System.out.println("R.I.P " + name + " is dead...please charge battery.");
        }
    }

    // Method for checking the batter level
    public void checkBattery() {

        System.out.println("Current battery level is " + batteryLevel);
    }

    // Method for charging battery
    public void chargeBattery() {

        batteryLevel = 100;

        System.out.println("Battery recharged!");
    }

    // Main method
    public static void main(String[] args) {

        // Create a new droid, Carl
        Droid carl = new Droid("Carl");

        // Initiate Carl and begin performing tasks
        System.out.println(carl);
        carl.performTask("hopping");
        carl.performTask("skipping");
        carl.performTask("jumping");
        carl.performTask("hopping");
        carl.performTask("skipping");
        carl.checkBattery();
        carl.performTask("jumping");
        carl.performTask("hopping");
        carl.performTask("skipping");
        carl.performTask("jumping");
        carl.performTask("hopping");
        carl.checkBattery();
        carl.performTask("skipping");
        carl.chargeBattery();
    }
}