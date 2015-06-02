package main

import (
	"fmt"
)

func main() {
	var s string
	fmt.Scan(&s)
	count0 := 0
	count1 := 0
	danger := false
	for i := 0; i < len(s); i++ {
		if s[i] == '0' {
			count0++
			count1 = 0
		} else {
			count1++
			count0 = 0
		}
		if count1 == 7 || count0 == 7 {
			danger = true
		}
	}
	if danger {
		fmt.Println("YES")
	} else {
		fmt.Println("NO")
	}

}
