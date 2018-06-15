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

> Let $P$ be the event that Pharah is picked. Let $L$ be the event where the game is lost. Let $W$ be the event that Winston is picked.
> $$\begin{aligned}P(P| L) &= \frac{P(L| P)P(P)}{P(L)} \\ &= \frac{0.2 \cdot 0.3}{P(L| P)P(P) + P(L| W)P(W)} \\ &= \frac{0.2 \cdot 0.3}{0.2 \cdot 0.3 + 0.1 \cdot 0.7} \\ &= 0.461
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

Example: Suppose a tack when flipped has probability $0.6$ of landing point up. If the tack is flipped $10$ times, what is the probability it lands point up more than twice?

> $X \in \{0, 1, 2, ..., 10\}$, $X \sim Bin(n = 10, p = 0.6)$   .
>
>  We want $P(X \ge 3) = 1 - P(X < 2) = 1 - (0.6^{10} + {10 \choose 1}0.6^9 0.4 + {10 \choose 2}0.6^8 0.4^2)$.

Example: Suppose a fair coin is flipped 17 times. Let $X$ denote the number of heads observed, and let $Y$ denote the number of tails observed. Which of the following is false?

> - $X \sim Binomial(17, 0.5)$.
> - $Y \sim Binomial(17, 0.5)$.
> - $X \sim Y$ (*X follows the distribution of Y*).
> - $X + Y = 17$.
> - $X = Y$ (*False, because RV quantity is not fixed*).

Example: Weekly lottery has a probability of 0.02 of winning a prize with a single ticket. If you buy one ticket per week for 52 weeks, what is the probability that you ...

> $X \sim Bin(n=52, p=0.02)$.

1. Win no prizes?

    > We want $P(X = 0) = 0.98^{52}$.

2. Win 3 or more prizes?

    > We want $P(X \ge 3) = 1 - (P(X = 0) + P(X = 1) + P(X = 2))$.

Binomial and hypergeometric distributions are fundamentally different, as the former picks with replacement, whereas the latter picks without replacement.

**Theorem**: If $r$ and $N$ relatively larger than $n$ and $\frac{r}{N} = p$ where $p \in [0, 1]$, then if $X \sim Hypergeometric(N, r, n)$ and $Y \sim Binomial(n, p)$ then $P(X \le k) \approx P(Y \le k)$.

Example: In Overwatch there are 27 playable characters, of which 6 are considered "Tanks". Suppose that three characters are drawn at random.

1. What is the probability that the selection contains exactly 2 tanks.

    > We want $P(T = 2) = \frac{{6 \choose 2}{21 \choose 1}}{27 \choose 3} \approx 0.1077$.

2. Approximate this probability using binomial distribution.

    > $T_{Bin} \sim Bin(3, \frac{6}{27})$.  
    >
    > We want $P(T_{Bin} = 2) = {3 \choose 2}(\frac{6}{27})^2(\frac{21}{27}) \approx 0.1152$.

## Negative Binomial
Question: We want the number of tails until you get the first head.
$$P(X = x) = (1-p)^xp,\ x = 0,1...$$

Question: If I model the total number of coin flips until I get the first head, is this also a geometric distribution? **Yes** because it is essentially the same as the last question.

We generalize to $k$ successes by noticing that the last trial must produce the $k$th success and the remaining $k-1$ successes may appear anywhere from the $1$st to $2$nd last trial.
$${r + k - 1 \choose k - 1}p^k(1-p)^r$$

Example: There is a 50.4% change of flipping a head. What is the probability that you need more than 5 flips to get a tail?

> $1 - P(X \le 4) = 1 - \sum_{x = 0}^4 0.504^x (1 - 0.504)$.;

Exampe: Hanzo is getting more popular. Every time I join a new game, I have a 15% change of picking Hanzo. What is the probability that ...

> Let $W$ be the number of games played before I pick Hanzo. $W \sim Geo(0.15)$. We have $f_W(w) = (1-p)^wp$, $w \in \mathbb{N}_0$.

