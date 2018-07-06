<title>Series and Sequences – Appendix</title>

# Series and Sequences
---

<br>

Jump to:
- [Arithmetic Sequences](#arithmetic)
	- [Sum of an Arithmetic Sequence](#sum-arithmetic)



<br>

In this article, we will review summation notation, as well as arithmetic and geometric series and sequences. Don't be afraid to ask for help if you haven't seen some of this content before, especially the proofs. 

<br>

<a name='arithmetic'>

## Arithmetic Sequences
---

</a>

<br>

An **arithmetic sequence** is defined by a starting term $$a$$ and a common difference $$d$$. In the sequence, the difference between consecutive terms is constant (and equal to the common difference). For example:

<div align=center>

$$
3, 5, 7, 9, 11...
$$

</div>

is an arithmetic sequence with first term $$a = 3$$ and common difference $$d = 2$$. 

Notice that the second term is the first term with the common difference added once, and the third term is the first with the common difference added twice. Then:

<div align=center>

$$
t_k = a + (k-1)d
$$

</div>

represents the $$k$$th term in the series, assuming that we start counting at 1. (Recall that when we studied the binomial theorem, our general term was 0-indexed)

<br>

<a name='sum-arithmetic'>

### Sum of an Arithmetic Sequence

</a>

<br>

**Sum of First $$n$$ Natural Numbers** <br>

Before we derive the formula for an arithmetic series, i.e. the sum of an arithmetic sequence, we will look at the sum of perhaps the most naturally arithmetic series – the set of (positive) natural numbers!

Suppose we want to find the sum of the first $$n$$ natural numbers, that is:

<div align=center>

$$
S = 1 + 2 + 3 + ... + (n-2) + (n-1) + n
$$

</div>

We can rewrite $$S$$ backwards:

<div align=center>

$$
S = 1 + 2 + 3 + ... + (n-2) + (n-1) + n \\
S = n + (n-1) + (n-2) + ... + 3 + 2 + 1
$$

</div>

Notice that the first term in the top line and first term in the bottom line add to $$n+1$$, as do the second terms, third terms, and so on and so forth. It should be noted that $$n + 1$$ is precisely the sum of the first and last terms of the sequence we are trying to sum.

<div align=center>

$$
2S = (n+1) + (n+1) + (n+1) + ... + (n+1) + (n+1) + (n+1) \\
\implies 2S = n(n+1) \\
\implies S = \frac{n(n+1)}{2}
$$

</div>

You'll want to remember this formula, as it shows up in several different fields. We'll also show several other ways to prove it in Chapter 6.

<br>

### Sum of a General Arithmetic Sequence

Let's repeat the analysis above, but for an arbitrary arithmetic series. Suppose we want to find the sum of the first $$n$$ terms of a series; we'll denote this as $$S_n$$.

$$
S_n = a + (a + d) +  ... +  (a + (n-2)d) + (a + (n-1)d) \\
S_n = (a + (n-1)d) + (a + (n-2)d) +  ...  + (a + d) + a \\
$$ 

In the case of the natural numbers, when we added the two different forms of $$S$$, the corresponding sum had $$n$$ terms, each of which was $$n + 1$$. Now, $$2S_n$$ will be the sum of $$n$$ terms, each of which are equal to $$2a + (n-1)d$$, which is the sum of the first and last terms of the arithmetic sequence we're summing.

$$
2S_n = (2a + (n-1)d) + (2a + (n-1)d) + ... + (2a + (n-1)d) + (2a + (n-1)d)
\\ \implies 2S_n = (2a + (n-1)d)n
\\ \implies S_n = \frac{(2a + (n-1)d) }{2}n
$$

Therefore, the sum of the first $$n$$ terms of an arithmetic sequence with first term $$a$$ and common difference $$d$$ is $$S_n = \frac{(2a + (n-1)d) }{2}n$$. 

There is an easier way to remember this: since $$a$$ is the first term and $$a + (n-1)d$$ is the last term, $$2a + (n-1)d$$ represents the sum of the first and last numbers in the series. We can then also remember the formula as 

$$
S_n = \frac{\text{first} + \text{last}}{2} \cdot (\text{# of numbers in sum})
$$

Since there is a common difference between terms, the value $$\frac{\text{first} + \text{last}}{2}$$ represents the average value of an element in the series. The sum is the result of treating the series as if each value were replaced with the average.

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
