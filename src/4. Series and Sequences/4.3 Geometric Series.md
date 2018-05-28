# Geometric Sequences and Series

A **geometric sequence** is a sequence of numbers defined by a starting term $$a$$ and a common ratio $$r$$. In the sequence, the ratio of consecutive terms (i.e. $$\frac{t_n}{t_{n-1}}$$) is constant, and is equal to $$r$$.

$$
2, 6, 18, 54, 108, ...
$$

is a geometric sequence with first term $$a = 2$$ and common ratio $$r = 3$$. 

Notice that the second term is the first term multiplied by the common ratio once, and the third term is the first term multiplied by the common ratio twice. Then, in general:

$$
t_k = ar^{k-1}
$$

represents the $$k$$th term in the series, assuming that we start counting at 1. 

<br>

## Sum of a Geometric Sequence

The derivation of the sum of a geometric series is similar to that of the arithmetic series. Suppose we want to find the sum $$S_n$$ of the first $$n$$ terms of a geometric series with first term $$a$$ and common ratio $$r$$. Then:

$$
\begin{align}
S_n = a + ar &+ ar^2 + ... + ar^{n-3} + ar^{n-2} + ar^{n-1} \\
rS_n = ar &+ ar^2  + ... + ar^{n-3} + ar^{n-2} + ar^{n-1} + ar^{n} \\
\end{align}
$$ 

Notice, if we subtract the second line from the first, the terms $$ar, ar^2, ar^3, ... ar^{n-2}, ar^{n-1}$$ are all cancelled out. 

$$
\implies (1-r)S_n = a - ar^n = a(1 - r^n) \\
\implies S_n = \frac{a(1 - r^n)}{1-r}
$$

This formula is also equal to 

$$
S_n = \frac{a(r^n - 1)}{r - 1}
$$

which comes from multiplying both the numerator and denominator of the first form by -1. 

<br>

### Sum of an Infinite Geometric Series

So far, we made no assumptions about $$a, r$$ or $$n$$. Now, let's look at two different cases of $$r$$:

- $$| r | > 1$$: The magnitude of $$t_{k+1}$$ is greater than the magnitude of $$t_k$$
- $$| r| < 1$$: The magnitude of $$t_{k+1}$$ is less than the magnitude of $$t_k$$

The reason we look at the magnitude of $$t_k$$ is because if $$r$$ is negative, terms oscillate between positive and negative. 

In the case where $$| r | < 1$$, we know that $$r^n \rightarrow 0$$ as $$n \rightarrow \infty$$. Then, consider $$S_n$$ as $$n \rightarrow \infty$$:

$$
\lim_{n \rightarrow \infty}S_n = \lim_{n \rightarrow \infty}\frac{a(r^n - 1)}{r - 1}
\\ = \frac{a(-1)}{r-1} = \frac{a}{1-r}
$$

This is the formula for the sum of an infinite geometric series. When $$|r| < 1$$, we say that the series **converges**, and it converges to the value above. In all other cases, we say that the series **diverges**.

Perhaps the most common example of a diverging geometric series is the case of $$a = r = \frac{1}{2}$$.

<br> 

## Problems and Applications

### Find $$a, r$$
One type of problem we can ask now is, suppose the third term of a geometric series is 12, and the fifth is 108. What are $$a$$ and $$r$$?

We know the third term must be of the form $$ar^2$$, and the fifth of the form $$ar^4$$. Then:

$$
ar^4 = 108
\\ ar^2 = 12
\\ \implies r^2 = 9
$$

Remember, $$r^2 = 9$$ has two solutions for $$r$$, and both are valid here, meaning that we either have $$r = 3$$ or $$r = -3$$. This implies that $$a = \frac{12}{r^2} = \frac{12}{9} = \frac{4}{3}$$. 

<br>

### Financial Mathematics

Geometric sequences and series have a direct application in finance – we can model payments with compounding interest as a geometric sequence, and use the properties we know of geometric series to calculate values.

1. Compounding Interest
2. Annuities
