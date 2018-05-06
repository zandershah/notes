MATH239
=

# Enumeration

## Sets we count
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