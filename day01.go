package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func pt1(numbers []int) int {
	var sum int
	for _, number := range numbers {
		sum += number
	}
	return sum
}

func pt2(numbers []int) int {
	var sum int
	occurred := map[int]bool{0: true}
	i := 0
	for {
		sum += numbers[i%len(numbers)]
		if occurred[sum] {
			return sum
		}
		occurred[sum] = true
		i++
	}
}

func main() {
	file, err := os.Open("day01-input.txt")
	if err != nil {
		panic(err)
	}
	defer file.Close()

	var numbers []int
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		number, _ := strconv.Atoi(scanner.Text())
		numbers = append(numbers, number)
	}
	// pt 1
	fmt.Println(pt1(numbers))
	// pt 2
	fmt.Println(pt2(numbers))
}
