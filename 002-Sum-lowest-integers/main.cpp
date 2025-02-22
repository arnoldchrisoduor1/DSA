#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int sum_of_lowest_integers(vector<int> numbers) {
    sort(numbers.begin(), numbers.end());

    return numbers[0] + numbers[1];
}

int main() {

    vector<int> numbers = { 19, 5, 42, 2, 77 };

    int result = sum_of_lowest_integers(numbers);

    cout << "sum of lowest integers " << result << endl;

    return 0;
}