// Given an array return the two oldest years.

#include <iostream>
#include <vector>
#include <algorithm>

std::vector<int> Solution(const std::vector<int>& arr) {
    if (arr.size() < 2) {
        throw std::runtime_error("Array must contain two celements");
    }

    int largest = std::max(arr[0], arr[1]);
    int secondLargest = std::min(arr[0], arr[1]);

    for(size_t i = 2; i < arr.size(); ++i) {
        if(arr[i] > largest) {
            secondLargest = largest;
            largest = arr[i];
        } else if (arr[i] > secondLargest) {
            secondLargest = arr[i];
        }
    }
    return { largest, secondLargest };
}

int main() {
    std::vector<int> numbers = { 10, 20, 4, 45, 99 };
    std::vector<int> result = Solution(numbers);

    std::cout << "The two largest numbers are: " << result[0] << " and " << result[1] << std::endl;
}