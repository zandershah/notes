MATH239
=

# Enumeration

## Sets We Count 

1. **Catesian Products**, $A \times B = \{(a, b) | a \in A, b \in B\}$, $A^k = \{(a_1, ..., a_k)|a_i \in A\}$.
2. **Disjoint Union**, $S = S_1 \cup S_2$, $S_1 \cap S_2 = \emptyset$, then $|S| = |S_1| + |S_2|$.

**Binomial Coeff**: How many subsets of $\{1, ..., n\}$ have size $k$? ${n \choose k} = \frac{n!}{(n-k)!k!}$

**Binomial Theorem**: $(1 + x)^n = \sum_{k = 0}^n{n \choose k}x^k$. Proof using counting arguments.

> $(1 + x)^n = \sum a_1a_2...a_n, a_i \in \{1, x\}$  > Coeff $x^k$ represents the number of terms in the sum that have $x^k$. To get $x^k$, we need exactly $k$ "x", and $n - k$ "1". There are $n \choose k$ ways so the coeff of $x^k$ is $n \choose k$.

# Combinatorial Proofs

> Idea: Count a set of objects in 2 different ways. The results must be equal.

Example: $2^n = \sum_{k = 0}^n {n \choose k}$

> Let $S$ be the set of all binary strings of length $n$. Then $|S| = 2^n$. We count $S$ in a different way. Let $S_k$ be the set of all binary strings of length $n$ with exactly $k$ 0, $k = 0,...,n$. Then $S = \cup_{k = 0}^n S_k$. This is a disjoint union so $|S| = \sum_{k = 0}^n |S_k|$. For each $k$, $|S_k| = {n \choose k}$ since we are choosing exactly $k$ bits out of $n$ bits to be 0. So $2^n = \sum_{k = 0}^n {n \choose k}$.

Example: ${n \choose k} = {n - 1 \choose k} + {n - 1 \choose k - 1}$

> Let $S$ be the set of all subsets of $\{1, ..., n\} of size $k$. So $|S| = {n \choose k}$. Let $S_1$ be subsets that include the element $n$, let $S_2$ be the subsets that do not include the element $n$.   
> Each subset of $S_1$ consists of $\{n\}$ unin with $k - 1$ elements of $\{1, ..., n - 1\}$ so $|S_1| = {n - 1 \choose k - 1}$.    
> Each subset of $S_2$ consists of $k$ elements of $\{1, ..., n\}$, so $|S_2| = {n - 1 \choose k}$. 
> Since $S = S_1 \cup S_2$ is a disjoint union, $|S| = |S_1| + |S_2|$. The result follows.

Example: ${n + k \choose n} = \sum_{i = 0}^k {n + i - 1 \choose n - 1}$

> Let $S$ be all subsets of $\{1, ..., n + k\}$ of size $n$. Then $|S| = {n + k \choose n}$. Let $S_i$ be the subsets of $\{1, ..., n + k\}$ of size $n$ where the largest element is $n + i$. So $i = 0, ..., k$. Then $S = \cup_{i = 0}^k S_i$ is a disjoint union and $|S| = \sum_{i = 0}^k |S_i|$. Each subset $S_i$ consists of $\{n + i\}$ union with a subset of $\{1, ..., n + i - 1\}$ of size $n - 1$. So $|S_i| = {n + i - 1 \choose n - 1}$. The result follows.

A **bijection** $f: S \to T$.   

1. $f$ is **injective** if every element of $S$ is mapped to a distinct element in $T$.
2. $f$ is **surjective** if everything in the codomain is mapped to something in the domain.
3. $f$ is a **bijection** if $f$ is **injective** and **surjective**.

Assume $S, T$ are finite. If $f$ is injective, $|S| \le |T|$. If $f$ is surjective, $|S| \geq |T|$. It follows that if $f$ is a bijection, $|S| = |T|$.

**Theorem**: $f$ is a bijection if it has an inverse $f^{-1}$.  
An inverse of $f: S \to T$ is a function $f^{-1}: T \to S$ where for every $x \in S$, $f^{-1}(f(x)) = x$ and for every $y \in T$, $f(f^{-1}(y)) = y$.

Example: Let $S$ be all subsets of $\{1, ..., n\}$. Let $T$ be all binary strings of length $n$.

