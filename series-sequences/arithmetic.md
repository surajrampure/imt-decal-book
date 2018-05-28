# Arithmetic Sequences and Series

An **arithmetic sequence** is defined by a starting term $$a$$ and a common difference $$d$$. In the sequence, the difference between consecutive terms is constant (and equal to the common difference). For example:

$$
3, 5, 7, 9, 11...
$$

is an arithmetic sequence with first term $$a = 3$$ and common difference $$d = 2$$. 

Notice that the second term is the first term with the common difference added once, and the third term is the first with the common difference added twice. Then:

$$
t_k = a + (k-1)d
$$

represents the $$k$$th term in the series, assuming that we start counting at 1. (Recall that when we studied the binomial theorem, our general term was 0-indexed)

<br>

## Sum of an Arithmetic Sequence

### Sum of First $$n$$ Natural Numbers

Before we derive the formula for an arithmetic series, i.e. the sum of an arithmetic sequence, we will look at the sum of perhaps the most naturally arithmetic series – the set of (positive) natural numbers!

Suppose we want to find the sum of the first $$n$$ natural numbers, that is:

$$
S = 1 + 2 + 3 + ... + (n-2) + (n-1) + n
$$

We can rewrite $$S$$ backwards:

$$
S = 1 + 2 + 3 + ... + (n-2) + (n-1) + n \\
S = n + (n-1) + (n-2) + ... + 3 + 2 + 1
$$

Notice that the first term in the top line and first term in the bottom line add to $$n+1$$, as do the second terms, third terms, and so on and so forth. It should be noted that $$n + 1$$ is precisely the sum of the first and last terms of the sequence we are trying to sum.

$$
2S = (n+1) + (n+1) + (n+1) + ... + (n+1) + (n+1) + (n+1) \\
\implies 2S = n(n+1) \\
\implies S = \frac{n(n+1)}{2}
$$

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