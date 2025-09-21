# Algorithm analysis
Now let's analyze the complexity of the Simultaneous Min. Max. algorithm, implemented in [main.py](code/main.py).

[1. Asymptotic complexity analysis by counting operations](#asymptotic-complexity-analysis-by-counting-operations)

[2. Asymptotic complexity analysis using the Master Theorem](#asymptotic-complexity-analysis-using-the-master-theorem)


---

## Asymptotic complexity analysis by counting operations
The following table summarizes the number of comparisons `C(n)` for a list of n elements.

| Base  | Condition    | Comparisons |Notes      
|------|--------------|-------------------------|----------------|
| Base (n = 1) | 1-number-list | 0 | The single element is already the min. and the max. |
| Base (n = 2) | 2 numbers-list | 1 | A comparison to decide which is the max. and which is min.  |
| Geral (n > 2)  | Bigger list    | `2 * C(n/2) + 2`  | Divide into two sublists, solve recursively, and combine with 2 comparisons. |

- Base case: when the list has 2 elements, we make 1 comparison to find the maximum and minimum. Therefore, C(2)=1.
- Recursive step: for a list of size n, we divide the list into two halves of size n/2. The number of comparisons to solve the two sublists is `2 * C(n/2)`.
- After the subroutines return the maximums and minimums of the two halves, we need 2 additional comparisons to find the final maximum (comparing the two maximums) and the final minimum (comparing the two minimums).

The recurrence equation is: `C(n)= 2 * C(n/2) + 2`

Now, let's expand this equation to find a pattern.

`C(n)= 2 * C(n/2) + 2`
`C(n)= 2 * [2 * C(n/4) + 2] + 2 = 4 * C(n/4) + 4 + 2`
`C(n)= 4 * [2 * C(n/8) + 2] + 6 = 8 * C(n/8) + 8 + 6`
`C(n)= 8 * C(n/8) + 14`

Let's generalize the pattern for `k` expansions: `C(n)= 2^k * C(n/2^k) + 2 * (2^k − 1)`

We continue expanding until we reach our base case, where the size of the sublist is 2. This happens when `n/2^k = 2`, which means `2^k = n/2`.

Substituting `2k` into our equation: `C(n) = (n/2) * C(2) + 2 * (n/2 − 1)`

Since we know that `C(2) = 1`: 
`C(n) = (n/2) * 1 + 2 * (n/2 − 1)`
`C(n) = n/2 + n − 2`
`C(n) = 3n/2 − 2`

Conclusion: the total number of comparisons is `C(n)= 3n/2 ​− 2`. Therefore, the asymptotic complexity of the algorithm is `O(n)`.


---

## Asymptotic complexity analysis using the Master Theorem
1. Identification of parameters
The general formula of the Master Theorem is `𝑇(n) = a * 𝑇 (n/b) + f(n)`. Comparing it with the recurrence of our algorithm (`𝑇(𝑛) = 2𝑇 * (𝑛 / 2) + 𝑂(1)` ), we have:

- `a`: the number of subproblems in the recursion. In our case, the algorithm is divided into two halves, so `a = 2`.
- `b`: the factor by which the size of the problem is reduced. Since the list is divided in half, `b = 2`.
- `f(n)`: the cost of the division and combination work outside the recursive calls. The cost of dividing the list (finding the midpoint) and combining the results (two comparisons) is constant, so `f(n) = O(1)`.

2. Calculating the critical exponent
The next step is to calculate the value of `n^logb(a)`. This value serves to determine which case of the theorem applies.

`logb(a) = log2(2) = 1`
​
Therefore, the value we compare with f(n) is `n^1 = n`.

3. Determining the Master Theorem case
Now, we compare `f(n)` with `n^logb(a)` to determine which of the three cases applies.

- `f(n) = O(1)`
- `n^logb(a) = n`

Since `O(1)` is asymptotically smaller than `n`, the recurrence fits into Case 1 of the Master Theorem.

4. Solution to the recurrence
According to Case 1, if `f(n) = O(n^logb(a−ϵ))`, then the solution to the recurrence is `𝑇(n) = Θ(n^logb(a))`.

`𝑇(n) = Θ(n^logb(a))`
`𝑇(n) = Θ(n^log2(2))`
`𝑇(n) = Θ(n^1)`
`𝑇(n) = Θ(n)`
​
The asymptotic complexity of the MaxMin Select algorithm is `O(n)`. This means that the execution time grows linearly with the size of the list, making it a very efficient algorithm for this problem.