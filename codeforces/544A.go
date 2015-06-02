package main

import (
	"fmt"
)

func main() {
	var count int
	var s string
	fmt.Scan(&count)
	fmt.Scan(&s)
	var chars [26]bool
	var indexes []int
	if count == 1 {
		fmt.Println("YES")
		fmt.Println(s)
		return
	}
	for i := 0; i < len(s); i++ {
		if chars[s[i]-'a'] == false {
			chars[s[i]-'a'] = true
			indexes = append(indexes, i)
			if len(indexes) == count {
				break
			}
		}
	}
	if len(indexes) == count {
		indexes = append(indexes, len(s))
		fmt.Println("YES")
		for i := 0; i < count; i++ {
			fmt.Println(s[indexes[i]:indexes[i+1]])
		}

	} else {
		fmt.Println("NO")
	}
}
