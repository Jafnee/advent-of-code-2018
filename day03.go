package main

import (
	"bufio"
	"fmt"
	"os"
	"regexp"
	"strconv"
)

type claim struct {
	id, x, y, width, height int
}

func parseClaim(str string) claim {
	// fmt.Println(str)
	r := regexp.MustCompile(`#(\d+) @ (\d+),(\d+): (\d+)x(\d+)`)
	var g []int
	for _, group := range r.FindStringSubmatch(str)[1:] {
		asInt, _ := strconv.Atoi(group)
		g = append(g, asInt)
	}
	return claim{g[0], g[1], g[2], g[3], g[4]}
}

func main() {
	file, err := os.Open("day03-input.txt")
	if err != nil {
		panic(err)
	}
	var claims []claim
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		claims = append(claims, parseClaim(scanner.Text()))
	}

	const (
		fabricSize    = 1000
		collisionChar = "X"
	)
	var fabric [fabricSize][fabricSize]string
	collisions := 0
	for _, claim := range claims {
		for i := 0; i < claim.width; i++ {
			for j := 0; j < claim.height; j++ {
				currentX := claim.x + i
				currentY := claim.y + j

				existingValue := fabric[currentY][currentX]
				insertValue := strconv.Itoa(claim.id)

				if existingValue != "" {
					if existingValue == strconv.Itoa(claim.id) || existingValue == collisionChar {
						continue
					}
					// Fresh collision
					collisions++
					insertValue = collisionChar
				}
				fabric[currentY][currentX] = insertValue
			}
		}
	}
	// pt 1
	fmt.Println(collisions)

	// Lazy style 😬
	// Just do the same thing again to find the one that doesn't overlap.
	for _, claim := range claims {
		collided := false

		for i := 0; i < claim.width; i++ {
			for j := 0; j < claim.height; j++ {
				existingValue := fabric[claim.y+j][claim.x+i]
				if existingValue != "" && existingValue != strconv.Itoa(claim.id) {
					collided = true
					// wasted effort here, should go to next claim
					break
				}
			}
		}
		if !collided {
			// pt 2
			fmt.Println(claim.id)
			break
		}
	}
}
