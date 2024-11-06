// array_diff.go

package main

func arrayDiff(a, b []int) []int {
	// creating a map to mark elemenst present in `b`
	bMap := make(map[int]bool)
	for _, num := range b {
		bMap[num] = true
	}

	// Use a map to store unique elements from `a` that are not in `b`
	uniqueResult := make(map[int]bool)
	result := [] int{}
	for _, num := range a {
		if !bMap[num] && !uniqueResult[num] {
			uniqueResult[num] = true
			result = append(result, num)
		}
	}
	return result
}