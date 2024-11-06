// ArrayDiff.java
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;

public class ArrayDiff {
    public static List<Integer> arrayDiff(List<Integer> a, List<Integer> b) {
        // Use a HashSet for elements in `b` for fast lookup
        HashSet<Integer> bSet = new HashSet<>(b);
        
        // List to store the result
        ArrayList<Integer> result = new ArrayList<>();
        HashSet<Integer> seen = new HashSet<>();

        // Loop through `a` and add elements to result if not in `b` and not already added
        for (Integer num : a) {
            if (!bSet.contains(num) && !seen.contains(num)) {
                result.add(num);
                seen.add(num);
            }
        }
        
        return result;
    }
}
