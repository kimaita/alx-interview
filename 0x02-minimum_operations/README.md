# Minimum Operations

In a text file, there is a single character `H`. Your text editor can execute only two operations in this file:

1. **Copy All**
2. **Paste**

Given a number `n`, write a method that calculates the fewest number of operations needed to result in exactly `n` `H` characters in the file.

- Prototype:  
`def minOperations(n)`
- Returns:  
 `int`: Number of minimum operations or if `n` is impossible to achieve, 0

## Example:

```
n = 9

H => Copy All => Paste => HH => Paste =>HHH => Copy All => Paste => HHHHHH => Paste => HHHHHHHHH
```

Number of operations: **6**