> Define $f: S \to T$ where $f(A) = s_ns_{n-1}...s2s1$.
> $$s_i \begin{cases}1, &\text{if } i \in A \\ 0, &\text{if } i \notin A\end{cases}$$
> By our definition, $f(A)$ is a binary string of length $n$ so $f(A) \in T$. The inverse $f^{-1}: T \to S$ where $f^{-1}(t_n...t_1) = \{i \in \{1, ..., n\} \mid t_i = 1\}$. So $f$ is a bijection and $|S| = |T| = 2^n$.

# Generating Series

Example: "How many subsets of $\{1, 2, 3\}$ have size $k$?". Define $S$ as the set of all subsets of $\{1, 2, 3\}$.

Define the weight $w$ of an element $A$ to be $w(A) = |A|$. How many elements in $S$ have weight $k$?

$\Phi_S(x) = 1 + 3x + 3x^2 + x^3$. The coeffient of $x^k$ in the generating series is the answer.

**Generating Series**: Given set $S$ where $\rho \in S$ is given a non-negative integer weight $w(\rho)$, the **generating series** of $S$ with respect to $w$ is $\Phi_S(x) = \sum_{\rho \in S} x^{w(\rho)}$. If $a_x$ is the number of elements in $S$ of weight $k$, then $\Phi_S(x) = \sum_{k \ge 0}a_k x^k$. The *coefficients* store the answers to our counting problems.

Notation: $[x^k]\Phi_S(x)$ denotes the coefficient of $x^k$ in $\Phi_S(x)$.

Example: How many ways can we throw 2 dice to get a sum of $k$?

> Define $S = \{1, 2, 3, 4, 5, 6\} = \{(a, b) \mid a, b \in \{1, 2, 3, 4, 5, 6\}\}$. Define $w(a, b) = a + b$. So $\Phi_S(x) = (x + x^2 + x^3 + x^4 + x^5 + x^6)^2$.

## Format Power Series

> A formal power series has the form $A(x) = \sum_{i \ge 0}a_i x_i$, where each $a_i$ is a well-defined, finite number. The coefficient of $x_i \in A(x) = a_i$, denoted by $[x_i]A(x)$.

**Equality**: Let $A(x) = \sum_{n \ge 0}a_n x^n$, $B(x) = \sum_{n \ge 0}b_n x^n$. $A(x) = B(x) \Leftrightarrow a_n = b_n \forall n \ge 0$.

### Operations
**Addition**:
 $A(x) + B(x) = \sum_{n \ge 0} (a_n + b_n) x^n$. Since $a_n + b_n$ is a well-defined finite number, $A(x) + B(x)$ is also a formal power series (*closed under addition*).

**Multiplication**:
$$\begin{aligned}
A(x)B(x) &= (\sum_{i \ge 0}a_i x^i)(\sum_{j \ge 0}b_i x^i) \\ 
&= \sum_{i \ge 0}\sum_{j \ge 0} a_i b_j x^{i + j} \\ 
&= \sum_{n \ge 0}(\sum_{i = 0}^n a_i b_{n - i})x^n
\end{aligned}$$

If we multiply $A(x)$ by $x^k$, what is $[x^n]x^kA(x)$?
$$[x^n]x^kA(x) = \begin{cases}
[x^{n - k}]A(x), &n \ge k \\
0, &n < k
\end{cases}$$

Example: $A(x) = (1 + 3x)^2$, $B(x) = \sum_{i \ge 0}2^i x^i$.

> $$\begin{aligned}[x^n]A(x)B(x) &= [x^n](1 + 6x + 9x^2)B(x)\\ &= [x^n]B(x) + [x^n]6xB(x) + [x^n]9x^2B(x) \\ &= 25n^{n - 2}\end{aligned}$$
> This is only valid for $n \ge 2$, so we can manually calculate for $n \le 1$.     
> So $A(x)B(x) = 1 + 8x + \sum_{n \ge 2} 25n^{n - 2}x^n$.

**Inverse**: The inverse of $A(x)$ is another series $B(x)$ such that $A(x)B(x) = 1$.

Example: Find the inverse for $1 - x$. Suppose $\frac{1}{1 - x} = \sum_{n \ge 0} a_n x^n$.
$$\begin{aligned}
\frac{1}{1 - x}(1 - x) &= (\sum_{n \ge 0} a_n x_n)(1 - x) \\
1 &= a_0 + a_1x + a_2x^2 + ... - a_0x - a_1x^2 - a_2x^3 - ... \\
&= a_0 + \sum_{n \ge 1}(a_n - a_{n - 1}) x^n
\end{aligned}$$
Comparing coefficients, $a_0 = 1$, $a_i = a_{i + 1}$ for $i \ge 0$. So $\frac{1}{1 - x} = \sum_{n \ge 0}x^n$.

