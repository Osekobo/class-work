import java.util.ArrayList;
import java.util.Collections;
public class SortNames {
    public static void main(String[] args) {
        // Create an ArrayList of names
        ArrayList<String> names = new ArrayList<>();
        names.add("Collins Oseko EEEI/02388/2024");
        names.add("Cyprian Kirui EEI/02336/2024");
        names.add("David Omega EEEI/02357/2024");
        names.add("Peter Otieno EEEI/01375/2022");
        names.add("Joseph Mwaniki EEEI/02329/2024");
        names.add("Gidion Kemboi EEEI/02335/2024");
        names.add("Joel Mutuku EEEI/02310/2024");
        names.add("Kelvin Kiprono EEEI/02362/2024");
        names.add("Philip Mwanzia EEEI/01518/2024");
        names.add("Rono Collins EEEI/02334/2024");
        names.add("Masea Bellamy EEEI/02367/2024");
        names.add("Leparan Duncan EEEI/02338/2024");
        names.add("Dennis Mwangi EEEI/02967/2024");

        // Display original list
        System.out.println("Original List:");
        System.out.println(names);

        // -------- Method 1: Using Collections.sort() --------
        Collections.sort(names);

        System.out.println("\nThe names in ascending order are:");
        System.out.println(names);

        // -------- Method 2: Using List.sort() --------
        names.sort(null); // null means natural ordering (ascending)

        System.out.println("\nThe names in ascending order are:");
        System.out.println(names);
    }
}
