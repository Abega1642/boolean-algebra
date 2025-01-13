# Boolean algebra program

Boolean algebra is one of the most important part of Logic. Not only in Logic but also in Mathematics and Computer science.

One of the most important part of this is the truth table and the karnaugh table of logical function
that allows us to understand the behaviors of the logical function or more important to simplify that last.

This repository is about that topic and holds programs that helps people to do so with just few steps.

The programs are written in `PYTHON (v3.11)`.

## Structures :

    ├── algos-description/
    │   ├── karnaugh_table.txt
    │   ├── truth_table.txt
    ├── tools/
    │   ├── utils/
    │   │   ├── tools.py
    │   ├── karnaugh_table.py
    │   ├── truth_table.py
    ├── README.md


### TOOLS :

`tools` directory holds the programs and the utils that are needed.

#### UTILS:

The `utils` directory holds the tools (functions) that are commonly used to implement the programs.

### ALGOS-DESCRIPTION :

`algos-description` will holds the algorithm description of the programs

## About the programs :

#### Truth table :

In this first section, the purpose is to define the `truth table` and the `cannonical forms`of any given logical function.

###### _How does this program work ?_

The program will first ask you how many variables your function contains.

    Please enter the number of variable of your logical function ?  → 

Then, it will ask you to name all of your variables. For this example, I'll name my variables as `a`, `b` and `c` ...

    Please, enter the name of the variable number 1: a
    Please, enter the name of the variable number 2: b
    Please, enter the name of the variable number 3: c
    Please, enter the name of the variable number 4: d
    ...

After that, the program will ask you to enter the logical function by using and respecting those boolean operators :``not`` or ``not_``, ``and`` , ``or``

``Warning !: only one space is allowed between variables and operators.``

Exemple :

    Please enter your logical function. ('not' or 'not_' : negation, 'and', 'or')
        ==> f(a,b,c,d) = a and b and not_c or not c and d
    
same as 

    f(a,b,c,d) = a.b.(non c) + (non c).d

Or mathematically as : 

    f(a,b,c,d) = a⋅b⋅(¬c) + (¬c)⋅d


**_NOTICE :_** The main function to run is the function named `table_of_truth` :
    
    table_of_truth()

In order to run the program, type :
    
    ┌─[user@server] - [../../..] - [9717]
    └─[$] python3 truth_table.py

Finally, the results will appear :
    
    a  ||  b  ||  c  ||  d  ||  f(a,b,c,d) = a and b and not_c or not c and d
    =========================================================================
    1  ||  1  ||  1  ||  1  ||         0
    1  ||  1  ||  1  ||  0  ||         0
    1  ||  1  ||  0  ||  1  ||         1
    1  ||  1  ||  0  ||  0  ||         1
    1  ||  0  ||  1  ||  1  ||         0
    1  ||  0  ||  1  ||  0  ||         0
    1  ||  0  ||  0  ||  1  ||         1
    1  ||  0  ||  0  ||  0  ||         0
    0  ||  1  ||  1  ||  1  ||         0
    0  ||  1  ||  1  ||  0  ||         0
    0  ||  1  ||  0  ||  1  ||         1
    0  ||  1  ||  0  ||  0  ||         0
    0  ||  0  ||  1  ||  1  ||         0
    0  ||  0  ||  1  ||  0  ||         0
    0  ||  0  ||  0  ||  1  ||         1
    0  ||  0  ||  0  ||  0  ||         0

    ==> The first canonic form of the logical function is : f(a,b,c,d) = : a*b*(not c)*d + a*b*(not c)*(not d) + a*(not b)*(not c)*d + (not a)*b*(not c)*d + (not a)*(not b)*(not c)*d

    ==> The second canonic form of the logical function is f(a,b,c,d) = : [(not a) + (not b) + (not c) + (not d)] * [(not a) + (not b) + (not c) + d] * [(not a) + b + (not c) + (not d)] * [(not a) + b + (not c) + d] * [(not a) + b + c + d] * [a + (not b) + (not c) + (not d)] * [a + (not b) + (not c) + d] * [a + (not b) + c + d] * [a + b + (not c) + (not d)] * [a + b + (not c) + d] * [a + b + c + d]


## Karnaugh Table :
This purpose of this next section is the Karnaugh table``karnaugh table``.

###### _How does this program work ?_

The same principle is hold for this karnaugh table program : the program will ask you the number of variable,
and the names of those last, and the logical function.

By the way, only one difference occurs. The program will ask you the number of variable you want to put in the
horizontal side of the `karnaugh table`.

Let's continue the example we took above and put 2 as the number of horizontal variables :

    Please, enter the number of variable in the horizontal line of the karnaugh table : → 2

_**NOTICE**_ : The main function to run is the function named `karnaugh_table` :
    
    karnaugh_table()

In order to run the program, type :
    
    ┌─[user@server] - [../../..] - [9717]
    └─[$] python3 karnaugh_table.py

Finally, the result will appear :

    ab     00 | 01 | 11 | 10
    cd   || ===================
    00   || 1  | 0  | 1  | 1
    01   || 1  | 1  | 1  | 1
    11   || 1  | 1  | 1  | 1
    10   || 0  | 0  | 1  | 1


