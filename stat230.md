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