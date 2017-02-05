package main

import (
	"fmt"
	"math/big"
)

func getPower(a big.Int, b int) big.Int {
	var ans big.Int
	(&ans).SetUint64(1)
	for b > 0 {
		if b%2 != 0 {
			(&ans).Mul(&a, &ans)
		}
		b = b >> 1
		(&a).Mul(&a, &a)
	}
	return ans
}

func main() {
	var i uint64
	i = 2
	kount := 0
	for i = 1; i < 20; i++ {
		missed := 0
		for j := 1; ; j++ {
			var z big.Int
			(&z).SetUint64(i)
			t := getPower(z, j)
			if len(t.String()) == j {
				fmt.Println(i, j, t)
				kount++
				missed = 0
			} else {
				missed++
				if missed == 20 {
					break
				}
			}
		}
	}
	fmt.Println(kount)
}
