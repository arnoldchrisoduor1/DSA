// Return the position of largest value in 'A' of size 'n'

int largest(int A[], int n) {
    int currlarge = 0; // holds the largest element position.
    for (int i=1; i<n; i++) {
        if(A[currlarge] < A[i]) {
            currlarge = i;
        }
    }
    return currlarge;
}