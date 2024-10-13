import java.util.stream.*;

public class MultipleSum {
    public static int solution(int number) {
        int sum = 0;

        if (number < 0){
            return 0;
        }

        for(int i = 1; i < number; i++) {
            if (i % 3 == 0 || i % 5 == 0) {
                sum += i;
            }
        }
        return sum;
    }

    // ================ OPTIMIZED ===================
    public static int solution2(int number2) {
        return IntStream.range(3, number2).filter(n -> n % 3 == 0 || n % 5 == 0).sum();
    }

    public static void main(String[] args) {
        int number = 10;
        int result = solution(number);
        System.out.println("Sum " + number + " is : " + result);
    }
}