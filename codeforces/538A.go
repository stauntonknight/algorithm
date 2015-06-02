package main

import (
	"fmt"
)

func main() {
	var s string
	fmt.Scan(&s)
	size := len(s)
	extra := size - len("CODEFORCES")
	if extra < 0 {
		fmt.Println("NO")
		return
	}
	for i := 0; i <= size-extra; i++ {
		x := s[:i] + s[i+extra:]
		if x == "CODEFORCES" {
			fmt.Println("YES")
			return
		}
	}
	fmt.Println("NO")
}
