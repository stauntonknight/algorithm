package main

import (
	"fmt"
)

func main() {
	var s string
	fmt.Scan(&s)
	output := false
	for i := 0; i < len(s); i++ {
		switch {
		case s[i] == 'H':
			fallthrough
		case s[i] == '9':
			fallthrough
		case s[i] == 'Q':
			output = true
		}
	}
	if output {
		fmt.Println("YES")
	} else {
		fmt.Println("NO")
	}

}
