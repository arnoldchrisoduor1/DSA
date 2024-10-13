package main

import "testing"

// Testing the Solution function.
func TestSolution(t *testing.T) {
	// test cases
	tests := []struct {
		input int
		expected int
	}{
		{10, 23},
		{20, 78},
		{-5, 0},
		{0, 0},
		{1, 0},
	}

	// Looping through the test cases.
	for _, test := range tests {
		result := Solution(test.input)
		if result != test.expected {
			t.Errorf("Solution(%d), =%d; expected %d", test.input, result, test.expected)
		}
	}
}