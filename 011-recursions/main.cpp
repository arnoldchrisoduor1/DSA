// Computing for n recursively.

long fact(int n) {
    // to fit n! into a long variable, we require n <= 12
    Assert((n >= 0) && (n <= 12), "Input out of range");
    if (n <= 1) return 1; // base case: return base solution.
    return n * fact(n-1); // Recursive call for n > 1.
}