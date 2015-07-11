package main

import (
	"fmt"
	"strconv"
)

func calc(part string) int {
	fmt.Println(part)
	softened := make([]int, 0)
	for i:= 0; i < len(part) ; i++ {
		if i%2 == 0 {
			temp,_ :=strconv.Atoi(part[i:i+1])
			softened = append(softened, temp)
		} else if (part[i] == '*') {
			i = i + 1
			x,_ := strconv.Atoi(part[i:i+1])
			t := softened[len(softened) - 1] * x
			softened[len(softened)-1] = t
		}
	}
	a:=0
	for i:= 0; i < len(softened); i++ {
		a = a+ softened[i]
	}
	fmt.Println(a)
	return a
}

func main() {
	var s string
	fmt.Scan(&s)
	n := len(s)/2 + 1
	dp := make([][]int, n)
	for i := range dp {
		dp[i] = make([]int, n)
	}
	for i := range dp {
		for j := i; j < n; j++ {
			dp[i][j] = calc(s[2*i : 2*j + 1])
		}
	}
	max := 0
	for i := range dp {
		for j := i; j < n; j++ {
			if i != 0 && s[2*i - 1] == '+' {
				fmt.Println("No match i ", i,j, 2*i - 1)
				continue
			}
			if j != n-1 && s[2*j + 1] == '+' {
				fmt.Println("No match j ", i,j,2*j + 1)
				continue
			}
			now := 0
			fmt.Println("Checking :", i, j)
			if i > 0 {
				now = dp[0][i-1]
				switch s[2*i-1] {
				case '+':
					now = now + dp[i][j]
				case '*':
					now = now * dp[i][j]
				}
			} else {
				now = now + dp[i][j]
			}
			fmt.Println("Now :", now)
			if j < n-1 {
				fmt.Println("2*j + 1:", s[2*j+1:2*j+2])
				switch s[2*j+1] {
				case '+':
					now = now + dp[j+1][n-1]
				case '*':
					now = now * dp[j+1][n-1]
				}
			}
			fmt.Println("Now :", now)
			if max < now {
				fmt.Println("Changing max :", i, j, now)
				max = now
			}
		}
	}
	fmt.Println(max)
}
