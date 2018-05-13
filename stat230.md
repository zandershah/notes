STAT 230
=

Example: Suppose you have 20 distinct books, 7 of which are written by Mark Twain.

1. How many ways can you arrange 12 books on a shelf if exactly 3 of them must be Mark Twain books?
    > ${7 \choose 3}{13 \choose 9}$ ways to choose subsets.     
    > Books can be rearranged in $12!$ ways.    
    > Therefore, the answer is $12!{7 \choose 3}{13 \choose 9}$.

Example: Consider drawing 3 numbers at random **with** replacement from the digits 0 to 10. What is the probability that there is a repeated number among the 3.
> We can consider the complement, where there are no repeated numbers.  
> $1 - \frac{10 \cdot 9 \cdot 8}{10^3}$

Example: Suppose there are 4 passengers on an elevator that services 5 floors. Each passenger is equally likely to get off at any floor.
> $|S| = 5^4$

1. What is the probability that the passengers all get off on different floors?
    > $|A| = 5^{(4)}$. Therefore $P(A) = \frac{5^{(4)}}{5^4}$.
2. 2 passengers get off on floor 2, and 2 get off on floor 3.
    > $|A| = {4 \choose 2}{2 \choose 2}$. Therefore $P(A) = \frac{{4 \choose 2}{2 \choose 2}}{5^4}$.
3. 2 passengers get off on one floor, and 2 passengers get off on another floor.
    > $3{5 \choose 2}{4 \choose 2}{2 \choose 2}$.

Example: Consider rearranging the letters at random in the name "ZENYATTA" to form a single 'word'.
1. How many ways can this be done?
    > $|S| = {8 \choose 2}{6 \choose 2}{4 \choose 1}{3 \choose 1}{2 \choose 1}{1 \choose 1} = \frac{8!}{2!2!}$.
2. What is the probaility that all of the letters appear in alphabetical order?
    > A = { "AAENTTYZ" }. Therefore $P(A) = \frac{1}{|S|}$.
3. What is the probability that the word begins and ends with "T"?.
    > $|A| = {6 \choose 2}{4 \choose 1}{3 \choose 1}{2 \choose 1}{1 \choose 1}$.

${n \choose n_1}{n - n_1 \choose n_2}...{n_k \choose n_k} = {n \choose n1,n2,...,n_k}$.

Example: Harold's daily morning ritual is to drink 5 cans of pop. He has 2 cans of pop C, 2 cans of pop F, and 1 can of pop P. How many ways can he complete the ritual?
> $|A| = \frac{5!}{2!2!} = 30$.

Example: Find the probability that a bridge hand (13 cards picked at random from a standard deck without replacement) has ...
> $|S| = {52 \choose 13}$.
1. 3 aces.
    > $|A| = {4 \choose 3}{48 \choose 10}$. Therefore $P(A) = \frac{{4 \choose 3}{48 \choose 10}}{52 \choose 13}$.
2. At least 1 ace.
    > Consider the complement. $|A^c| = {48 \choose 13}$. Therefore $P(A) = 1 - \frac{48 \choose 13}{52 \choose 13}$.
3. 6 spaces, 4 hearts, 2 diamonds, 1 club.
    > $|A| = {13 \choose 6}{13 \choose 4}{13 \choose 2}{13 \choose 1}$. Therefore $P(A) = \frac{{13 \choose 6}{13 \choose 4}{13 \choose 2}{13 \choose 1}}{52 \choose 13}$.

For verifying your answer when counting across disjoint unions, adding up the top and bottom numbers for the ${n \choose k}$ in $|A|$ should add up to $|S|$.

Example (*Team captain problem*): Show that ${n \choose k} \cdot k = {n -1 \choose k - 1} \cdot n$.
> We are either picking the team first and then choosing the captain, or the other way around.

Example (*Vandermonde's Identity*): Show that ${n + m \choose k} = \sum_{i = 0}^k {n \choose i}{m \choose k - i}$ for non-negative integers $n, m, k$.