#include <iostream>
#include <bitset>

using namespace std;

int count_bits(int num) {
    string bit_version = bitset<32>(num).to_string();
    int count = 0;

    for( char x : bit_version) {
        if( x == '1') {
            count++;
        }
    }
    return count;
}

int main () {

    int result = count_bits(1234);

    cout << "The number of bits are: " << result << endl;

    return 0;
}