> Some power series have **no inverses** ...

Example: $\frac{1}{x}$. Suppose $\frac{1}{x} = \sum_{n \ge 0} a_n x_n$. Then $1 = \sum_{n \ge 0}a_n x^{n + 1}$. There is no constant on the right hand side so there is a contradiction. Therefore $\frac{1}{x}$ does not have an inverse.

**Theorem**: $A(x)$ has an inverse if and only if $[x^0]A(x) \not= 0$.

Example: Let $A(x) = \frac{1 - x}{1 - 2x - 3x^2}$. Suppose $A(x) = \sum_{n \ge 0}a_n x^n$.

> $$\begin{aligned} A(x) &= \frac{1 - x}{1 - 2x - 3x^2} \\ 1 - x &= A(x)(1 - 2x - 3x^2) \\ &= a_0 + (a_1 - 2a_0)x + \sum_{n \ge 2}(a_n - 2a_{n - 1} - 3a_{n - 2})x^n \end{aligned}$$
> **Comparing coefficients**.   
> $1 = a_0$,    
> $-1 = a_1 - 2a_0 \Rightarrow a_1 = 1$,    
> $a_n = 2a_{n - 1} + 3a_{n - 2}$.  
>
> We can determine the coefficients of subsequent terms through the *recurrence*.

### Common Series

1. $\frac{1}{1 - x} = \sum_{n \ge 0} x^n$.
2. $\frac{1 - x^{k + 1}}{1 - x} = 1 + x + x^2 + ... + x^k$.
3. $(\frac{1}{1 - x})^k = \sum_{n \ge 0} {n + k - 1 \choose k - 1}x^n$ (*negative binomial theorem*).
    - Proof: Induction on $k$.

    > **Base Case**: $k = 1$, ${n - 1 \choose 0} = 1$, $\sum_{n \ge 0}x^n$ is the geometric series. 
    > **Induction Step**: Consider $k$.
    > $$\begin{aligned} (\frac{1}{1 - x})^k &= (\frac{1}{1 - x})(\frac{1}{1 - x})^{k - 1} \\ &= (1 + x + x^2 + ...)(\sum_{n \ge 0}{n - k + 2 \choose k - 2}x^n) \\ &= \sum_{n \ge 0}({n + k - 2 \choose k - 2} + {n + k - 3 \choose k - 2} + ... + {k - 2 \choose k - 2})x^n \\ &= \sum_{n \ge 0} {n + k - 1 \choose k - 1}x^n \end{aligned}$$

### Composition of Formal Power Series

> Is $A(B(x))$ a formal power series?

Example: $G(x) = \frac{1}{1 - x}$, $A(x) = \frac{x^2}{1 - x}$.

> $$\begin{aligned} G(A(x)) &= 1 + (\frac{x^2}{1 - x}) + (\frac{x^2}{1 - x})^2 + ... \\ &= \frac{1}{1 - \frac{x^2}{1 - x}} \\ &= \frac{1 - x}{1 - x - x^2} \end{aligned}$$

Example: $G(1 + x^2)$.

> $G(1 + x^2) = 1 + (1 + x^2) + (1 + x^2)^2 + ...$.     
> Looking at the constant term, there it is not a well-defined, finite number, so $G(1 + x^2)$ is **not** a formal power series.

**Theorem**: If $A(x)$ and $B(x)$ are formal power series, where $[x^0]B(x) = 0$, then $A(B(x))$ is a formal power series.

- Intuition is that we need a finite bound for the terms where $[x^n]A(B(x))$ can be found.

## Sum and Product Lemmas

### Sum Lemma

Let $S = A \cup B$, $A \cap B = \emptyset$. Let $w$ be the weight function on $S$. Then $\Phi_S(x) = \Phi_A(x) + \Phi_B(x)$.

> $\Phi_S(x) = \sum_{\rho \in S}x^{w(\rho)} = \sum_{\rho \in A} x^{w(\rho)} + \sum_{\rho \in B} x^{w(\rho)} = \Phi_A(x) + \Phi_B(x)$.

### Product Lemma

