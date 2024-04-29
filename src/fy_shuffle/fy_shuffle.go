package main

import (
	"fmt"
	"math/rand"
)

func fyShuffle(array []int) []int {

	for iterations := (len(array) - 1); iterations > 0; iterations-- {

		ri := rand.Intn(len(array))

		t := array[iterations]
		array[iterations] = array[ri]
		array[ri] = t

	}

	return array
}

func main() {

	var a []int

	for i := 0; i < 15; i++ {
		a = append(a, i)
	}

	fmt.Println(fyShuffle(a))
}
