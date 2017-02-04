package main

import "fmt"

func main() {
	k := 1000000
	var a [1000000]bool
	for i := range a {
		a[i] = true
	}
	a[0] = false
	a[1] = false
	start := 2
	for j := start; j*j < k; j++ {
		if a[j] {
			for t := j * j; t < k; t += j {
				a[t] = false
			}
		}
	}

	var primes []int
	for i := range a {
		if a[i] {
			primes = append(primes, i)
		}
	}
	var cum []int
	cum = append(cum, 0)
	for i := range primes {
		cum = append(cum, cum[len(cum)-1]+primes[i])
	}
	found := 0
	for i := len(primes); i >= 0; i-- {
		for j := 0; i+j <= len(primes); j++ {
			t := cum[j+i] - cum[j]
			if t < 1000000 && a[t] {
				fmt.Println("%d", t)
				found = 1
				break
			}
			if t >= 1000000 {
				break
			}
		}
		if found == 1 {
			break
		}
	}
}
