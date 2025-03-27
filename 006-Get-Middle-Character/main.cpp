#include <iostream>
#include <string>

using namespace std;

string get_laptop(string s)  {
    int length = s.length();
    string result;

    // for even number of characters in the string.
    if (length % 2 == 0 ) {

        int value = length / 2;
        result = string(1, s[value - 1]) + s[value];

    } else {
        int value = length / 2;
        result = string(1, s[value]);
    }
    return result;
}

int main() {
    cout << "Current state: " << get_laptop("textin") << endl;
    cout << "Current state: " << get_laptop("hello") << endl;
    cout << "Current state: " << get_laptop("hello") << endl;
    return 0;
}