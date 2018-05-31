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
    > ${5 \choose 2}{4 \choose 2}{2 \choose 2}$.

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

## Inclusion Exclusion Principle
> $$P(\cup_{i = 1}^n A_i) = \cup_{i} P(A_i) - \cup_{i < j} P(A_iA_j) + \cup_{i < j < k}P(A_iA_jA_k) - ...$$

Example: Suppose that 2 fair 6 sided dce are rolled. What is the probability that at least 1 of the dice shows a 6?
> $P(A) = 1 - P(A^c) = 1 - (\frac{5}{6})^2 = 1 - \frac{25}{36} = \frac{11}{36}$.

Example: There are 6 stops on the subway and 4 passengers on the subway car. Assume the passengers are equally likely to get off at any stop. Find the probability that:
> $|S| = 6^4$.
1. The passengers all get off at different stops.
2. 2 passengers get off at stop 2 and 2 passengers get off at stop 5.
3. 2 passengers get off at 1 stop and the other 2 passengers get off at another 1 stop.
    > $|A| = {6 \choose 2}{4 \choose 2}{2 \choose 2}$.

Example: 5 tourists plan to attent Octoberfest. There are 7 locations possible. Find the probability that:
> $|S| = 7^5$
1. All tourist attend different locations.
2. The tourists all attend the same location.
3. 2 tourists attend 1 location and 3 tourists attend another location.
    > $|A| = {7 \choose 2} \cdot 2 \cdot {5 \choose 2}{3 \choose 3} = 7 \cdot 6 \cdot {5 \choose 2}{3 \choose 3}$.

Example: Consider rearranging the "NOOB" at random. Let $A$ represent the event that two "O"s appear together, and let $B$ denote the event that the word starts with the letter $N$. Determine.
1. $P(A) = \frac{3!}{\frac{4!}{2!}} = \frac{1}{2}$
2. $P(B) = \frac{3!}{4!} = \frac{1}{4}$
3. The probability that the resulting word does not start with "N" and that the "O"s do not appear together. $P(\overline{A} \cap \overline{B}) = P(\overline{A \cup B})$.

Two events $A$ and $B$ are said to be **indepenedent** if $P(A \cap B) = P(A)P(B)$.

Example: Consider rolling 2 fair 6 sided dice. $A$ is the event where the sum is 10. $B$ is the event that the first die rolls a 6. $C$ is the event that the sum is 7. Are $A$ and $B$ independent?
> $B = \{(6, i) \mid i \in \{1, ..., 6\}\}$. $A = \{(5, 5), (6, 4), (4, 6)\}$. We can see that $A$, $B$ are not independent.

If *knowing* $A$ restricts our choices for $B$, they are not independent.

Two events $A$ and $B$ are **mutually exclusive** if $A$ and $B$ are disjoint.

**Proposition**: Suppose that not both $A$ and $B$ are trivial events. If $A$, $B$ are indepenent **and** mutually exclusive, then either $P(A) = 0$ or $P(B) = 0$.

**Proposition**: If $A$ and $B$ are independent, then $\overline{A}$ and $\overline{B}$ are independent, $A$ and $\overline{B}$ are independent, and $\overline{A}$ and $B$ are independent.

**Definition**: Conditional probabilty of $A$ given $B$, so long as $P(B) > 0$, is denoted by $P(A \mid B) = \frac{P(A \cup B)}{P(B)}$.

**Definition**: For events $A$ and $B$, $P(A \cap B) = P(A \mid B)P(B) = P(B \mid A)P(A)$.

**Bayes Theorem**: $P(B_i | A) = \frac{P(A|B_i)P(B_i)}{\sum_{j = 1}^k P(A | B_j)P(B_j)}$

Example: Pick Pharah, 20% chance of loss. Pick Winston, 10% chance of loss. Pick Winston 70% of the time, Pharah 30% of the time. Given that the game was lost, what is the probability that Pharah was picked?
> $$\begin{aligned}P(Pharah | Loss) &= \frac{P(Loss | Pharah)P(Pharah)}{P(Loss)} \\ &= \frac{0.2 \cdot 0.3}{P(Loss | Pharah)P(Pharah) + P(Loss | Winston)P(Winston)} \\ &= \frac{0.2 \cdot 0.3}{0.2 \cdot 0.3 + 0.1 \cdot 0.7} \\ &= 0.461
> 5\end{aligned}$$

**Probablity Function**: $f_X(x) = P(X = x)$.
1. $0 \le f_X(x) \le 1$.
2. $\sum_{x \in X(S)}f_X(x) = 1$.

**Cumulative Distribution Function (*CDF*)**: $F_X(x) = P(X \le x)$, $x \in \mathbb{R}$. We can use $P(X \le x) = P(\{\omega \in S: X(\omega) \le x\})$.
1. $0 \le F_X(x) \le 1$.
2. $F_X(x) \le F_X(y)$ for $x < y$.
3. $\lim_{x \to -\infty}F_x(x) = 0$, and $\lim_{x \to \infty}F_X(x) = 1$.

Example: $N$ balls labelled $1, 2, ..., N$ are placed in a box, and $n \le N$ are randomly selected without replacement. Find $P(X = x)$ where random variable $X$ is the largest number selected.
> **pdf**: There is only 1 way to select $x \in \{1, ..., n\}$. There are ${x - 1 \choose n - 1}$ ways to pick the remaining $n - 1$ balls. $P(X = x) = \frac{x - 1 \choose n - 1}{N \choose n}$, $x \ge n$. $P(X \le x) = \frac{x \choose n}{N \choose n}$, $x \ge n$.
>
> Now we use the property of **pdf**.
> $$\begin{aligned}P(X = x) &= F(x) - F(x - 1) \\ &= \frac{x \choose n}{N \choose n} - \frac{x - 1 \choose n}{N \choose n} \\ &= \frac{x - 1 \choose N - 1}{N \choose n}\end{aligned}$$