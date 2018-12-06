package main

import (
	"bufio"
	"fmt"
	"os"
)

func countChars(text string) map[string]int {
	count := map[string]int{}
	for _, char := range text {
		count[string(char)]++
	}
	return count
}

func pt1(ids []string) int {
	var double, triple int
	checkAgainst := map[int]*int{
		2: &double,
		3: &triple,
	}
	for _, id := range ids {
		charCount := countChars(id)
		for qty, pointer := range checkAgainst {
			for _, count := range charCount {
				if count == qty {
					*pointer++
					break
				}
			}
		}
	}
	return double * triple
}

func stringDiffs(s1, s2 string) []int {
	diffs := []int{}
	for i, char := range s1 {
		if string(char) != string(s2[i]) {
			diffs = append(diffs, i)
		}
	}
	return diffs
}

func pt2(ids []string) string {
	for i, id := range ids {
		idsToCompare := ids[i+1:]
		for _, otherID := range idsToCompare {
			diffs := stringDiffs(id, otherID)
			if len(diffs) == 1 {
				diffIndex := diffs[0]
				return id[:diffIndex] + id[diffIndex+1:]
			}
		}
	}
	return "Uh oh, something went wrong"
}

func main() {
	file, err := os.Open("day02-input.txt")
	if err != nil {
		panic(err)
	}
	defer file.Close()

	var ids []string
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		ids = append(ids, scanner.Text())
	}
	// pt 1
	fmt.Println(pt1(ids))
	// pt 2
	fmt.Println(pt2(ids))
}
