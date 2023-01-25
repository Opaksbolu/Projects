
import java.util.Scanner;

public class Array {

    public static void main(String[] args) {
        int n = 1;
        int entry;
        int sold;
        Scanner sc = new Scanner(System.in);
        System.out.print("How many types of soda would you like to enter:");
        entry = sc.nextInt();
        if (entry < 0) {
            System.out.print("How many types of soda would you like to enter:");
            entry = sc.nextInt();
        }
        String soda_name[] = new String[entry];
        sc.nextLine();
        for (int i = 0; i < entry; i++) {
            System.out.print("Enter the name of soda type1 :");
            String s = sc.nextLine();
            soda_name[i] = s;
        }
        int array[] = new int[soda_name.length];
        for (int i = 0; i < array.length; i++) {
            System.out.print("Enter the number of " + soda_name[i] + " bottles sold:");
            sold = sc.nextInt();
            if (sold < 0) {
                System.out.print("Enter the number of " + soda_name[i] + " bottles sold:");
                sold = sc.nextInt();
                array[i] = sold;
            }
            array[i] = sold;
        }

        int sum = 0;
        int max = 0;
        int maxnum = Integer.MIN_VALUE;
        int min = 0;
        int minnum = Integer.MAX_VALUE;
        for (int i = 0; i < array.length; i++) {
            sum += array[i];
            if (maxnum <= array[i]) {
                max = i;
                maxnum = array[i];
            }

            if (minnum >= array[i]) {
                min = i;
                minnum = array[i];
            }
        }
        System.out.println("Total Sold: " + sum);
        System.out.println("Highest Sold:" + soda_name[max]);
        System.out.println("Lowest Sold:" + soda_name[min]);
    }
}
