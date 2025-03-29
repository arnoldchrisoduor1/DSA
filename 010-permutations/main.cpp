// C++ function for generating a random permutations.
// The n values of the sequence are stored in positions 0 through n-1 of arrays A.

// Randomly permute the "n" values of arrsy "A".
template<typename E>
void permute(E A[], int n) {
    for (int i = n; i>0; i--)
        swap(A, i-1, Random(i));
}