Let $A$, $B$ be sets with weight functions $\alpha, \beta$. Consider $A \times B$ with the weight function $w(a, b) = \alpha(a) + \beta(b)$, for all $(a, b) \in A \times B$. Then $\Phi_{A \times B}(x) = \Phi_A(x)\Phi_B(x)$.

> $$\begin{aligned} \Phi_A(x)\Phi_B(x) &= (\sum_{a \in A}x^{\alpha(a)})(\sum_{b \in B}x^{\beta(b)}) \\ &= \sum_{a \in A}\sum_{b \in B}x^{w(a, b)} \\ &= \sum_{(a, b) \in A \times B}x^{w(a, b)} \\ &= \Phi_{A \times B}(x) \end{aligned}$$

Example: How many ways can a sequence of $k$ non-negative integers sum up to $n$?

> Define $S = \mathbb{N}_0^k$ (all sequences of $k$ non-negative integers). Define $w(a_1, ..., a_k) = \sum_{i = 1}^k a_i$. Define $\alpha(a) = a$ for each copy of $\mathbb{N}_0$. Then the produce lemma applies.
> $$\begin{aligned}\Phi_S(x) &= (\Phi_{\mathbb{N}_0}(x))^k \\ &= \frac{1}{(1 - x)^k}\end{aligned}$$
> Answer is $[x^n]\frac{1}{(1 - x)^k} = {n + k - 1 \choose k - 1}$.

## Integer Composition Problems

> A $k$-tuple $(a_1, ..., a_k)$ of positive integers is a composition of $n$ if $a_1 + ... + a_k = n$. Each $a_i$ is a part, and the composition has $k$ parts.

Example: Compositions of $n$ with $2k$ parts. The first $k$ are at least $5$, the last $k$ are multiples of $3$.

> Define $S = A^k \times B^k$ where $A = \{5, ... \}$, $B = \{3, 6, 9, ...\}$. $w(a_1, ..., a_k, b_1, ..., b_k) = a_1 + ... + a_k + b_1 + ... + b_k$. Use $\alpha(a) = a$ and $\beta(b) = b$. $\Phi_A(x) = \frac{x^5}{1 - x}$, $\Phi_B(x) = \frac{x^3}{1 - x^3}$. By Product lemma, $\Phi_S(x) = (\Phi_A(x))^k(\Phi_B(x))^k \frac{x^{8k}}{(1-x)^k(1-x^3)^k}$.
>
> The answer is $[x^{n-8k}](\frac{1}{1 - x})^k(\frac{1}{1 - x^3})^k$. We can reindex into $\sum_{j = 0}^{\lfloor\frac{n - 8}{3}\rfloor}{k + n - 8k - 3j - 1 \choose k -1}{k + j - 1\choose k - 1}$

Example: How many compositions of $n$ are there?

> Define $S = \mathbb{N}^0 \cup \mathbb{N} ... \ \cup_{k \ge 0}\mathbb{N}^k$. Define $w$ of a composition to be the sum of the parts. By sum lemma, $\Phi_S(x) = \sum_{k \ge 0}(\Phi_{\mathbb{N}}(x))^k$. By product lemma, geometric series, and constant term is 0, $\sum_{k \ge 0}(\frac{x}{1-x})^k = \frac{1}{1 - \frac{x}{1-x}} = \frac{1-x}{1-2x}$.
>
> The answer is $[x^n]\frac{1-x}{1-2x} = \begin{cases} 2^{n-1}, &n > 0 \\ 1, &n = 0\end{cases}$

Example: How many compositions of $n$ where each part is odd?

> Let $\mathbb{N}_{odd} = \{1, 3, ...\}$. Define $S = \cup_{k \ge 0}\mathbb{N}_{odd}^k$. We use the usual weight function.
> $$\begin{aligned}\Phi_S(x) &= \sum_{k \ge 0}(\Phi_{\mathbb{N}_{odd}}(x))^k \\ &= \sum_{k \ge 0}(\frac{x}{1-x^2})^k \\ &= \frac{1}{1-\frac{x}{1-x^2}} \\ &= \frac{1-x^2}{1-x-x^2}\end{aligned}$$
> Answer is $[x^n]\frac{1-x^2}{1-x-x^2}$. Let $A(x) = \frac{1-x^2}{1-x-x^2}$, $A(x) - xA(x) - x^2A(x) = 1 - x^2$. By comparing coefficients, we have $a_0 = 0, a_1 = 1, a_2 = 1, a_n = a_{n-1} + a_{n-2}$.

We also have a combinatorial proof.

