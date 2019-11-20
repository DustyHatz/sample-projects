/*
This program allows you to confirm a restaurant reservation.
By: Dustin Hatzenbuhler
*/
public class Reservation {
    int guestCount;
    int restaurantCapacity;
    boolean isRestaurantOpen;
    boolean isConfirmed;

    public Reservation(int count, int capacity, boolean open) {
        if (count < 1 || count > 8) {
            System.out.println("Invalid reservation!");
            isConfirmed = false;
        }
        guestCount = count;
        restaurantCapacity = capacity;
        isRestaurantOpen = open;
    }
    // Method for confirming a reservation
    public void confirmReservation() {
        if (restaurantCapacity >= guestCount && guestCount <= 8 && guestCount > 1 && isRestaurantOpen) {
            System.out.println("Reservation confirmed");
            isConfirmed = true;
        } else {
            System.out.println("Reservation denied");
            isConfirmed = false;
        }
    }

    public void informUser() {
        if (!isConfirmed) {
            System.out.println("Unable to confirm reservation, please contact restaurant.");
        } else {
            System.out.println("Please enjoy your meal!");
        }
    }

    // Main method
    public static void main(String[] args) {

        Reservation partyOfTwo = new Reservation(2, 7, true);
        partyOfTwo.confirmReservation();
        partyOfTwo.informUser();
    }
}