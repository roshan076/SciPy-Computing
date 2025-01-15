# Tower of Hanoi

This Python code solves the classic Tower of Hanoi problem using recursion. The Tower of Hanoi puzzle involves moving a set of disks from one pole (source) to another (target) while using a third pole as an auxiliary. The rules are:

1. Only one disk can be moved at a time.
2. A disk can only be placed on top of a larger disk or on an empty pole.
3. The objective is to move all disks from the source pole to the target pole.

---
## Code Breakdown

### Constants and Initial Setup
- `NUMBER_OF_DISKS = 4`: The number of disks to be moved.
- `A = list(range(NUMBER_OF_DISKS, 0, -1))`: A list representing the source pole (A) with disks ordered from largest (4) to smallest (1).
- `B = []`: An empty list for the auxiliary pole (B).
- `C = []`: An empty list for the target pole (C).

### Recursive Function
The function `move(n, source, auxiliary, target)` is a recursive function that solves the Tower of Hanoi problem by moving `n` disks from the `source` pole to the `target` pole using the `auxiliary` pole.

#### Base Case
- The recursion ends when there are no disks to move (`n <= 0`).

#### Recursive Steps
1. Move `n-1` disks from source to auxiliary: The function first moves the top `n-1` disks from the source pole to the auxiliary pole to make room for the largest disk.

2. Move the nth disk from source to target: The nth (largest) disk is moved directly from the source pole to the target pole.

3. Move the `n-1` disks from auxiliary to target: Finally, the `n-1` disks previously moved to the auxiliary pole are transferred to the target pole, completing the process.

---

## Initial Function Call
- The initial call to `move(NUMBER_OF_DISKS, A, B, C)` starts the process by moving all disks from the source (A) to the target (C) using the auxiliary (B).

---

## Output

The program will print the status of the poles (`A`, `B`, and `C`) at each step of the process. It shows how the disks are moved between the poles until all disks are successfully transferred to the target pole (C).