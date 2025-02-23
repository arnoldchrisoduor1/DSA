#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

bool is_triangle(int a, int b, int c) {
    vector<int> values = { a, b, c };

    sort(values.begin(), values.end());

    return values[0] + values[1] > values[2];
}

int main() {
    bool result = is_triangle(1, 2, 2);

    cout << "the answer is " << (result ? "True" : "False") << endl;
}