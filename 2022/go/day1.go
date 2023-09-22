package main

import (
	"fmt"
	"os"
	"slices"
	"strconv"
	"strings"
)

func part1(file string) (int, error) {
	max := 0
	contents := strings.Split(string(file), "\n\n")
	for _, grouped_cals := range contents {
		local := 0

		for _, cal_string := range strings.Split(grouped_cals, "\n") {
			num, _ := strconv.Atoi(cal_string)
			local += num
		}

		if local > max {
			max = local
		}
	}
	return max, nil
}

func part2(file string) (int, error) {
	var sums []int
	contents := strings.Split(string(file), "\n\n")
	for _, grouped_cals := range contents {
		local := 0

		for _, cal_string := range strings.Split(grouped_cals, "\n") {
			num, _ := strconv.Atoi(cal_string)
			local += num
		}

		sums = append(sums, local)
	}
	slices.Sort(sums)
	slices.Reverse(sums)

	total := 0
	for _, num := range sums[:3] {
		total += num
	}
	return total, nil
}

func main() {

	file, err := os.ReadFile("../inputs/day01.txt")
	if err != nil {
		panic(err)
	}

	part1, err := part1(string(file))
	if err != nil {
		panic(err)
	}
	fmt.Println("part1: ", part1)

	part2, err := part2(string(file))
	if err != nil {
		panic(err)
	}
	fmt.Println("part2: ", part2)
}