> Let $S_n$ be the set of all compositions of $n$ where every part is odd. We want a bijection $f: S_n \to S_{n - 1} \cup S_{n-2}$. Define $f(a_1, ... a_k) = \begin{cases}(a_1, ..., a_{k-1}), &a_k = 1 \\ (a_1, ..., a_k - 2), &a_k > 1\end{cases}$. We see that every part in the output is still valid (-2 does not change parity), so it is either in $S_{n - 1}$ or $S_{n-2}$. The inverse is $f^{-1}: S_{n-1} \cup S_{n-2} \to S_n$ where $f^{-1}(b_1, ..., b_l) = \begin{cases}(b_1, ..., b_l, 1), &\sum_{b_i} = n - 1 \\ (b_1, ..., b_l +2), &\sum_{b_i} = n - 2\end{cases}$.
>
> So $f$ is a bijection and $|S_n| = |S_{n-1}| + |S_{n-2}|$

# Binary Strings

- Denote empty string $\epsilon$.
- A block is a maximal non-empty substring of all 0's or all 1's.

The general question given is how many binary strings of length $n$ have certain properties.

1. Find an expression for the set of all binary strings with these properties.
2. Define the weight of a string to be its length.
3. Find the generating series of $S$ with respect to $w$.
4. Answer is $[x^n]\Phi_S(x)$.

## Operations on Sets of Stringso

1. Concatenation of two strings $A, B$. $AB = \{ab | a \in A, b \in B\}$.
2. Star. $A^* = \cup_{k \ge 0} A^k$, $A^0 = \{\epsilon\}$, $\{0, 1\}^*$ is the set of all binary strings.

We want to be able to apply product and sum lemma to string operations, but we need to ensure that they are not ambiguous.

### Ambiguity

> Strings that can be generating in multiple ways.

$AB$ is ambiguous if $\exists$ $s \in AB, s = a_1 b_1 = a_2 b_2$ for distinct $a_1, a_2 \in A$, $b_1, b_2 \in B$. $A \cup B$ is ambiguous if $A \cap B \neq \emptyset$.

**Theorem**: Let $A, B$ be sets of strings.

1. If $A \cup B$ is unambiguous, then $\Phi_{A \cup B}(x) = \Phi_A(x) + \Phi_B(x)$.
2. If $AB$ is unambiguous, then $\Phi_{AB}(x) = \Phi_A(x)\Phi_B(x)$.
3. If $A^*$ is unambiguous, then $\Phi_{A^*}(x) = \frac{1}{1 = \Phi_A(x)}$.

    > By 1 and 2, the sum and product lemma apply. $\Phi_{A^*}(x) = \sum_{k \ge 0}(\Phi_A(x))^k$ by geometric series and $[x^0]\Phi_A(x) = 0$ ($\epsilon$ would make $A^*$ ambiguous).

### Unambiguous Expressions for Strings

1. $\{0, 1\}^*$.
2. $\{0\}^*(\{1\}\{0\}^*)^*$, or flip all the bits.
3. **Block decomposition**: $\{0\}^*(\{1\}\{1\}^*\{0\}\{0\}^*)^*\{1\}^*$, or flip all the bits.

For string generation problems, start with one of the three unambiguous expressions and then remove parts that violate our conditions.

Example: The set of all strings with no three consecutive 0's.

> Start with $\{0\}^*(\{1\}\{0\}^*)^*$, we can find 000 in both instances of $\{0\}^*$. Remove these instances $\{0\}^* \to \{\epsilon, 0, 00\}$. We are left with $\{\epsilon, 0, 00\}(\{1\}\{\epsilon, 0, 00\})^*$.

Example: Set of all strings where an even block of 0's cannot be followed by an odd block of 1's.

> We start with block decomposition and break into cases with even and odd block of 0's. In the odd case, we can leave the 1's alone but in the even case, we need to ensure an even block of 1's. We are left with $\{1\}^*(\{00\}\{00\}^*\{11\}\{11\}^* \cup \{0\}\{00\}^*\{1\}\{1\}^*)^* \{0\}^*$.

## String Recursion
Let $S$ be the set of all strings, we can recursively define $S$ as $S = \{0, 1\}S \cup \{\epsilon\}$. We get a generating series expression $\Phi_S(x) = 2x\Phi_S(x) + 1$, $\Phi_S(x) = \frac{1}{1 - 2x}$.

Example: Sets that do not have 1010 as a substring

