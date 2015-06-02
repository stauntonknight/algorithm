package main

import (
	"fmt"
)

func max(x, y int) int {
	if x > y {
		return x
	} else {
		return y
	}
}

func main() {
	var n, m, q int
	fmt.Scan(&n, &m, &q)
	var bears = make([][]int, n)
	for i := range bears {
		bears[i] = make([]int, m)
	}
	var count = make([]int, n)
	for i := range bears {
		count[i] = 0
		total := 0
		for j := range bears[i] {
			fmt.Scan(&bears[i][j])
			if bears[i][j] == 1 {
				total++
			} else {
				count[i] = max(count[i], total)
				total = 0
			}
		}
		if total != 0 {
			count[i] = max(count[i], total)
		}
	}
	for i := 0; i < q; i++ {
		var a, b int
		fmt.Scan(&a, &b)
		a = a - 1
		b = b - 1
		if bears[a][b] == 1 {
			bears[a][b] = 0
		} else {
			bears[a][b] = 1
		}
		kount := 0
		maxim := 0
		for j := 0; j < m; j++ {
			if bears[a][j] == 1 {
				maxim = maxim + 1
			} else {
				kount = max(maxim, kount)
				maxim = 0
			}
		}
		if maxim != 0 {
			kount = max(kount, maxim)
		}
		count[a] = kount
		x := 0
		for t := range count {
			x = max(x, count[t])
		}
		fmt.Println(x)
	}

}
