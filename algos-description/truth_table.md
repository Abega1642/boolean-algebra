## Truth Table and Canonical Forms of Logical Functions

### Truth Table
A truth table is a mathematical table used to determine the output of a logical function for all possible input combinations. It provides a comprehensive representation of how the logical function behaves under every possible input scenario. The rows correspond to the combinations of input values, while the columns represent the inputs and the corresponding outputs.

For a logical function with `n` variables, the truth table contains `2^n` rows, each representing a unique combination of the inputs. This makes the truth table a fundamental tool in digital logic, boolean algebra, and logic circuit design.

### Canonical Forms
The **canonical forms** of a logical function are standard representations used to express the function systematically. They are particularly useful in simplifying and analyzing logical expressions. There are two primary canonical forms:

1. **Sum of Products (SOP)**: 
   - In this form, the logical function is expressed as a disjunction (OR) of minterms.
   - A minterm is a product (AND) of all input variables, where each variable appears either in its true form (e.g., `x`) or complemented form (e.g., `¬x` or `NOT x`).
   - Example: `F(x, y) = (x AND ¬ y) OR (¬ x AND y)`

2. **Product of Sums (POS)**:
   - In this form, the logical function is expressed as a conjunction (AND) of maxterms.
   - A maxterm is a sum (OR) of all input variables, where each variable appears either in its true form (e.g., `x`) or complemented form (e.g., `¬x` or `¬ x`).
   - Example: `F(x, y) = (x OR y) AND (¬ x OR ¬ y)`

### Relationship to the Truth Table
- **Minterms** correspond to rows in the truth table where the output is `1`. Each minterm represents a unique combination of inputs that result in a true output.
- **Maxterms** correspond to rows in the truth table where the output is `0`. Each maxterm represents a unique combination of inputs that result in a false output.

By constructing the truth table, you can derive both the SOP and POS forms, enabling a clear and systematic representation of the logical function.
