import java.util.ArrayList;
import java.util.Collections;
// import java.util.List;

public class SortNames {

    public static void main(String[] args) {

        // Create an ArrayList of names
        ArrayList<String> names = new ArrayList<>();
        names.add("Collins");
        names.add("Cyprian");
        names.add("David");
        names.add("Peter");
        names.add("Joseph");
        names.add("Kemboi");
        names.add("Joel");
        names.add("Kelvin");
        names.add("Philip");
        names.add("Rono");
        names.add("Masea");
        names.add("Leparan");

        // Display original list
        System.out.println("Original List:");
        System.out.println(names);

        // -------- Method 1: Using Collections.sort() --------
        Collections.sort(names);

        System.out.println("\nThe names in ascending order are:");
        System.out.println(names);

        // Add more names to demonstrate List.sort()
        // names.add("Eve");
        // names.add("Frank");

        // -------- Method 2: Using List.sort() --------
        names.sort(null); // null means natural ordering (ascending)

        System.out.println("\nThe names in ascending order are:");
        System.out.println(names);
    }
}
