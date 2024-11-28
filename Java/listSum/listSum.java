package Java.listSum;

import java.util.ArrayList;

public class listSum {
    public static void main(String[] args) {
        ArrayList<Integer> theList  = new ArrayList<Integer>();
        theList.add(2);
        theList.add(3);
        theList.add(5);
        theList.add(7);

        int sum = 0;

        // the java interaction syntax.
        for(Integer item : theList) {
            sum = sum + item;
        }

        System.out.println("The sum is " + sum);
    }
}
