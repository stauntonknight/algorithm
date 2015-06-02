package main

import (
	"fmt"
)

func main() {
	var n int
	fmt.Scan(&n)
	total25 := 0
	total50 := 0
	poss := true
	for i := 0; i < n; i++ {
		var y int
		fmt.Scan(&y)
		bal := y - 25
		if bal >= 50 {
			if total50 > 0 {
				total50--
				bal -= 50
			}
		}
		total25 -= bal / 25
		if total25 < 0 {
			poss = false
		}
		if y == 25 {
			total25 = total25 + 1
		} else if y == 50 {
			total50 = total50 + 1
		}
	}
	if poss {
		fmt.Println("YES")
	} else {
		fmt.Println("NO")
	}
}
