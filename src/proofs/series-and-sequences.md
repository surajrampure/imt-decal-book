<title>Series and Sequences – IMT DeCal</title>

# Series and Sequences
---

<br>

<!--

Jump to:
- [Arithmetic Sequences](#arithmetic)
- [Sum of an Arithmetic Sequence](#sum-arithmetic)
	- [Sum of First $$n$$ Natural Numbers](#sum-first-n)
	- [Sum of a General Arithmetic Sequence](#sum-general-arithmetic)
	- [Proofs using Induction](#arithmetic-induction)
- [Geometric Sequences](#geometric)
- [Sum of a Geometric Sequence](#sum-geometric)
	- [Infinite Geometric Series](#sum-infinite)
	- [Proof using Induction](#geometric-induction)
- [Telescoping Sums](#telescoping)

<br>

-->

In this note, we will review definitions and formulas for arithmetic and geometric series and sequences. We will also derive the sums of arithmetic and geometric series and prove these formulas using induction. Then, we will focus on deriving and proving formulas for sums of the form $$1^k + 2^k + 3^k + ... + n^k$$, using a technique known as telescoping sums.

We'll introduce these ideas as they tie in quite well with proof techniques. We will show how to prove the identities in this article in multiple ways.

If you're uncomfortable with sigma notation, please refer to the appendix note on **[Sigma and Pi Notation](../appendix/sigma-and-pi-notation.html)**.

<br>

<a name='arithmetic'>

## Arithmetic Sequences
---

</a>

An **arithmetic sequence** is defined by a starting term $$a$$ and a common difference $$d$$. In the sequence, the difference between consecutive terms is constant (and equal to the common difference). For example:

<div align=center>

$$
3, 5, 7, 9, 11...
$$

</div>

is an arithmetic sequence with first term $$a = 3$$ and common difference $$d = 2$$. Notice that the second term is the first term with the common difference added once, and the third term is the first with the common difference added twice.

In general,

<div align=center>

$$
\boxed{t_k = a + (k-1)d}
$$

</div>

represents the $$k$$th term in the series, assuming that we start counting at 1. We can also use a recursive definition:

<div align=center>

$$t_1 = a$$

$$t_k = d + t_{k - 1}, k \geq 1$$

</div>

<br>

<a name='sum-arithmetic'>

## Sum of an Arithmetic Sequence
---

</a>

<a name='sum-first-n'>

### Sum of First $$n$$ Natural Numbers
---

</a>


Before we derive the formula for an arithmetic series, i.e. the sum of an arithmetic sequence, we will look at the sum of perhaps the most naturally arithmetic series – the set of natural numbers!

Suppose we want to find the sum of the first $$n$$ natural numbers, that is:

<div align=center>

$$
S = \sum_{i = 1}^n i = 1 + 2 + 3 + ... + (n-2) + (n-1) + n
$$

</div>

We can rewrite $$S$$ backwards:

<div align=center>

$$S = 1 + 2 + 3 + ... + (n-2) + (n-1) + n$$

$$S = n + (n-1) + (n-2) + ... + 3 + 2 + 1$$

</div>

Notice that the first term in the top line and first term in the bottom line add to $$n+1$$, as do the second terms, third terms, and so on and so forth. It should be noted that $$n + 1$$ is precisely the sum of the first and last terms of the sequence we are trying to sum.

<div align=center>

$$ 2S = (n+1) + (n+1) + (n+1) + ... + (n+1) + (n+1) + (n+1) \\\ 2S = n(n+1) \\\ S = \frac{n(n+1)}{2}
$$

</div>

Therefore, $$\boxed{\sum_{i = 1}^n i = \frac{n(n+1)}{2}}$$, as we proved in the previous article.

<br>

<a name='sum-general-arithmetic'>

### Sum of a General Arithmetic Sequence
---

</a>

Let's repeat the analysis above, but for an arbitrary arithmetic series. Suppose we want to find the sum of the first $$n$$ terms of a series; we'll denote this as $$S_n$$.

<div align=center>

$$ \begin{aligned} S_n &= a + (a + d) +  ... +  (a + (n-2)d) + (a + (n-1)d) \\\ S_n &= (a + (n-1)d) + (a + (n-2)d) +  ...  + (a + d) + a \end{aligned} $$ 

</div>

In the case of the natural numbers, when we added the two different forms of $$S$$, the corresponding sum had $$n$$ terms, each of which was $$n + 1$$. Now, $$2S_n$$ will be the sum of $$n$$ terms, each of which are equal to $$2a + (n-1)d$$, which is the sum of the first and last terms of the arithmetic sequence we're summing.

<div align=center>

$$ \begin{aligned} 2S_n &= (2a + (n-1)d) + (2a + (n-1)d) + ... + (2a + (n-1)d) + (2a + (n-1)d) \\\ 2S_n &= (2a + (n-1)d)n \\\ S_n &= \frac{(2a + (n-1)d) }{2}n \end{aligned}
$$

</div>

Therefore, the sum of the first $$n$$ terms of an arithmetic sequence with first term $$a$$ and common difference $$d$$ is $$\boxed{S_n = \frac{(2a + (n-1)d) }{2}n}$$. 

There is an easier way to remember this: since $$a$$ is the first term and $$a + (n-1)d$$ is the last term, $$2a + (n-1)d$$ represents the sum of the first and last numbers in the series. We can then also remember the formula as 

<div align=center>

$$
S_n = \frac{\text{first} + \text{last}}{2} \cdot (\text{# of numbers in sum})
$$

</div>

Since there is a common difference between terms, the value $$\frac{\text{first} + \text{last}}{2}$$ represents the average value of an element in the series. The sum is the result of treating the series as if each value were replaced with the average.


<br>

We can also derive this result by using the properties of summation notation, as well as the fact that $$\sum_{i = 1}^n = \frac{n(n+1)}{2}$$ (derived above). Another way of phrasing this sum is as $$\sum_{k = 1}^n (a + (k-1)d)$$. 

<div align=center>

$$\begin{aligned} \sum_{k = 1}^n (a + (k-1)d) &= \sum_{k = 1}^n a + \sum_{k = 1}^n (k-1)d \\\ &= na + d \left( \sum_{k = 1}^n k - \sum_{k = 1}^n 1 \right) \\\ &= na + d \left( \sum_{k = 1}^n k - n \right) \\\ &= na + d \left( \frac{n(n+1)}{2} - n \right) \\\ &= \frac{n}{2} \left( 2a + (n-1)d \right)   \end{aligned}$$

</div>

This is the same result we acquired above.

<br>

<a name='arithmetic-induction'>

### Proofs, using Induction
---

</a>

Now, we will prove the above two statements, using mathematical induction. Note, the first proof was also done in the previous note.

#### Statement 1

RTP: $$\sum_{i = 1}^n i = \frac{n(n+1)}{2}$$

**Base Case**: $$n = 1$$

LHS: $$\sum_{i = 1}^1 i = 1$$, RHS: $$\frac{1(2)}{2} = 1$$

LHS = RHS, therefore the base case holds.

**Induction Hypothesis**: Assume that $$\sum_{i = 1}^k i = \frac{k(k+1)}{2}$$, for some arbitrary $$k$$.

**Induction Step**:

$$\begin{aligned} \sum_{i = 1}^{k + 1} i &= \sum_{i = 1}^k i + (k + 1) \\\ &= \frac{k(k+1)}{2} + \frac{2(k+1)}{2} \\\ &= \frac{(k+1)(k+2)}{2} \end{aligned}$$

<br>

#### Statement 2

RTP: $$\sum_{i = 1}^n (a + (i-1)d) = \frac{2a + (n-1)d}{2}n$$

**Base Case**: $$n = 1$$
LHS: $$\sum_{i = 1}^1 (a + (i-1)d) = a + 0d = a$$, RHS: $$\frac{2a + 0d}{2} = a$$
LHS = RHS, therefore the base case holds.

**Induction Hypothesis**: Assume that $$\sum_{i = 1}^k (a + (i-1)d) = \frac{2a + (k-1)d}{2}k$$, for some arbitrary $$k$$.

**Induction Step**:

$$\begin{aligned} \sum_{i = 1}^{k + 1} (a + (i-1)d) = \sum_{i = 1}^k (a + (i-1)d) + a + kd \\\ &= \frac{2a + (k-1)d}{2}k + \frac{2a + 2kd}{2}  \end{aligned}$$

<br>

<a name="geometric">

## Geometric Sequences
---

</a>

A **geometric sequence** is a sequence of numbers defined by a starting term $$a$$ and a common ratio $$r$$. In the sequence, the ratio of consecutive terms (i.e. $$\frac{t_n}{t_{n-1}}$$) is constant, and is equal to $$r$$.

<div align=center>

$$
2, 6, 18, 54, ...
$$

</div>

is a geometric sequence with first term $$a = 2$$ and common ratio $$r = 3$$. Notice that the second term is the first term multiplied by the common ratio once, and the third term is the first term multiplied by the common ratio twice.

In general, we have that

<div align=center>

$$\boxed{t_k = ar^{k-1}}$$

</div>

represents the $$k$$th term in the sequence, assuming that we start counting at 1. As with arithmetic sequences, we can also phrase a geometric sequence recursively:

<div align=center>

$$t_1 = a$$

$$t_k = rt_{k - 1}, k \geq 1$$

</div>

<br>

<a name="sum-geometric">

## Sum of a Geometric Sequence
---

</a>

The derivation of the sum of a geometric series is similar to that of the arithmetic series. Suppose we want to find the sum $$S_n$$ of the first $$n$$ terms of a geometric series with first term $$a$$ and common ratio $$r$$. Then:

<div align=center>

$$\begin{aligned} S_n &= a + ar + ar^2 + ... + ar^{n-3} + ar^{n-2} + ar^{n-1} \\\ rS_n &= ar + ar^2  + ... + ar^{n-3} + ar^{n-2} + ar^{n-1} + ar^{n} \end{aligned}$$ 

</div>

Notice, if we subtract the second line from the first, the terms $$ar, ar^2, ar^3, ... ar^{n-2}, ar^{n-1}$$ are all cancelled out. 

<div align=center>

$$\implies (1-r)S_n = a - ar^n = a(1 - r^n)$$

$$\implies \boxed{S_n = \frac{a(1 - r^n)}{1-r}}$$

</div>

This formula is also equal to $$\boxed{S_n = \frac{a(r^n - 1)}{r - 1}}$$, which comes from multiplying both the numerator and denominator of the first form by -1. 

<br>

As a side note: We can use this formula to show that $$r^n - 1$$ factors into $$(r - 1)(1 + r + r^2 + ... + r^{n-1})$$.

<div align=center>

$$\begin{aligned} a\left( \frac{r^n - 1}{r - 1} \right) &= a + ar + ar^2 + ... + ar^{n-1} \\\ \frac{r^n - 1}{r - 1} &= 1 + r + r^2 + ... + r^{n-1} \\\ \implies r^n - 1 &= (r-1)(1 + r + r^2 + ... + r^{n-1}) \end{aligned} $$

</div>

<br>

<a name="sum-infinite">

### Infinite Geometric Series
---

</a>

So far, we made no assumptions about $$a, r$$ or $$n$$. Now, let's look at two different cases of $$r$$:

- $$| r | > 1$$: The magnitude of $$t_{k+1}$$ is greater than the magnitude of $$t_k$$
- $$| r| < 1$$: The magnitude of $$t_{k+1}$$ is less than the magnitude of $$t_k$$

We're considering the absolute value of $$r$$, as now we're only concerned with the magnitude of our terms, and not the sign (if $$r$$ is negative, terms alternate between positive and negative).

In the case where $$| r | < 1$$, we know that $$r^n \rightarrow 0$$ as $$n \rightarrow \infty$$, from the basics of limits. This implies that our terms (which are of the form $$ar^{k -1}$$ also converge to 0; however, just because the terms themselves converge, it does not imply that the sum converges (as an example, recall the series defined by $$a_i = \frac{1}{i}$$: the terms themselves approach 0, however the sum has no limit!) Let's look at what happens to our formula for $$S_n$$ as we take $$n \rightarrow \infty$$:

<div align=center>
$$
\lim_{n \rightarrow \infty}S_n = \lim_{n \rightarrow \infty}\frac{a(1 - r^n)}{1 - r}
\\ = \boxed{\frac{a}{1-r}}
$$

</div>

<br>


Indeed, the sum of an infinite geometric series converges, when $$|r| < 1$$. The formula for this sum is given by $$S_\infty = \frac{a}{1-r}$$.

Perhaps the most common example of a diverging geometric series is the case of $$a = r = \frac{1}{2}$$; we can use the above formula to show that 

<div align=center>

$$\frac{1}{2} + \frac{1}{4} + \frac{1}{8} + \frac{1}{16} + ... = 1$$

</div>

<br> 

<a name="telescoping">

## Telescoping Sums
---

</a>

Consider the sum 

<div align=center>

$$\sum_{i = 1}^{99} (a_{i + 1} - a_i) = (2-1) + (3-2) + (4-3) + (5-4) + ... + (100 - 99)$$ 

</div>

We can rewrite this sum as 

<div align=center>

$$-1 + (2-2) + (3-3) + (4-4) + .... + (99-99) + 100$$

</div>

Then, all of the terms other than $$-1$$ and $100$ cancel out, giving us that the value of this sum is $$-1 + 100 = 99$$. Such a sum, where part of term $$i$$ cancels out with part of term $$i+1$$ and $$i-1$$, is known as a **telescoping sum**. The act of cancelling these terms is called the **Method of Differences**.


<br>

#### Example

Let's evaluate $$\sum_{k = 1}^{100} (\cos(k) - \cos(k-1))$$.

<div align=center>
$$\begin{aligned} \sum_{k = 1}^{100} \big(\cos(k) - \cos (k-1)\big) &= (\cos 1 - \cos 0) + (\cos 2 - \cos 1) + ... + (\cos 100 - \cos 99) \\\ &= - \cos 0 + (\cos 1 - \cos 1) + (\cos 2 - \cos 2) + ... + (\cos 99 - \cos 99) + \cos 100 \\\ &= \cos 100 - \cos 0 \end{aligned}$$
</div>

<br>

#### Example

Now, let's evaluate $$\sum_{i = 1}^n \frac{1}{i(i+1)}$$. 

First, we notice that $$\frac{1}{i(i+1)} = \frac{1}{i} - \frac{1}{i+1}$$. Then:

<div align=center>

$$\begin{aligned} \sum_{i = 1}^n \frac{1}{i(i+1)} &= \sum_{i = 1}^n \left( \frac{1}{i} - \frac{1}{i+1} \right) \\\ &= \left(\frac{1}{1} - \frac{1}{2} \right) + \left(\frac{1}{2} - \frac{1}{3} \right) + ... + \left(\frac{1}{n-1} - \frac{1}{n} \right) + \left(\frac{1}{n} - \frac{1}{n+1} \right) \\\ &= 1 + \left(-\frac{1}{2} + \frac{1}{2} \right) + \left( -\frac{1}{3} + \frac{1}{3} \right) + ... + \left( -\frac{1}{n} + \frac{1}{n} \right) - \frac{1}{n-1} \\\ &= 1 - \frac{1}{n+1} \end{aligned}$$

</div>

<br>

<a name='sum-naturals'>

## Sum of the First $$n$$ Natural Numbers
---

</a>

The question remains --- how can we use telescoping sums to give us formulas for sums of the form $$\sum_{i = 1}^n i^k$$?

The key insight lies here: Consider $(i+1)^2 = i^2 + 2i + 1$. We can rearrange this to have $(i+1)^2 - i^2 = 2i + 1$. Then, on the left hand side we have something that resembles a telescoping sum. Since both the left hand side and right hand side are equal, if I sum both sides from $i = 1$ to $i = n$, the results should be the same.

<div align=center>

$$\begin{aligned} \sum_{i = 1}^n \big( (i+1)^2 - i^2 \big) &= \sum_{i = 1}^n \big( 2i + 1\big) \\\ (2^2 - 1^2) + (3^2 - 2^2) + ... + ((n+1)^2 - n^2) &= 2 \sum_{i =1}^n i + \sum_{i = 1}^n 1 \\\ (n+1)^2 - 1^2 &= 2 \sum_{i = 1}^n i + n \end{aligned}$$

</div>

We used the fact that $$\sum 2x = 2\sum x$$ and $$\sum_{i = 1}^n 1 = 1 + 1 + ... + 1 = n$$.

Now, we can rearrange for $$\sum_{i = 1}^n i$$:

<div align=center>

$$\begin{aligned} (n+1)^2 - 1^2 &= 2 \sum_{i = 1}^n i + n \\\ 2\sum_{i = 1}^n i &= (n+1)^2 - n - 1 \\\ \sum_{i = 1}^n i &= \frac{n^2 + 2n + 1 - n - 1}{2} \\\ &= \boxed{\frac{n(n+1)}{2}} \end{aligned}$$

</div>

This confirms the result we saw before. 



