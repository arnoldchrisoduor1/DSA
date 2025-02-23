#include <iostream>
#include <vector>
#include <sstream>
#include <algorithm>
#include <string>
#include <climits>

using namespace std;

int find_short(const string& s) {
    // splitting the string into words.
    vector<string> words;
    stringstream ss(s);
    string word;
    while (ss >> word) {
        words.push_back(word);
    }

    // finding the length of the shortest word.
    int smallestLength = INT_MAX;
    for (const string& w : words) {
        int length = w.length();
        if(length < smallestLength) {
            smallestLength = length;
        }
    }
    cout << smallestLength << endl;
    return smallestLength;
}

int main () {

    string input = "bitcoin take over the world maybe who knows perhaps";
    int result = find_short(input);
    cout << "Length of the shortest word: " << result << endl;

    return 0;
}