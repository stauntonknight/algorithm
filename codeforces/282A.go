package main

import (
	"fmt"
)

func main() {
	var t int
	fmt.Scan(&t)
	c := 0
	for i := 0; i < t; i++ {
		var s string
		fmt.Scan(&s)
		if s[1] == '-' {
			c = c - 1
		} else {
			c = c + 1
		}
	}
	fmt.Println(c)
}