> Let $T$ be a string with one copy of 1010, which is at the right end of the string.   
> 
> We have two equations.
>
> 1. $\{\epsilon\} \cup S\{0, 1\} = S \cup T$.
>       - ($\subseteq$): $\epsilon \in S$. Let $\sigma \in S$. Then $\sigma\{0, 1\}$ has no 1010 unless $\sigma$ ends with 101 and we attach a 0 at the end. If so, this would be the only copy of 1010 in $\sigma 0$ as no 1010 can be found in $\sigma$. So $\sigma 0$ and $\sigma 1$ are in $S \cup T$.
>       - ($\supseteq$): A string in $S$ is either empty, or we can take off the rightmost bit and obtain another string in $S$. $S \subseteq \{\epsilon\} \cup S\{0, 1\}$. For a string in $T$, removing the rightmost bit destroys the only copy of 1010 in the string. So $T \subseteq S\{0\}$. So $S \cup T \subseteq \{\epsilon\} \cup S\{0, 1\}$.
>
> 2. $S\{1010\} = T \cup T\{10\}$.
>       - ($\subseteq$): Let $\sigma \in S$. Then $\sigma 1010$ has at least 1 copy of 1010 at the right end. If that is the only copy then $\sigma \{1010\} \in T$. A second copy can exist if $\sigma$ envds with 10, so $\sigma 1010$ ends with 101010. Then this is in $T\{10\}$.
>       - ($\supseteq$): Any string in $T$ ends with 1010. Removing this destroys all copies of 1010 in the string, so it is in $S\{1010\}$.
>
> We can solve for $\Phi_S(x)$ using the two equations, and obtain $\Phi_S(x) = \frac{1+x^2}{1-2x+x^2-2x^3+x^4}$.

# Coefficients in Rational Expressions

> Finding $[x^n]\frac{f(x)}{g(x)}$.

Example: $A(x) = \sum_{n \ge 0}a_n x^n$ where $A(x) = \frac{3-8x-2x^2}{1-7x+16x^2-12x^3}$.

> We can use partial fraction decomposition to see that $A(x) = \frac{-1}{1-2x} + \frac{3}{(1-2x)^2} + \frac{1}{1-3x}$. This allows us to solve for $[x^n]A(x)$.
> $$\begin{aligned}[x^n]A(x) &= [x^n] \frac{-1}{1-2x} + [x^n]\frac{3}{(1-2x)^2} + [x^n]\frac{1}{1-3x} \\ &= -1(2^n) + 3{n + 1 \choose 1}2^n + 3^n \\ &= -(2^n) + 3(n+1)2^n + 3^n\end{aligned}$$

Let us generalize this approach.

Suppose $A(x) = \frac{f(x)}{g(x)}$. If $deg(f(x)) \ge deg(g(x))$, we can use polynomial long division to get $A(x) = q(x) + \frac{r(x)}{g(x)}$ where $deg(r(x)) < deg(g(x))$.

Assume constant term of $g(x) = 1$ (if 0, then we cannot divide). Then we can factor $g(x) = (1-r_1 x)^{e_1}(1 - r_2 x)^{e_2} ...(1-r_k x)^{e_k}$ by the fundamental theorem of algebra. Using partial fraction decomposition, we can obtain $A(x) = \frac{p_1(x)}{(1-r_1 x)^{e_1}} + ... + \frac{p_k(x)}{(1-r_k x)^{e_k}}$, where $deg(p_i(x)) < e_i$.

Each $\frac{p_i(x)}{(1-r_i)^{e_i}} = \frac{c_1}{1-r_1 x} + ... + \frac{c_{e_i}}{(1-r_i x)^{e_i}}$, $c_j$ constant.

$$\begin{aligned}[x^n]\frac{p_i(x)}{(1-r_i)^{e_i}} &= [x^n]\frac{c_1}{1-r_1 x} + ... + [x^n]\frac{c_{e_i}}{(1-r_i x)^{e_i}} \\ &= \sum_{j = 1}^{e_i} [x^n]\frac{c_j}{(1-r_i x)^j} \\ &= \sum_{j=1}^{e_i} c_j{n + j - 1 \choose j - 1}r_i^n \\ &= \sum_{j = 1}^{e_i} c_j \frac{(n + j - 1)!}{(j - 1)!(n)!}r_i^n \\  &= \sum_{j = 1}^{e_i} Q(n)r_i^n\end{aligned}$$
Where $Q(n)$ is a polynomial of $n$ of degree at most $j - 1$.

