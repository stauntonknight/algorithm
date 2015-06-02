package main

import (
	"fmt"
)

func main() {
	var t int
	fmt.Scan(&t)
	ans := 0
	for i := 0; i < t; i++ {
		count := 0
		for j := 0; j < 3; j++ {
			var a int
			fmt.Scan(&a)
			count = count + a
		}
		if count >= 2 {
			ans = ans + 1
		}
	}
	fmt.Println(ans)
}
