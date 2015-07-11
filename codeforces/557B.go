package main

import "fmt"

func qsort(a []int) {
	if len(a) < 2 {
		return
	}
	track := 1
	k := 1
	for k < len(a) {
		if a[k] < a[0] {
			t := a[track]
			a[track] = a[k]
			a[k] = t
			track++
		}
		k++
	}
	a[track-1], a[0] = a[0], a[track-1]
	qsort(a[:track-1])
	qsort(a[track+1:])
}

func main() {
	w, n := 0, 0
	fmt.Scan(&n, &w)
	a := make([]int, 2*n)
	for i := 0; i < 2*n; i++ {
		fmt.Scan(&a[i])
	}
	qsort(a)
	mini := float32(a[0])
	if float32(a[n]) < float32(2*mini) {
		mini = float32(a[n]) / float32(2)
	}
	var total float32
	total = float32(3) * mini * float32(n)
	if total > float32(w) {
		wf := float32(w)
		wf = wf / 3
		wf = float32(int(wf*10000000)) / 10000000
		total = wf * 3
	}
	fmt.Println(total)
}
