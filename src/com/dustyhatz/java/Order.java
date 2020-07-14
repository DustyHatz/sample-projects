
// Example of a program to check the shipping status and shipping cost of an order.
// By: Dustin Hatzenbuhler


public class Order {

    // Declare variables
    boolean isFilled;

    double billAmount;

    String shipping;


    // Method for new orders
    public Order(boolean filled, double cost, String shippingMethod) {

        // If the cost of the item is greater than 24 print High Value Item
        if (cost > 24.00) {

            System.out.println("High value item!");

        // Else print Low Value Item
        } else {

            System.out.println("Low value item!");
        }

        // Assign variables to the method arguments
        isFilled = filled;

        billAmount = cost;

        shipping = shippingMethod;
    }


    // Method for checking status of order
    public void checkOrder() {

        // If the order is filled then it is ready for shipping
        if (isFilled) {

            System.out.println("Shipping");

        // Else the order is not ready
        } else {

            System.out.println("Order not ready");
        }

        // Call calculateShipping method to calculate and print the shipping cost
        double shippingCost = calculateShipping();

        System.out.println("Shipping cost: " + shippingCost);

    }


    // Calculate shipping cost of order
    public double calculateShipping() {

        // Initiate the shipping cost variable
        double shippingCost;

        // Identify the shipping method and assign the appropriate price
        switch (shipping) {

            // Regular shipping cost is 0
            case "Regular":

                shippingCost = 0;

                break;

            // Express shipping cost is 1.75
            case "Express":

                shippingCost = 1.75;

                break;

            // Default shipping cost is .50
            default:

                shippingCost = .50;
        }

        return shippingCost;
    }

    // Main method
    public static void main(String[] args) {

        // Create a new order with express shipping option
        Order myOrder = new Order(true, 2, "express");

        // Check the order status
        myOrder.checkOrder();
    }
}
