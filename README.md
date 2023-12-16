# Cryptarithmetic-Problem
Cryptarithmetic Problem is a type of constraint satisfaction problem where the game is about digits and its unique replacement either with alphabets or other symbols. In cryptarithmetic problem, the digits  (0-9) get substituted by some possible alphabets or symbols. The task in cryptarithmetic problem is to substitute each digit with an alphabet to get the result arithmetically correct.

## Implement Backtracking Algorithm for CSPs
### Project Description: 
Design and implement a program to solve Cryptarithmetic problems as shown below:

![image](https://github.com/ramyaaprasath/Cryptarithmetic-Problem/assets/75536064/67a98a59-6130-4c00-9d0d-4283cadc21ba)

where 𝑥1 to 𝑥13 can be any capital letter from A to Z; some letters may occur more than once. Each
letter stands for a distinct digit; the aim is to find a substitution of digits for letters such that the
resulting sum is arithmetically correct, with the added restriction that no leading zeros are allowed.
The domain for 𝑥9 is therefore {1}, the domain for 𝑥1 and 𝑥5 is {1,2, … , 9} and the domain for
variables 𝑥2 to 𝑥4, 𝑥6 to 𝑥8, and 𝑥10 to 𝑥13 is {0,1,2, … , 9}. You can introduce auxiliary variables
and specify their domains to represent carry overs from previous columns. After this, you can set
up a set of constraints for the problem.

### Implementation: 
Implement Backtracking Algorithm for CSPs to solve this problem. Implement the function SELECT-UNASSIGNED-VARIABLE in the algorithm by using the minimum remaining values and degree heuristics. Instead of implementing the least constraining value heuristic in the ORDER-DOMAIN-VALUES function, simply order the domain
values in increasing order (from lowest to highest). You can skip the implementation of the INFERENCE function.

### Input and output files: 
The program will read in values from an input text file and produce an output text file that contains the solution.
