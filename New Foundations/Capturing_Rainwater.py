"""
Imagine a very heavy rainstorm over a highway that has many potholes and cracks. The rainwater will collect in the empty spaces in the road, creating puddles. Each puddle can only be as high as the road around it, as any excess water will just flow away.

The capturing rainwater problem asks you to calculate how much rainwater would be trapped in the empty spaces in a histogram (a chart which consists of a series of bars).
"""
def efficient_solution(heights):
  total_water = 0
  left_pointer = 0
  right_pointer = len(heights) - 1
  left_bound = 0
  right_bound = 0

  # Write your code here
  while left_pointer < right_pointer:
    if heights[left_pointer] <= heights[right_pointer]:
      left_bound = max(heights[left_pointer], left_bound)
      total_water += left_bound - heights[left_pointer]
      left_pointer += 1
    else:
      right_bound = max(heights[right_pointer], right_bound)
      total_water += right_bound - heights[right_pointer]
      right_pointer -= 1
  return total_water
    
test_array = [4, 2, 1, 3, 0, 1, 2]
print(efficient_solution(test_array))
