import java.util.ArrayList;

class MostExpensive {

    public static void main(String[] args) {
        ArrayList<Double> expenses = new ArrayList<Double>();

        expenses.add(54.75);
        expenses.add(99.99);
        expenses.add(4.25);
        expenses.add(46.78);
        expenses.add(149.99);
        expenses.add(29.99);

        double mostExpensive = 0;
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