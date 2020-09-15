/*
Given two strings s and t , write a function to determine if t is an anagram of s.
Example 1:
Input: s = "anagram", t = "nagaram"
Output: true
Example 2:
Input: s = "rat", t = "car"
Output: false
https://leetcode.com/problems/valid-anagram/
*/
package main

import (
	"fmt"
	"sort"
	"strings"
)

func isAnagram(s string, t string) bool {
	ss := strings.Split(s, "")
	sort.Strings(ss)
	st := strings.Split(t, "")
	sort.Strings(st)
	return strings.Join(st, "") == strings.Join(ss, "")
}

func main() {
	fmt.Println(isAnagram("anagram", "nagaram"))
}
