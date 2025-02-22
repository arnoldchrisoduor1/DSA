package ArrayDiff
import java.util.Arrays;
import java.util.List;

public class ArrayDiffTest {

    @Test
    public void testBasicCase() {
        List<Integer> result = ArrayDiff.arrayDiff(Arrays.asList(1, 2), Arrays.asList(1));
        assertEquals(Arrays.asList(2), result);
            }
        
            private void assertEquals(List<Integer> asList, List<Integer> result) {
                // TODO Auto-generated method stub
                throw new UnsupportedOperationException("Unimplemented method 'assertEquals'");
            }
        
            @Test
    public void testMultipleOccurrences() {
        List<Integer> result = ArrayDiff.arrayDiff(Arrays.asList(1, 2, 2, 2, 3), Arrays.asList(2));
        assertEquals(Arrays.asList(1, 3), result);
    }

    @Test
    public void testWithDuplicatesInA() {
        List<Integer> result = ArrayDiff.arrayDiff(Arrays.asList(1, 2, 3, 3, 3, 4), Arrays.asList(3));
        assertEquals(Arrays.asList(1, 2, 4), result);
    }

    @Test
    public void testEmptyB() {
        List<Integer> result = ArrayDiff.arrayDiff(Arrays.asList(1, 2, 3), Arrays.asList());
        assertEquals(Arrays.asList(1, 2, 3), result);
    }

    @Test
    public void testEmptyA() {
        List<Integer> result = ArrayDiff.arrayDiff(Arrays.asList(), Arrays.asList(1, 2));
        assertEquals(Arrays.asList(), result);
    }

    @Test
    public void testAllElementsInB() {
        List<Integer> result = ArrayDiff.arrayDiff(Arrays.asList(1, 2), Arrays.asList(1, 2));
        assertEquals(Arrays.asList(), result);
    }
}
