#include <iostream>
#include <string>

using namespace std;

bool solution(const string& text, const string& ending) {
    if(ending.size() > text.size()) {
        return false;
    }
    return text.substr(text.size() - ending.size()) == ending;
}

int main() {

    string text = "abc";
    string ending = "bac";

    bool result = solution(text, ending);
    cout << "Result " << (result ? "True" : "False") << endl;

    return 0;
}