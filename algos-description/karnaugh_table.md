## Karnaugh Table and Simplification of Logical Functions

### Karnaugh Table
A Karnaugh Table (K-map) is a graphical method used to simplify logical functions. It is a two-dimensional representation of a truth table, where each cell corresponds to a unique minterm of the function. The cells are arranged so that adjacent cells differ by only one variable, making it easy to identify patterns for simplification.

### Structure of the K-Map
For a logical function with `n` variables:
- The K-map contains `2^n` cells, each representing a minterm.
- The rows and columns are labeled using Gray code to ensure that adjacent cells differ by only one variable.

For example:
- A 2-variable K-map has 4 cells.
- A 3-variable K-map has 8 cells.
- A 4-variable K-map has 16 cells.

### Using the K-Map
1. **Populate the K-map**: Fill each cell with the output value (`0` or `1`) from the truth table corresponding to the minterm.
2. **Group adjacent ones**: Identify groups of 1s in the table that can form rectangles of size `1`, `2`, `4`, `8`, etc., ensuring the group sizes are powers of 2.
3. **Write the simplified expression**: Each group represents a simplified term in the logical expression.

### Example
#### 3-Variable Function
Given a truth table:

| A | B | C | Output |
|---|---|---|--------|
| 0 | 0 | 0 |   1    |
| 0 | 0 | 1 |   1    |
| 0 | 1 | 0 |   0    |
| 0 | 1 | 1 |   0    |
| 1 | 0 | 0 |   1    |
| 1 | 0 | 1 |   1    |
| 1 | 1 | 0 |   0    |
| 1 | 1 | 1 |   0    |

The corresponding K-map is:

| AB\C | 0 | 1 |
|------|---|---|
| 00   | 1 | 1 |
| 01   | 0 | 0 |
| 11   | 0 | 0 |
| 10   | 1 | 1 |

From the K-map, the simplified expression is:
`F(A, B, C) = ¬A ¬C + A¬C`

### Advantages of K-Maps
- Reduces complex logical functions into simplified forms.
- Minimizes the number of terms and literals in the expression.
- Useful for designing efficient digital circuits.
