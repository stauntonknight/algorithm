package main

import (
    "fmt"
)

func main() {
    var i int
    for {
        n, err := fmt.Scanf("%d", &i)
        if err != nil {
            fmt.Println(n, err)
        }
        if i == 42 {
            break
        }
        fmt.Println(i);
    } 
}
