#include <cmath>

bool narcissistic( int value ){

  int n = value;
	int i = log10(value) + 1; //get the number of digits in "number"
	int sum = 0;
	
	while (n) {
		sum += pow(n%10, i);
		n /= 10;
	}
	
  return sum == value;
}