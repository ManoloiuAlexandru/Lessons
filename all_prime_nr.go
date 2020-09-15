/*
Given a number n, print all primes smaller than or equal to n.
Example:
Input : n =10
Output : 2 3 5 7
Input : n = 20
Output: 2 3 5 7 11 13 17 19
*/
package main

import (
	"fmt"
)

func prime(number int) bool {
	for div := 2; div < number/2+1; div++ {
		if number%div == 0 {
			return false
		}
	}
	return true
}

func main() {
	const given_nr = 20
	for nr := 2; nr <= given_nr; nr++ {
		if prime(nr) == true {
			fmt.Println(nr)
		}
	}
}
