package main

import (
	"fmt"
)

func SwapCase(r uint8) uint8 {
	switch {
	case 'a' <= r && r <= 'z':
		return r - 'a' + 'A'
	case 'A' <= r && r <= 'Z':
		return r - 'A' + 'a'
	default:
		return r
	}
}

func main() {
	var s string
	fmt.Scan(&s)
	change := true
	for i := 1; i < len(s); i++ {
		if s[i] < 'A' || s[i] > 'Z' {
			change = false
		}
	}
	t := ""
	if change == true {
		for i := 0; i < len(s); i++ {
			t += string(SwapCase(s[i]))
		}
		fmt.Println(t)

	} else {
		fmt.Println(s)
	}
}
