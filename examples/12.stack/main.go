package main

import (
	"fmt"
	"time"
)

func bench(note string, testee func(int) int) {
	iterations := 100_000_000
	acc := 0
	s := time.Now()
	for i := 0; i < iterations; i++ {
		acc = testee(acc)
	}
	f := time.Now()
	elapsed := f.Sub(s)
	fmt.Printf("%s spent %f μs\n", note, (float64)(elapsed.Microseconds())/(float64)(iterations))
}

// UpArg is used to store upwards funarg
var UpArg = func(n int) int { return n }

func slowest(v int) int {
	z := v + 1
	f := func(x int) int {
		z += x // z is modified
		return z
	}
	UpArg = f // requires writable instance of z
	return f(v)
}

func slower(v int) int {
	z := v + 1
	f := func(x int) int {
		return z + x
	}
	UpArg = f // requires copy of z
	return f(v)
}

func fast(v int) int {
	z := v + 1
	f := func(x int) int {
		return z + x
	}
	UpArg = fast // just to take time
	return f(v)
}

func main() {
	bench("fast", fast)
	bench("slower", slower)
	bench("slowest", slowest)
}
