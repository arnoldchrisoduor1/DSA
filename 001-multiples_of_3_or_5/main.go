package main

import (
	"fmt"
)

func Solution(number int) (sum int) {

	if number < 0 {
		return 0
	}

	for i := 1; i < number; i++ {
		if i%3 == 0 || i%5 == 0 {
			sum += i
		}
	}
	return;
}

func main() {
	fmt.Println(Solution(10))  // Should print 23
    fmt.Println(Solution(20))  // Should print 78
    fmt.Println(Solution(-5))  // Should print 0
    fmt.Println(Solution(0))   // Should print 0
}