So $[x^n]\frac{p_i(x)}{(1-r_i x)^{e_i}} = Q_i(n)r_i^n$, where $Q_i(n)$ is a polynomial in $n$ of degree at most $e_i - 1$. So $[x^n]A(x) = Q_1(n)r_1^n + ... + Q_k(n)r_k^n$, where $Q_i(n)$ has degree at most $e_i - 1$.

**Characteristic Polynomial**: If $g(x) = (1-r_1x)^e_i ... (1-r_kx)^{e_k}$, then its characteristic polynomial is $g^*(x) = (x-r_1)^{e_i} ... (x-r_x)^{e_k}$. Then $r_1, ..., r_k$ are the roots of the characteristic polynomial with multiplicities $e_1, ..., e_k$.

Example: $\{a_n\}$ satisties $a_0 = 1, a_5 = 5$ and $a_n - 5a_{n - 1} + 6a_{n-2} = 0$ for $n \ge 2$.

> First find $A(x) = \sum_{n \ge 0}x^n$ as a rational expression.   
> For each $n \ge 2$ multiply its recurrence by $x^n$.
> $$\begin{aligned}a_2x^2 - 5a_1x^2 + 6a_0x^2 &= 0 \\ a_3x^3 - 5a_2x^3 + 6a1x^3 &= 0 \\ ... \\ a_nx^n - 5a_{n-1}x^n + 6a_{n-2}x^n &= 0\end{aligned}$$
> Add all of the equations together.
> $$\begin{aligned}\sum_{n \ge 2}a_nx^n - 5\sum_{n \ge 1}a_nx^{n+1} + 6\sum_{n \ge 0}a_nx^{n+2} &= 0 \\ \sum_{n \ge 2}a_nx^n - 5x\sum_{n \ge 1}a_nx^n + 6x^2\sum_{n \ge 0}a_nx^n &= 0 \\ (A(x) - a_0 - a_1x) - 5x(A(x) - a_0) + 6x^2A(x) &= 0\end{aligned}$$
> We have $A(x)(1 - 5x + 6x^2) - 1 - 5x + 5x = 0$ and $A(x) = \frac{1}{1 - 5x + 6x^2}$. The characteristic polynomial is $x^2 - 5x + 6 = (x-2)(x-3)$. The roots are $x=2,3$ with multiplicity 1 each.
>
> The answer is $[x^n]A(x) = a_n = A\cdot 2^n + B \cdot 3^n$ for constants $A, B$.  
> For $a_0$: $1 = A + B$.   
> For $a_1$: $5 = 2A + 3B$.     
> We have $A = -2$, $B = 3$, so $a_n = (-2)2^n + (3)3^n$.

We see that there is a shortcut from the recurrence to the characteristic polynomial. If $\{a_n\}$ satisfies the recurrence $a_n + c_1a_{n - 1} + ... + c_ka_{n - k} = 0$, then its corresponding characteristic polynomial is $x^k + c_1x^{k-1} + ... + c_k$. $A(x) = \sum a_nx^n$ has the form $A(x) = \frac{...}{1 + c_1x + ... + c_kx^k}$.

Example: $\{a_n\}$ satisties $a_0 = 1, a_1, = 2, a_2 = 1$ where $a_n - 3a_{n-1} + 3a_{n-2} - a_{n-3} = 0$ for $n \ge 3$.

> The characteristic polynomial is $x^3 - 3x^2 + 3x - 1 = (x-1)^3$. The root is $x=1$ with multiplicity 3. We have $a_n = An^2 + Bn + C$ for some constants $A, B, C$.  
> For $a_0$: $1 = C$.    
> For $a_1$: $2 = A + B + C$.     
> For $a_2$: $1 = 4A + 2B + C$.      
> We have $A = -1, B = 2, C = 1$, so $a_n = (-1)n^2 + 2n + 1$.

Example: $a_0 = 7, a_1 = 10, a_2 = 13, a_n - 7a_{n-1} + 15a_{n-2}-9a_{n-3}=0$ for $n \ge 3$.

> The characteristic polynomial is $x^3 - 7x^2 + 15x - 9 = (x-3)^2(x-1)$. The roots are $x=3,1$ with multiplicities $2$ and $1$ respectively. We have $a_n = (An + B)3^n + C$ for constants $A, B, C$.  
> For $a_0$: $7 = B + C$.   
> For $a_1$: $10 = 3A + 3B + C$.    
> For $a_1$: $13 = 18A + 9B + C$.   
> We have $A = -1, B = 3, C = 4$, so $a_n = (-n + 3)3^n + 4$.

