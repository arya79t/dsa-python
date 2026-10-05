# Time and Space Complexity

Understanding time and space complexity is essential for analyzing how efficiently an algorithm performs as the input size increases.

## 1. What Does Big-O Mean?
The O means Order of growth. 
We're asking: As the input gets bigger, how does the amount of work or memory used by my algorithm grow?

- O(1)       Constant
- O(log n)   Logarithmic
- O(n)       Linear
- O(n log n) Linearithmic
- O(n²)      Quadratic

Eg for i in range(n):
    print(i)
n = 10       → roughly 10 iterations
n = 100      → roughly 100 iterations

So Time = O(n)

x = 10
y = 20
z = x + y
Whether your input has 10 elements or 10 million elements, these variables are still just: x, y, z

Space = O(1)

For data structures:
Eg 1:
def example(nums):
    total = 0

    for x in nums:
        total += x

    return total
    
nums → n elements
total → 1 variable
x → 1 variable
Therefore:
Time = O(n) ; Space = O(1)

Eg 2:
def example(nums):
    result = []

    for x in nums:
        result.append(x)

    return result
nums → n elements
result → n elements

The extra memory grows with n.
Therefore:
Time = O(n) ; Space = O(n)

# For Binary Search

It cuts the search space in half:
16 → 8       1 time halved
8 → 4        2
4 → 2        3
2 → 1        4

log₂(16) = 4
That's where the log comes from.

After k iterations:
n / 2^k

Eventually we reach 1:
n / 2^k = 1

Multiply both sides:
n = 2^k

Take log₂:
k = log₂(n)

Therefore, the number of iterations is: O(log n)
That's the mathematical reason.

Big-O describes growth rate, and constant factors don't matter. So we don't write O(n/2)
