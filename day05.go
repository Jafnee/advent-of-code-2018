package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func fullyReactPolymer(polymer string) string {
	polymerSlice := strings.Split(polymer, "")
	startIndex := 0
	for {
		for i := startIndex; i < len(polymerSlice); i++ {
			// last unit can't react
			if i == len(polymerSlice)-1 {
				return strings.Join(polymerSlice, "")
			}
			unit1 := polymerSlice[i]
			unit2 := polymerSlice[i+1]
			if strings.ToLower(unit1) == strings.ToLower(unit2) && unit1 != unit2 {
				polymerSlice = append(polymerSlice[:i], polymerSlice[i+2:]...)
				if i != 0 {
					startIndex = i - 1
				}
				break
			}
		}
	}
}

func main() {
	file, err := os.Open("day05-input.txt")
	if err != nil {
		panic(err)
	}
	scanner := bufio.NewScanner(file)
	scanner.Scan()
	polymer := scanner.Text()

	// pt1
	fmt.Println(len(fullyReactPolymer(polymer)))
}
