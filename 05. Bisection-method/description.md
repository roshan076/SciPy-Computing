# Bisection Method

This Python module implements the bisection method to find the square root of a given number (`square_target`). It uses binary search within a specified tolerance level to iteratively approximate the square root.

---

## Function Overview

The function `square_root_bisection` calculates the square root of a number using the bisection method. The bisection method works by repeatedly narrowing down the range where the square root lies until the difference between the square of the midpoint and the target number is within a specified tolerance.

### Parameters:
- `square_target`: The number for which the square root is to be computed. Should be a non-negative number.
- `tolerance`: The acceptable error for the approximation. Default is `1e-7`.
- `max_iterations`: The maximum number of iterations to perform. Default is `100`.

### Returns:
- `root`: The approximate square root of the target number.
  
### Edge Cases:
- If `square_target` is less than 0, a `ValueError` is raised because square roots of negative numbers are not defined in the real number system.
- If `square_target` is 0 or 1, the function directly returns 0 or 1 as the square root without further calculations.

---

## Process:
1. If `square_target` is 0 or 1, the function returns the exact value.
2. For values greater than 1, the bisection method is used:
   - The search space is initialized with `low = 0` and `high = max(1, square_target)`.
   - In each iteration, the midpoint is calculated and its square is compared to the target.
   - If the square of the midpoint is sufficiently close to the target (within the tolerance), the method converges and the result is returned.
   - Otherwise, the search range is updated (`low` or `high` is adjusted) and the process repeats.

---

## Example Usage:

```python
square_root_bisection(1)
# Output: The square root of 1 is 1

square_root_bisection(256)
# Output: The square root of 256 is approximately 16.0

square_root_bisection(856)
# Output: The square root of 856 is approximately 29.268457984859467