CS 350 Help Session
=

> Question and answer format.

1. Page 77, Question 5.
    - Did not cover in class.
2. A2, Question 1. Difference between standard form and dynamics function.
    - Same thing.
3. Page 40, Question 1a.
    - Set up $p(x) = a + bx + cx^2 + dx^3$ and the four givens.
    - $$\begin{bmatrix}
    1 & x_0 & x_0^2 & x_0^3 \\
    1 & x_2 & x_2^2 & x_2^3 \\
    0 & 1 & 2x_1 & 3x_1^2 \\
    0 & 0 & 2 & 6x_1 \\
    \end{bmatrix}$$
    - For 1b, set rows to 1 and others to 0.
4. Local Truncation Error. A2.
    - Everything on the right-hand side is exactly correct.
    - Taylor's and then simplify.
    - $$\begin{aligned}
    y_{n+1} &= 4y_n - 3y_{n-1} - 2hf(t_{n-1}, y_{n-1}) \\
    &= 4y(t_n) - 3y(t_{n-1}) - 2hy^\prime(t_{n-1}) \\
    &= y(t_n) + y^\prime(t_n)h + y^{\prime\prime}(t_n)\frac{h^2}{2} - y^{\prime\prime\prime}(t_n)\frac{h^3}{2} + ...
    \end{aligned}$$
    - So $y_{n+1} - y(t_{n+1}) = O(h^3)$.
    - If the question asked for the global error of this method, do local truncation and remember global is one less. But that would be a dirty question.

> Note: Exams do not try to fool anybody.
    
5. Fair game for midterm.
    - Anything from the course notes that was taught, up to and including last friday.

6. Page 23, Question 1a.
    - $F(2, 5, -1, 10)$.
    - Largest number looks like $0.11111 \cdot 2^{10}$ in binary, $992$ in decimal. Brute force factorials to find $6!$ is the largest.
    - Turns out $720$ requires 6 bits. So it is not in our floating point number system. This was an oversight, $5!$ or $6!$ would be accepted on an examination.
7. Page 23, Question 2a.
    - Could we be asked to plot elements on the real axis in an exam.
    - Sure. Kind of a pain.
    - OFL, UFL are overflow, underflow.
    - More than one formula in the notes for calculating epsilon.
        - Just remember $fl(x) = x(1 + \delta)$, $|\delta| < \epsilon$. $\beta^{1-t}$.
8. Calculators?
    - Wont need them.
9. Page 24, Question 5c.
    - Exactly the assignment question. Errors follow the same recursion.
10. Page 23, Question 3.
    - We are adding $1 + \frac{1}{2} + \frac{1}{3} + ... + \frac{1}{M}$.
    - For large $M$, when we go from back-to-front, it does not give the same value as front-to-back.
    - Remember that $(a + b) + c \neq a + (b + c)$.
    - It should happen that going from back-to-front is better, since we add small to large. We can only keep a fixed number of digits. We are not losing anything.
    - *Follow up*: catastrophic cancellation? No, because $n, M$ are both integers.
11. Page 18, Exercise.
    - $0.111, 0.011, 0.001$.
12. From first or second lecture, doing the integral backwards was better.
    - $e_n = \alpha e_{n-1} = \alpha^n e_0$. If $\alpha > 1$, then lets do $e_{n-1} = \frac{1}{\alpha}e_n$.
    - Issue because we dont have $I_{n}$ in the first place.
13. Page 40, Question 4.
    - Seems like $S(0) = 0$, but we have to compute the spline.
14. Not-a-knot boundary conditions.
    - Use third derivatives.
15. Page 41, Question 9.
    - We have three cubic polynomials. Not-a-knot says that $S_1(x) = S_2(x) = S_3(x)$. So it is just $P(x) = 2x^3 + 5x - 7$.
16. Matlab.
    - No Matlab questions, but pseudocode is fair.
17. Notes.
    - Must be your own. Can have printed notes from iPad, but you must show professor before.
18. Page 40, Question 5.
    - $S^\prime(x_1) = -S^{\prime\prime}(x_n)$, $S^{\prime\prime}(x_1) = -S^{\prime}(x_n)$.
    - $S_1(x) = a_1 + b_1(x - x_1) + c_1(x-x_1)^2 + d(x-x_1)^3$. Similar for $S_{n-1}(x)$.
    - The coefficient depend on the last two points, and the last two derivatives.
        i. $$S_1^\prime(x_1) = b_1 = s_1 = -S^{\prime\prime}_{n-1}(x_n) = -2c_{n-1} - 6d_{n-1}(x_n - x_{n-1})$$
        ii. $$\begin{aligned}S^{\prime\prime}(x_1) &= 2c_1 \\ &= -S^\prime(x_n) \\ &= -(b_{n-1} + 2c_{n-1}(x_n - x_{n-1}) + 3d_{n-1}(x_n - x_{n-1})^2)\end{aligned}$$
19. Page 41, Question 7.
    - A little bit of a pain.
    - Plug in $x_i, x_{i+1}$ in order to solve for some terms.
    - $S_i(x_i) = y_i = a_i \Delta x_i$. $S_i(x_{i+1}) = y_{i+1} = c_i \Delta x_i$.
    - To get $b_i$, we take derivatives.
