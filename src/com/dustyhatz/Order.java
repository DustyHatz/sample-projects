/*
This program allows you to check the shipping status and shipping cost of an order.
By: Dustin Hatzenbuhler
*/

public class Order {

    // Declare variables
    boolean isFilled;
    double billAmount;
    String shipping;

    // Method for new orders
    public Order(boolean filled, double cost, String shippingMethod) {
        if (cost > 24.00) {
            System.out.println("High value item!");
        } else {
            System.out.println("Low value item!");
        }
        isFilled = filled;
        billAmount = cost;
        shipping = shippingMethod;
    }

    // Method for checking status of order
    public void checkOrder() {
        if (isFilled) {
            System.out.println("Shipping");
        } else {
            System.out.println("Order not ready");
        }

        double shippingCost = calculateShipping();

        System.out.println("Shipping cost: " + shippingCost);

    }

    // Calculate shipping cost of order
    public double calculateShipping() {
        double shippingCost;
        switch (shipping) {
            case "Regular":
                shippingCost = 0;
                break;
            case "Express":
                shippingCost = 1.75;
                break;
            default:
                shippingCost = .50;
        }
        return shippingCost;
    }

    public static void main(String[] args) {

        Order myOrder = new Order(true, 2, "express");
        myOrder.checkOrder();
    }
}
