package main
import "fmt"

func main() {
	nums := []int {1, 2, 3}
	target := 4
	result := twoSum(nums, target)
	fmt.Println(result)

}

func twoSum(nums []int, target int) []int {
	valueStore := make(map[int]int)
	var result []int
	for i:=0; i < len(nums); i++ {
		if value, ok :=valueStore[target - nums[i]]; ok {
			result = append(result, value, i)
			return result
		}
		valueStore[nums[i]] = i 
	}
	return result
}