package main

// go get github.com/dterei/gotsc
// go build main.go
// or on UNIX go build -compiler gccgo -gccgoflags "-march=native -O3" main.go
// main

import (
	"fmt"
	"github.com/dterei/gotsc"
)

func bench(note string, testee func(int) int) {
	iterations := 100_000
	acc := 0
	o := gotsc.TSCOverhead()
	s := gotsc.BenchStart()
	for i := 0; i < iterations; i++ {
		acc = testee(acc)
	}
	f := gotsc.BenchEnd()
	fmt.Printf("%s spent %f cycles avg\n", note, (float64)(f - s - o)/(float64)(iterations))
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
	UpArg = f // requires copy of z; hopefully just a copy as z is never modified
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
	fmt.Println("not benchamrking fast / inner")

	bench("slower", slower)
	bench("slower / inner", UpArg)

	bench("slowest", slowest)
	bench("slowest / inner", UpArg)
}
