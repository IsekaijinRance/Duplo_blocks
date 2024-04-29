package main

import (
	"fmt"
	"math/rand"
)

func createRange(n int) []int {
	var a []int

	for i := 0; i < n; i++ {
		a = append(a, i)
	}

	return a
}

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

	a := createRange(15)

	fmt.Println(fyShuffle(a))
}
