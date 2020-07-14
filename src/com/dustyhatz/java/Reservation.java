
// Example program for confirming a restaurant reservation.
// By: Dustin Hatzenbuhler


public class Reservation {

    // Declare variables
    int guestCount;
    int restaurantCapacity;
    boolean isRestaurantOpen;
    boolean isConfirmed;


    // Method for creating a reservation
    public Reservation(int count, int capacity, boolean open) {

        // If the number of people is 0 or more than 8 reservation cannot be made
        if (count < 1 || count > 8) {

            System.out.println("Invalid reservation!");

            isConfirmed = false;
        }

        // Else assign variables to the method arguments
        guestCount = count;

        restaurantCapacity = capacity;

        isRestaurantOpen = open;
    }


    // Method for confirming a reservation
    public void confirmReservation() {

        // Ensure the number of guests is not more than the restaurant capacity
        // and that restaurant is open
        if (restaurantCapacity >= guestCount && guestCount <= 8 && guestCount > 1 && isRestaurantOpen) {

            System.out.println("Reservation confirmed");

            isConfirmed = true;

        // Else deny reservation
        } else {

            System.out.println("Reservation denied");

            isConfirmed = false;
        }
    }


    // Method to inform the user whether or not reservation was successful
    public void informUser() {

        if (!isConfirmed) {

            System.out.println("Unable to confirm reservation, please contact restaurant.");

        } else {

            System.out.println("Please enjoy your meal!");
        }
    }


    // Main method
    public static void main(String[] args) {

        // Create a new reservation for a part of 2
        Reservation partyOfTwo = new Reservation(2, 7, true);

        // Check whether or not the reservation can be made
        partyOfTwo.confirmReservation();

        // Inform the user of the reservation status
        partyOfTwo.informUser();
    }
}

