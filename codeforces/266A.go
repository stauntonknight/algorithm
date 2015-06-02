package main

import (
	"fmt"
)

func main() {
	var N int
	fmt.Scan(&N)
	var s string
	fmt.Scan(&s)
	ch := s[0]
	count := 0
	for i := 1; i < N; i++ {
		if s[i] == ch {
			count++
		} else {
			ch = s[i]
		}
	}
	fmt.Println(count)
}
