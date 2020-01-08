// Basic example of using a for loop to find the most expensive and least expensive prices in a list.

import java.util.ArrayList;

class Expensive {

    public static void main(String[] args) {
        ArrayList<Double> expenses = new ArrayList<Double>();

        expenses.add(54.75);
        expenses.add(99.99);
        expenses.add(4.25);
        expenses.add(46.78);
        expenses.add(149.99);
        expenses.add(29.99);

        // Initialize the most expensive starting value at 0
        double mostExpensive = 0;
        // Initialize the least expensive starting value assuming you know the largest amount in the list
        double leastExpensive = 200;

        for (double expense : expenses) {
            if (expense > mostExpensive) {
                mostExpensive = expense;
            }
        }
        for (double expense : expenses) {
            if (expense < leastExpensive) {
                leastExpensive = expense;
            }
        }
        System.out.println(expenses);
        System.out.println("Most Expensive: " + mostExpensive);
        System.out.println("Least Expensive: " + leastExpensive);

    }
}