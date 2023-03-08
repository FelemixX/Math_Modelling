package main

import (
	"fmt"
	"math/rand"
)

func TruncatedNormal(mean, stdDev, low, high float64) float64 {
	if low >= high {
		panic("high must be greater than low")
	}

	for {
		x := rand.NormFloat64()*stdDev + mean
		if low <= x && x < high {
			return x
    }
	}
}

func main() {
	for i := 0; i < 20; i++ {
		x := TruncatedNormal(10, 5, 8, 13)
		fmt.Println(x)
	}

}
