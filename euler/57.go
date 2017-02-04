package main

import (
	"fmt"
	"math/big"
)

func countDigits(n big.Int) int {
	k := 0
	for n.Cmp(new(big.Int).SetInt64(0)) >= 0 {
		k++
		ten := new(big.Int).SetInt64(10)
		n.Quo(&n, ten)
	}
	return k
}
func main() {
	num := new(big.Int).SetInt64(3)
	den := new(big.Int).SetInt64(2)
	ans := 0
	for i := 2; i <= 1000; i++ {
		fmt.Println("Doing ...")
		var t big.Int
		(&t).Add(den, num)
		num.Add(&t, den)
		*den = t
		if len(num.String()) > len(den.String()) {
			ans++
		}
	}
	fmt.Printf("%d", ans)
}
