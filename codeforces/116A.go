package main

import (
	"fmt"
)

func main() {
	var T int
	fmt.Scan(&T)
	c := 0
	capia := 0
	for i := 0; i < T; i++ {
		var a, b int
		fmt.Scan(&a, &b)
		c = c - a + b
		if capia < c {
			capia = c
		}

	}
	fmt.Println(capia)

}