Example:  $f_0 = 0, f_1 = 1, f_n - f_{n - 1} - f_{n - 2} = 0$, $n \ge 2$.

> Characteristic polynomial is $x^2 - x - 1$. The roots are $x = \frac{1 \pm \sqrt 5}{2}$, so $f_n = A(\frac{1+\sqrt 5}{2})^n + B(\frac{1-\sqrt 5}{2})^n$ for constants $A, B$.     
> For $f_0$: $0 = A + B$.   
> For $f_1$: $1 = (\frac{1+\sqrt 5}{2})A + (\frac{1 - \sqrt 5}{2})B$.   
> We have $A = \frac{1}{\sqrt 5}$, $B = \frac{-1}{\sqrt 5}$, so $f_n = \frac{(\frac{1 + \sqrt 5}{2})^n - (\frac{1-\sqrt 5}{2})^n}{\sqrt 5}$. We can show that $f_n \in \mathbb{Z}$.

# Graph Theory

A graph $G$ is a pair $(V(G), E(G))$ where $V(G)$ is a set of objects called vertices, and $E(G)$ is a set of unordered pairs of $V(G)$ called edges. We might say $G = (V, E)$.

**Terminology**:

1. Two vertices $u, v$ are adjacent if $\{u, v\}$ is an edge. They are also said to be neighbours.
2. The set of all neighbours of $v$ in $G$ is its neighbourhood, denoted $N_G(v)$.
3. Edge $e = \{u, v\}$ is **incident** with its end points $u, v$. We can also say that $e$ **joins** $u$ and $v$.

**Notes**:

1. $e=uv$ appreviates $ = \{u, v\}$.
2. $uv = vu$, edges are unordered.
3. For most of this course, our graphs are "simple". There are no loops or multiple edges.
4. Graphs are considered to be finite.

## Degrees

Degree of vertex $v$ in $G$ is the number of edges in $G$ that are incident with $v$, denoted $deg_G(v)$ or $deg(v)$.

$\sum_{v \in V(G)} deg(v)$ is always even.

> **Handshaking Lemma**: For any graph $G$, $\sum_{v \in V(G)}deg(v) = 2|E(G)|$.
>
> Each $e = uv \in E(G)$ contributes 2 to the sum, one for $dev(u)$ and one for $deg(v)$.

**Corollary**: For any graph $G$, the number of odd degree vertices is even.

> $O, E \in V(G)$ with odd, even vertices respectively. Then $\sum_{v \in V(G)}deg(V) = \sum_{v \in O}deg(v) + \sum_{v \in E}deg(v)$. By handshaking lemma, $\sum_{v \in V(G)}deg(v)$ is even. $\sum_{v \in E}deg(v)$ is even because it is a sum of even numbers. Therefore, $\sum_{v \in O}deg(v)$ is even. A sum of odd integers is even, so there are an even number of them.

## Isomorphism

**Definition**: Two graphs $G_1$, $G_2$ are **isomorphic** if there exists a bijection $f: V(G_1) \to V(G_2)$ such that $uv \in E(G_1)$ if and only if $f(u)f(v) \in E(G_2)$ (edge adjacency is preserved). Such a function is an **isomorphism**.

Assume $|E(G_1)| \neq |E(G_2)|$, then there cannot possibly be a bijection between $V(G_1)$ and $V(G_2)$. Similarily, we can look at the degree of certain vertices.

To prove that two graphs are isomorphic, find an isomorphism. To prove that two graphs are not isomorphic, find an adjacency structure that exists in one but not the other.

## Classes of Graphs

1. **Complete graph**: a graph where every pair of vertices is an edge. A complete graph on $n$ vertices is $K_n$. There are $n \choose 2$ edges in $K_n$.
2. **K-Regular**: a graph where every vertex has degree $k$. In a $k$-regular graph of $n$ vertices, there are $\frac{nk}{2}$ edges.

    > By handshaking lemma, $2|E(G)| = \sum_{v \in V(G)}deg(v) = \sum_{v \in V(G)}k = nk$.
    
4. G is **bipartite** if there exists a parition $(A, B)$ of $V(G)$ such that every edge in $G$ joins one vertex in $A$ with one vertex in $B$.