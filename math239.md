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
    > **Induction Step**: Consider $k$.;
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