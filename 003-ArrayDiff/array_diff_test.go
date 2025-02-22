package main

import (
	"reflect"
	"testing"
)

func TestArrayDiff(t *testing.T) {
	tests := []struct {
		a, b, expected []int
	} {
		{[]int{1, 2}, []int{1}, []int{2}},
        {[]int{1, 2, 2, 2, 3}, []int{2}, []int{1, 3}},
        {[]int{1, 2, 3, 3, 3, 4}, []int{3}, []int{1, 2, 4}},
        {[]int{1, 2, 3}, []int{}, []int{1, 2, 3}},
        {[]int{}, []int{1, 2}, []int{}},
        {[]int{1, 2}, []int{1, 2}, []int{}},
	}

	for _, test := range tests {
		result := arrayDiff(test.a, test.b)
		if !reflect.DeepEqual(result, test.expected) {
			t.Errorf("arrayDiff(%v, %v) = %v; expected %v", test.a, test.b, result, test.expected)
		}
	}
}