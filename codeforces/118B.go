package main

import (
	"fmt"
)

func main() {
	var n int
	fmt.Scan(&n)
	for i := 1; i <= 2*n+1; i++ {
		t := i - 1
		if i > n+1 {
			t = n - (i - n) + 1
		}
		numspace := n - t
		for k := 0; k < numspace; k++ {
			fmt.Print("  ")
		}
		for j := 0; j < t; j++ {
			fmt.Print(j)
			fmt.Print(" ")
		}
		fmt.Print(t)
		for j := t - 1; j >= 0; j-- {
			fmt.Print(" ")
			fmt.Print(j)
		}
		fmt.Println("")
	}

}