1. I will need to play 4 games before I get to pick Hanzo?

    > $P(W = 4) = f_w(4) = (0.85)^40.15 = 0.0783$.

2. I will need to play at least 4 games before I get to pick Hanzo, given that I have to play at least 3 games before I pick him?

    > $(P(W \ge 4 | W \ge 3) = \frac{P(W \ge 4 \cap W \ge 3)}{P(W \ge 3)} = \frac{P(W \ge 4)}{P(W \ge 3)} = 0.85$.
    >
    > $$\begin{aligned}P(W \ge w) &= \sum_{t=w}^\infty (1-p)^tp \\ &= p(1-p)^w\sum_{t=0}^\infty (1-p)^t \\ &= p(1-p)^w\frac{1}{1 - (1-p)} \\ &= (1-p)^w\end{aligned}$$

3. I will need to play at least one game before I get to pick Hanzo?

    > $P(W \ge 1) = 1 - P(W = 0) = 1 - p = 0.85$.

## Memoryless Property of Geometric
Let $X \sim Geo(p)$ and $s, t$ be non-negative integers.
$$P(X \ge s + t | X \ge s) = P(X \ge t)$$

Example: Mobile game "Show Me The Money". Game released super rate item which only appears from a loot box which costs $2 per box, with the change of 0.01%.

> Let $X$ be the number of boxes without the rare item.

1. What is the probability that he will need to buy 50 loot boxes to get 2 super rate items?

    > Number of success is fixed but not the number of trials, so we use negative binomial. $X \sim NB(2, 0.0001)$.     
    >
    > We want $P(X = 48) = {48 + 2 - 1 \choose 2 - 1}(0.9999)^{48}(0.0001)^2 = 0.000000488$.

# Poisson
We say that a random variable $X \sim Poisson(\lambda)$ if we have $f_X(x)$ such that.
$$f_X(x) = e^{-\lambda}\frac{\lambda^x}{x!}$$

We verify that this is a valid probability distribution using the exponential series.
$$\begin{aligned}
\sum_{x=0}^\infty f_X(x) &= \sum_{x=0}^\infty e^{-\lambda}\frac{\lambda^x}{x!} \\
&= e^{-\lambda}e^\lambda \\
&= 1
\end{aligned}$$

One way to view poisson is to consider the limiting case of binomial, where you fix $\lambda = np$, and let $n \to \infty$ and $p \to 0$.

## Poisson Process

1. **Independence**: the number of occurences in non-overlapping intervals are independent.

2. **Individuality**: for sufficiently short periods of time, $\Delta t$, the probability of two or more events occuring in the interval approaches zero.

$$\lim_{\Delta t \to 0} \frac{P(\text{2 of more events in } (t, t + \Delta t))}{\Delta t} = 0$$

3. **Homogeneity or Uniformity**: events occur at a uniform or homogenous rate $\lambda$ and proportional to time interval $\Delta t$.

$$\lim_{\Delta t \to 0} \frac{P(\text{one event in } (t, t + \Delta t)) - \lambda \Delta t}{\Delta t} = 0$$

A process that satisfies the prior conditions on the occurrence of events is often called a **Poisson Process**. More precisely, if $X_t$, for $t \ge 0$, denotes the number of events that have occurred up to time $t$, then $X_t$ is called a **Poisson Process**.

Example: Website hits for a given website occur according to a Poisson process with a rate of 100 hits per minute. Find ...

1. $P(\text{1 hit is observed in a second}) = \frac{e^{-\frac{5}{3}}\frac{5}{3}^1}{1!}$
2. $P(\text{90 hits are observed in a minute}) = \frac{e^{-100}100^{90}}{90!}$

## Relation to Binomial

Consider one unit of time, so that the process follows $Poi(\lambda)$.

We chop up the interval into $n$ equally-sized pieces. If we chop it up finely enough, then by individuallity, the probability of two or more events occuring goes to 0.

This means that, over a small enough size, we approximately have either 0 or 1 event occuring with $P(event) = p$ for every piece.

Moreover, the event probability $p$ is proportional to the length of the interval by homogeneity. This means that as $n \to \infty$, $p \to 0$.

Finally, by independence, each $n$ pieces are independent, so we have $Bin(n, p)$, where $n$ is very large and $p$ is very small.

We expect to see $np$ events, recall that rate $\lambda$ is the rate of occurance over 1 unit of time. So $\lambda = np$, and as $n \to \infty$, $p \to 0$, in $Bin(n, p)$, we approach $Poi(np)$.

Example: A bit error occurs got a given data transmission method independently in out of of every 1000 bits transferred. Suppose a 64 bit message is sent using the transmission system.

1. What is the probability that there are exactly 2 bit errors?

    > $X \sim Bin(64, \frac{1}{1000})$, $P(X = 2) = {64 \choose 2}(\frac{999}{1000})^{62} (\frac{1}{1000})^2 \approx 0.019$.

2. Approximate using Poisson.       

    > $X \sim Poi(\frac{64}{1000})$, $P(X = 2) = \frac{e^{-\frac{64}{1000}}(\frac{64}{1000})^2}{2!} \approx 0.019$.

Example: Shiny versions of Pokemon are possible to encounter and catch starting in Generation 2 (Pokemon Gold / Silver).  Normal encounters with Pokemon while running in grass occur according to a Poisson process with rate 1 per minute on average. 1 in every 8192 encounters will be a Shiny Pokemon, on average.

1. If you run around in the grass for 15 hours, what is the probability you will encounter at least one Shiny Pokemon?

> $X \sim Poi(\frac{900}{8192})$. $P(X \ge 1) = 1 - P(X = 0) = 1 - e^{-\frac{900}{8192}}$. 

2. How long would you have to run around in grass to have better than 50 percent chance of encountering at least one Shiny Pokemon?

> Solve for $t$, where $0.5 = P(X_t \ge 1)$.

Example: An infinite number of Harolds are released in a gold mine. They scatter randomly, so that on average, a gold nugget is surrounded by 6 Harolds. Assume that all gold nuggets are of equal size.

> Let $H$ be the number of Harolds surrounding the nugget. $H \sim Poi(\lambda = 6\ Harolds / nugget)$.

1. What is the probability that a nugget is surrounded by more than 3 Harolds?

    > $$\begin{aligned}P(H > 3) &= 1 - P(H <= 3) \\ &= 1 - f(0) - f(1) - f(2) - f(3) \\ &=  0.8488 \\ f(x) &= \frac{e^{-6}6^x}{x!}\end{aligned}$$
    
2. When 10 nuggets are picked at random, what is the probability that 8 of those nuggets have more than 3 Harolds?

    > $Bin(n=10, p=0.8488)$. $P(N=8) = {10 \choose 8}(0.8488)^8(1-0.8488)^2$.

3. On 2 nuggets there are $t$ Harolds in total. What is the probability that $x$ of them are on the first of the two nuggets?

    > Let $A$ be the event that there are $t$ Harolds on 2 nuggets. Let $B$ be the event that there are $x$ Harolds on the first nugget. $P(B|A) = \frac{P(A \cap B)}{P(A)}$. Where $A \cap B$ is the event where $x$ Harolds are on the first nugget, and $t-x$ Harolds are on nugget 2.
    >
    > These events are independent, so $P(A \cap B) = \frac{e^{-6}6^x}{x!} \cdot \frac{e^{-6}6^{t-x}}{(t-x)!} = \frac{e^{-12}6^t}{x!(t-x)!}$.
    >
    > We can double the original rate, $Poi(12)$ for the denominator. So $P(A) = \frac{e^{-12}12^t}{t!}$.
    >
    > So $P(B|A) = {t \choose x}\frac{1}{2}^t$.

If you order a set of random variables, they become **order statistics**.

Question: Let $X_1, X_2, X_3$ denote the random variables for the outcome of three independent fair random number generators. Assume that their ranges are $\{1, 2, ..., 10\}$. Now let $X_{max}$ denote the maximum value, then $P(X_{max} \le x) = P(X_1 \le x)P(X_2 \le x)P(X_3 \le 3)$.

# Expectation

**Definition**: Let $x_1, x_2, ..., x_n$ be outcomes of random variable $X$. Its **sample mean** is defined as $\overline{x} = \frac{\sum_{i=1}^nx_i}{n}$.

We can calculate a theoretical mean of $X$ directly if we know its distribution. Suppose $X$ is a discrete random variable with probability function $f(x)$, then $E(X)$ is called the **expected value** of $X$ and is defined by $E(X) = \sum_{x \in X(S)}xf(x)$. The expected value is sometimes referred to as the **mean**, **expectation**, or **first moment** of $X$.

Example: A lottery is conducted in which 7 numbers are drawn without replacement between the numbers 1 and 50. A player wins the lottery if the numbers selected on their ticket match all 7 of the drawn numbers.  A ticket to play the lottery costs $1, and the jackpot is valued at $5000000.  Compute the expected return.

> If you win the lottery, the return is 4999999. If you did not win, the return is -1. Let $R$ denote the return amount. $E(R) = (-1)P(\overline{w}) + (4999999)P(w) < 0$.

## "Law of the Unconscious Statistiation"

If $g: \mathbb{R} \to \mathbb{R}$, then for a random variable $X$ with probability function $f(x), the expected value of $g(x) is given be $\sum_{x \in S(X)}g(x)f(x)$.

To retrieve our original expectation function, we set $g(x) = x$.

Example: If $g(x) = x^2$ and $X$ is the result of a fair six sided die roll, then compute $E[g(X)]$.

> $E[g(x)] = E[x^2] = \sum_{x = 1}^6 x^2 \frac{1}{6}$.

## Linearity of Expectation

If $g(x)$ is a linear function $g(x) = ax + b$, then for a random variable $X$, $E[aX + b] = aE[X] + b$.

> $$\begin{aligned}E[aX + b] &= \sum_{x \in X(S)}(ax + b)f(x) \\ &= a\sum_{x \in X(S)}xf(x) + b\sum_{x \in X(S)} \\ &= aE[x] + b\end{aligned}$$

Note: It is **not true** in general that $g(E[X]) = E[g(X)]$.

An extention of linearity is, $E[af(X) + bg(X)] = aE[f(X)] + bE[g(X)]$.

## Expectation of Binomial

> If $X \sim Bin(n, p)$ then $E[X] = np$.

$$\begin{aligned}
E[X] &= \sum_{x = 0}^n xf(x) \\
&= \sum_{x = 1}^n xf(x) \\
&= \sum_{x = 1}^n x \frac{n!}{x!(n-x)!}p^x(1-p)^{n-x} \\
&= \sum_{x=1}^n \frac{n(n-1)!}{(x-1)!((n-1) - (x-1))!}pp^{x-1}(1-p)^{(n-1)-(x-1)} \\
&= np(1-p)^{n-1} \sum_{x=1}^n \left({n - 1 \choose x-1}p^{x-1}(1-p)^{-(x-1)} \right) \\
&= np(1-p)^{n-1} \sum_{x=1}^n \left( {n-1\choose x-1} \left(\frac{p}{1 - p}\right)^{x-1} \right) \\
&= np(1-p)^{n-1} \sum_{y=0}^{n-1} \left( {n-1\choose y} \left(\frac{p}{1 - p}\right)^{y} \right) \\
&= np(1-p)^{n-1} \left(1+\frac{p}{1-p}\right)^{n-1} \\
&= np(1-p)^{n-1} \left(\frac{1}{1-p}\right)^{n-1} \\
&= np
\end{aligned}$$

Example: Suppose two fair six sided die are independently rolled 24 times, at let $X$ denote the number of times the sum of die rolls is 7. Compute $E[X]$.

> 36 outcomes, 6 yield a sum of 7, so $p = \frac{1}{6}$. We are rolling 24 times, so $n = 24$. We have $E[X] = np = 4$.

## Expectation of Poisson

> If $Y \sim Poi(\lambda)$, then $E[Y] = \lambda$.

$$\begin{aligned}
E[Y] &= \sum_{y \ge 0}yf(y) \\
&= \sum_{y \ge 1}y\frac{e^{-\lambda}\lambda^y}{y!} \\
&= \sum_{y \ge 1}\frac{e^{-\lambda}\lambda \lambda^{y-1}}{(y-1)!} \\
&= e^{-\lambda}\lambda \sum_{y \ge 1}\frac{\lambda^{y-1}}{(y-1)!} \\
&= e^{-\lambda}\lambda \sum_{z \ge 0}\frac{\lambda^{z}}{z!} \\
&= e^{-\lambda}\lambda e^{\lambda} \\
&= \lambda
\end{aligned}$$

Example: Suppose that calls to Canadian Tire Financial call center follow a Poisson process with rate 30 calls per minute. Let $X$ denote the number of calls to the center after 1 hour. Compute $E[X]$.

> $E[X] = 30 * 60$.

## Expectation of Hypergeometric

> If $X \sim hyp(N, r, n)$, then $E[X] = n\frac{r}{N}$.

## Expectation of Negative Binomial 

> If $Y \sim NB(k, p)$, then $E[Y] = \frac{k(1-p)}{p}$.

# Variability

Expectation along may not be enough. Oftentimes, we want to study how much a random variable tends to deviate from its mean.

1. **Deviation**: $E[X - \mu] = E[X] - \mu$.
2. **Absolute Deviation**: $E[|X - \mu|]$.
3. **Squared Deviation**: $E[(X - \mu)^2]$. Turns out to be a useful measure of variability.

## Variance

The **variance** of a random variable $X$ is denoted $Var(X)$ and is defined by $Var(X) = E[(X - E[X])^2]$. A simple calculation gives the *short cut formula*, $Var(X) = E[X^2] = E[X]^2$.

$$\begin{aligned}
E[(X - E[X])^2] &= E[X^2 - 2XE[X] + E[X]^2] \\
&= E[X^2] - 2E[X]^2 + E[X]^2 \\
&= E[X^2] - E[X]^2
\end{aligned}$$

We know that $E[(X - E[X])^2] \ge 0$ so we can say that $E[X^2] - E[X]^2 \ge 0$.

### Variance of Linear Combination

For any random variable $X$ and $a, b \in \mathbb{R}$.

$$ Var(aX + b) = a^2Var(X)$$

**Proposition**: $Var(X = 0)$ if and only if $P(X = E[X]) = 1$.

Example: Let $X$ denote the outcome of a fair six sided die. Compute $Var(X)$.

> **Recall**: $Var(X) = E[X^2] - E[X]^2$.   
> We know $X \in \{1, .., 6\}$, $X^2 \in \{1, ..., 36\}$.
>
> $E[X] = 3.5 = \frac{7}{2}$.   
> $E[X^2] = \sum x^2f(x) = \frac{1}{6}(1 + 4 + 9 + 16 + 25 + 36) = \frac{91}{6}$.
> So, $Var(X) = \frac{91}{6} - \frac{49}{4}$.

## Standard Deviation

> **Note**: $Var(X)$ is a squared unit. To recover the original unit, we take the square root of variance.

We define the **standard deviation** of a random variable $X$ as $SD(X)$, where $SD(X) = \sqrt{Var(X)}$.

## Variability of Binomial

> Suppose that $X \sim Bin(n, p)$. Then $Var(X) = np(1-p)$.

## Variability of Poisson

> Suppose that $X \sim Poi(\lambda)$. Then $Var(X) = \lambda$.

Example: Suppose that $X_n$ is binomial with parameters $n$ and $p_n$, so that $np_n \to \lambda$ as $n \to \infty$. If $Y \sim Poi(\lambda)$, show that $\lim_{n \to \infty} Var(X_n) = Var(Y)$.

## Variability of Hypergeometric

> Suppose that $X \sim hyp(N, r, n)$. Then $Var(X) = n\frac{r}{N}(1 - \frac{r}{N})(\frac{N - n}{N - 1})$.

## Variability of Hypergeometric

> Suppose that $Z \sim NB(k, p)$. Then $Var(Z) = \frac{k(1-p)}{p^2}$.