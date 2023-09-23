package main

import (
	"errors"
	"fmt"
	"os"
	"strings"
)

func points_for_result(left, right string) (int, error) {
	var points int
	switch left {
	case "A":
		if right == "X" {
			points = 3
		} else if right == "Y" {
			points = 6
		} else {
			points = 0
		}
	case "B":
		if right == "X" {
			points = 0
		} else if right == "Y" {
			points = 3
		} else {
			points = 6
		}
	case "C":
		if right == "X" {
			points = 6
		} else if right == "Y" {
			points = 0
		} else {
			points = 3
		}
	default:
		return -1, errors.New("their move is invalid")
	}

	return points, nil
}

func points_for_play(play string) (int, error) {
	var points int
	switch play {
	case "X":
		points = 1
	case "Y":
		points = 2
	case "Z":
		points = 3
	default:
		return -1, errors.New("invalid play")
	}
	return points, nil
}

func part1(file string) (int, error) {
	points := 0
	for _, line := range strings.Split(file, "\n") {
		plays := strings.Split(line, " ")
		if len(plays) > 2 {
			return -1, errors.New("invalid line")
		}
		theirs, mine := plays[0], plays[1]

		play_points, err := points_for_play(mine)
		if err != nil {
			panic(err)
		}
		result_points, err := points_for_result(theirs, mine)
		if err != nil {
			panic(err)
		}

		points += play_points + result_points
	}

	return points, nil
}

func main() {
	file, err := os.ReadFile("../inputs/day02.txt")
	if err != nil {
		panic(err)
	}

	part1, err := part1(string(file))
	if err != nil {
		panic(err)
	}
	fmt.Println("part1: ", part1)
}
