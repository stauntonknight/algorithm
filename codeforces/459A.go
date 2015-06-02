package main

import (
	"fmt"
)

func main() {
	var x1, y1, x2, y2 int
	fmt.Scan(&x1, &y1, &x2, &y2)
	baseX, baseY := x1, y1
	x1, y1 = 0, 0
	x2, y2 = x2-baseX, y2-baseY
	var x3, x4, y3, y4 int
	poss := true
	if x1 == x2 {
		y := y1 - y2
		if y < 0 {
			y = -y
		}
		x3, y3 = y, y2
		x4, y4 = y, y1
	} else if y1 == y2 {
		x := x1 - x2
		if x < 0 {
			x = -x
		}
		x3, y3 = x1, x
		x4, y4 = x2, x
	} else if x2 == y2 || x2 == -y2 {
		x := x2
		if x < 0 {
			x = -x2
		}
		x3, y3 = x2, 0
		x4, y4 = 0, y2
	} else {
		poss = false
	}
	if poss {

		fmt.Println(x3+baseX, y3+baseY, x4+baseX, y4+baseY)
	} else {
		fmt.Println("-1")
	}
}
