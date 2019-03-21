<title>Primality and Divisibility – IMT DeCal</title>

# Primality and Divisibility

_by Suraj Rampure_<br>
_Last modified: March 21, 2019_

---

<br>

<!--

Jump to:
* [Division Algorithm](#divalg)
	* [Divisibility](#divisibility)
* [Prime Numbers](#primes)
	* [Finding Primes](#findingprimes)
* [Fundamental Theorem of Arithmetic](#fta)
	* [Determining Prime Factorizations](#determiningpf)
	* [Proof: No Largest Prime](#proofnolargest)
* [Greatest Common Divisors and Lowest Common Multiples](#gcdlcm)
	* [Greatest Common Divisor](#gcd)
	* [Linear Combinations](#lincomb)
	* [Euclid's GCD Algorithm](#euclid)
	* [Lowest Common Multiples](#lcm)

<br>

-->

In this note, we will introduce many of the fundamental ideas in number theory.

<br>

<a name='divalg'>

## Division Algorithm
---

</a>

The division algorithm states that **if $$n$$ is any integer and $$d$$ is a positive integer, there exist unique integers $$q, r$$ such that**

<div align=center>

$$\boxed{n = dq + r}$$

</div>

**where $$0 \leq r < d$$**.

Here, we say that $$n$$ is the dividend, $$d$$ represents the divisor, $$q$$ represents the quotient, and $$r$$ represents the remainder.

For example, if we are considering the division of $$25$$ by $$3$$, we can say $$25 = 3 \cdot 8 + 1$$, which tells us the quotient when performing this division is $$8$$, and the remainder is $$1$$. 

As another example, we can consider the division of $$-33$$ by $$5$$: we can say $$-33 = 5 \cdot (-7) + 2$$. Notice, we still have the notion of divisors, quotients, and remainders, even when the dividend is negative. This will be especially important when we look at the following chapter.

Admittedly, the division algorithm is nothing but a fancy representation of our results from division. However, the structure that it defines will become useful to us shortly.

<br>

<a name='divisibility'>

### Divisibility
---

</a>

In the case where $$r = 0$$ in $$n = dq + r$$, we can say that "$$d$$ **divides** $$n$$", represented visually as

<div align=center>

$$\boxed{d | n}$$

</div>

Another way of phrasing this is that $$d$$ is a **factor** of $$n$$, or $$n$$ is a **multiple** of $$d$$. 

More formally, if we have that

<div align=center>

$$\forall a \in \mathbb{N}, b \in \mathbb{Z}, a | b \implies \exists c \in \mathbb{Z}: b = ac$$

</div>

Here, we are saying that if $$a$$ divides $$b$$, then there must exist some integer $$c$$ that we can multiply by $$a$$ to get $$b$$. For example, we can say that $$8 | 24$$, since there exists some integer to multiply $$8$$ by to get $$24$$ ($$8 \cdot 3 = 24$$), but that $$\neg (5 | 24)$$, since there is no integer we can multiply $$5$$ by to get us $$24$$.

Note: Often times we will re-arrange the statement to be of the form $$n - dq = r$$ when we are concerning ourselves with the remainder. This is the same statement.

<br>

<a name='primes'>

## Prime Numbers
---

</a>

We say a natural number $$p$$ is **prime** if and only if its only two divisors are $$1$$ and $$p$$ itself. If $$p$$ has factors other than $$1$$ and $$p$$, we call it **composite**. _Note: $$1$$ is neither prime nor composite._

The smallest few prime numbers are $$2, 3, 5, 7, 11, 13, ...$$. However, it turns out that there are infinitely many primes, i.e. that there is no largest prime number. We will look at a proof of this after formalizing the Fundamental Theorem of Arithmetic.

<br>

<a name='findingprimes'>

### Finding Primes
---

</a>

Often, we like to answer the question, is $$n$$, is $$n$ prime?

One solution would be to look at all naturals between $$2$$ and $$n-1$$, inclusive, and check to see if they divide $$n$$.

```py
def is_prime(n):
	if n <= 1:
		return False
	for i in range(2, n):
		if n % i == 0:
			return False
	return True
```

However, this is significantly redundant. It turns out that we only need to check up to and including $$\lfloor\sqrt{n}\rfloor$$. This is because, if $$n$$ is not prime, then we can find $$a, b$$ such that $$n = ab$$. If we have $$a > \sqrt{n}$$ and $$b > \sqrt{n}$$, then $$ab > n$$, thus we must have at least one of $$a, b$$ being less than or equal to $$\sqrt{n}$$. If we cannot find any such factor, then $$n$$ must be prime.

An intuitive way to think about this – consider $$100 = 10^2$$. Suppose we want to find $$a, b$$ such that $$ab = 100$$. If we increase $$a$$, we must decrease $$b$$ in order for the product to remain the same. (Credits to **[Stack Overflow](https://stackoverflow.com/questions/5811151/why-do-we-check-up-to-the-square-root-of-a-prime-number-to-determine-if-it-is-pr)** for that example.)


An updated implementation of the above:

```py
def is_prime(n):
	if n <= 1:
		return False
	for i in range(2, int(n**0.5) + 1):
		if n % i == 0:
			return False
	return True
```

<br>

Another question we may want to answer: given some $$n$$, how can we find all of the primes up to and including $$n$$? One way is to implement the **[Sieve of Eratosthenes](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes)**. We will not discuss it in depth here, but below is an interactive image showing how the algorithm works (taken from the above link).

<div align=center>

<img src='sieve.gif' width=300>

</div> 


<br>

<a name='fta'>

## Fundamental Theorem of Arithmetic
---

</a>

The **Fundamental Theorem of Arithmetic** states that any natural number $$n > 1$$ is either a prime or can be written as a unique product of prime factors.

For example, we can say that 

<div align=center>

$$\begin{align*}2520 &= 2 \cdot 2 \cdot 2 \cdot 3 \cdot 3 \cdot 5 \cdot 7 \\\ &=5 \cdot 7 \cdot 3 \cdot 2 \cdot 3 \cdot 2 \cdot 2 \\\ &= 2^3 \cdot 3^2 \cdot 5 \cdot 7 \end{align*}$$

</div>

FTA states that 1) $$2520$$ can be written as a product of primes, and 2) any product of primes that equates to $$2520$$ will consist of three $$2$$s, two $$3$$s, one $$5$$, and one $$7$$.

As a result, we usually think of numbers in their **canonical representation**, that is, in the form

<div align=center>

$$\boxed{n = p_1^{a_1} p_2^{a_2} ... p_k^{a_k}}$$

</div>

where $$p_1, p_2, ... , p_k$$ represent the prime factors of $$n$$ and $$a_1, a_2, ... , a_k$$ represent their multiplicities ($$a_i \in \mathbb{N}_0$$). Note, we can use as many primes as we want, as we can set $$a_i = 0$$ if we are not going to use that factor. For example, we could, if we needed to, say $$75 = 2^0 3^1 5^2 7^0 11^0 ... 101^0$$.

_Note 1: The FTA is a reason why we don't consider $$1$$ to be prime. If it were prime, then we could say $$10 = 1 \cdot 2 \cdot 5 = 1^2 \cdot 2 \cdot 5 = 1^{100} \cdot 2 \cdot 5 = ...$$, which are technically all different representations, though the FTA says that there is only one unique representation of each number._

_Note 2: We restricted the exponents $$a_i$$ to be non-negative integers. However, if we allow $$a_i$$ to take on the value of negative integers as well, then this can form the basis for all rational numbers as well!_

<br>

<a name='determiningpf'>

### Determining Prime Factorizations
---

</a>

To determine the prime factorization of $$n$$, one method is to repeatedly divide $$n$$ by the smallest possible prime number until it no longer is a multiple of this number. We then move up to the next largest prime and continue this process until your number is completely factored into primes.

For example, let's determine the prime factorization of $$336$$:

<div align=center>

$$336 = 2 \cdot 168 = 2^2 \cdot 84 = 2^3 \cdot 42 = 2^4 \cdot 21 = 2^4 \cdot 3 \cdot 7$$

</div>

Thus, we'd say the prime factorization of $$336$$ is $$2^4 \cdot 3 \cdot 7$$. Note, the rule that we must repeatedly divide by the smallest possible prime is not hard and fast, since multiplication can be done in any order. 

There is a common trick we use when a number is a multiple of $$10$$ – if a number is a multiple of $$10$$, it is a multiple of both $$2$$ and $$5$$. For example:

<div align=center>

$$3600 = 2 \cdot 5 \cdot 360 = 2^2 \cdot 5^2 \cdot 36 = 2^2 \cdot 5^2 \cdot 6^2 = 2^2 \cdot 5^2 \cdot (2 \cdot 3)^2 = 2^4 \cdot 3^2 \cdot 5^2$$

</div>

_Note: It is recommended to consult the lecture video for this exercise, as it is significantly easier to learn by watching someone do it first._


<br>

<a name='proofnolargest'>

### Proof: Infinitely Many Primes
---

</a>

Let's proceed by contradiction. Let's assume that there are only finitely many primes, say, $$p_1, p_2, p_3, ... , p_{n-1}, p_n$$. 

Now, consider $$q = p_1p_2p_3 ... p_{n - 1}p_n + 1$$. None of the primes $$p_1, p_2, ..., p_n$$ evenly divide $$q$$, as they all leave a remainder of $$1$$. Now, we have two cases:

1. $$q$$ is prime: This means we have a prime that was not in our list $$p_1, p_2, ... , p_n$$, since $$q$$ is bigger than each of these – this is a contradiction of the fact that our list contained every prime
2. $$q$$ is not prime: This means there must exist some prime $$p'$$ such that $$p' | q$$. However, $$p'$$ cannot be any one of $$p_1, p_2, ... , p_{n - 1}, p_n$$. To see this, suppose $$p' = p_i$$, where $$p_i$$ is one of the primes in the original list:

<div align=center>

$$q = p_1p_2...p_{n-1}p_n + 1$$

$$\frac{q}{p'} = \frac{p_1p_2....p_{n-1}p_n}{p'} + \frac{1}{p'}$$

$$n_2 = n_1 + \frac{1}{p'}, n_1, n_2 \in \mathbb{N}$$

</div>

If $$p'$$ was equal to one $$p_i$$, then the quotient $$\frac{p_1p_2...p_{n-1}p_n}{p'}$$ would be a natural number. However (since we're assuming $$p' | q$$) this would mean that we would need $$p' | 1$$, which is impossible, since $$p' \neq 1$$ (as $$1$$ is not prime). Therefore, $$p'$$ is a prime that was not in the original list.

All of this is to say, by contradiction, the set of all primes is not finite, and thus there are infinitely many primes, and no largest prime.

_Note: The second part of the proof isn't stating that $$q$$ must be prime. It is simply stating that our original list did not contain every single prime, and thus, there is no such list._

<br>

<a name='gcdlcm'>

## Greatest Common Divisors and Lowest Common Multiples
---

</a>

We defined the canonical representation of an integer as $$n = p_1^{a_1} p_2^{a_2} ... p_k^{a_k}$$. We can also express standard multiplication (and division, for that matter) in terms of this new representation. 

Suppose $$n_1 = p_1^{a_1} p_2^{a_2} ... p_k^{a_k}$$ and $$n_2 = p_1^{b_1} p_2^{b_2} ... p_k^{b_k}$$ (remember from above, we can set $$a_i$$ or $$b_j$$ to $$0$$ if that factor is not in use). Then, by exponent laws,

<div align=center>

$$n_1 \cdot n_2 = p_1^{a_1 + b_1} p_2^{a_2 + b_2} ... p_k^{a_k + b_k}$$

</div>

For example, suppose we have $$1200$$ and $$2520$$. 

<div align=center>

$$\begin{align*}1200 &= 2^4 \cdot 3^1 \cdot 5^2 \cdot 7^0 \\\ 2520 &= 2^3 \cdot 3^2 \cdot 5^1 \cdot 7^1 \\\ \implies 1200 \cdot 2520 &= 2^7 \cdot 3^3 \cdot 5^3 \cdot 7^1 \end{align*}$$

</div>

<br>

<a name='gcd'>

### Greatest Common Divisor
---

</a>

Now, consider the idea of the **greatest common divisor** of two numbers $$a, b$$, denoted by $$\gcd(a, b)$$. This is, we want the largest $$d$$ such that $$(d | a) \wedge (d | b)$$. We can start by looking at the prime factorization of $$a$$ and $$b$$ – as an example, let's consider $$1200$$ and $$2520$$ from above.

We can consider each prime base separately:

- $$1200$$ has a divisor of $$2^4$$ and $$2520$$ has a divisor of $$2^3$$. The largest power of $$2$$ that is a factor of both is $$2^3$$.
- $$1200$$ has a divisor of $$3^1$$ and $$2520$$ has a divisor of $$3^2$$. The largest power of $$3$$ that is a factor of both is $$3^1$$.
- Similarly, we will choose $$5^1$$ and $$7^0$$.

Then, our greatest common divisor will be the product of each of the quantities we described above, i.e.

<div align=center>

$$\gcd(1200, 2520) = 2^3 \cdot 3^1 \cdot 5^1 \cdot 7^0 = 120$$

</div>

We can extend this to general $$a, b$$: Suppose $$a = p_1^{a_1} p_2^{a_2} ... p_k^{a_k}$$ and $$b = p_1^{b_1} p_2^{b_2} ... p_k^{b_k}$$. We can then say

<div align=center>

$$\boxed{\gcd(a, b) = p_1^{\min(a_1, b_1)} p_2^{\min(a_2, b_2)} ... p_k^{\min(a_k, b_k)}}$$

</div>

Note: Iff $$\gcd(a, b) = 1$$, we say $$a$$ and $$b$$ are **relatively prime**, or **coprime**, i.e. they share no common factors (other than $$1$$).

<br>

<a name='lincomb'>

### Linear Combinations
---

</a>

Suppose $$a, b \in \mathbb{N}$$. Then, there exist $$u, v \in \mathbb{Z}$$ such that

<div align=center>

$$\boxed{au + bv = \gcd(a, b)}$$

</div>

The theorem states that there always exists a linear combination of $$a$$ and $$b$$ that sums to $$\gcd(a, b)$$. We won't prove this here, but for now, let's give an example.

Consider $$\gcd(12, 15) = 3$$. This theorem states that we can find $$u, v$$ such that $$12u + 15v = 3$$. One such pair is $$u = 4, v = -3$$. _Note: One of $$u, v$$ will likely be negative._

A good question is, how can we determine $$u, v$$? This is a process we will become very familiar with later in this chapter. An important note to make – we will use this extensively in the case where $$\gcd(a, b) = 1$$, i.e. in finding coefficients such that $$au + bv = 1$$, though this holds in general.

<br>

<a name='euclid'>

### Euclid's GCD Algorithm
---

</a>

There's another method that we can use to determine prime factorizations, called the **Euclidean algorithm.** Let's take a look:

```py
def gcd(a, b):
	assert a >= b

	if b == 0:
		return a

	return gcd(b, a % b)
```

_The `%` sign in Python refers to the "modulo" operator, which we haven't formally discussed yet. `a % b` is the remainder when dividing `a` by `b`, i.e. it is $$r$$ in $$a = bq + r$$._

Notice, the Euclidean algorithm works recursively. Additionally, it assumes the first argument is greater than or equal to the second. This is not really an issue, as $$\gcd(a, b) = \gcd(b, a)$$.

Let's look at an example call to the algorithm:

```
gcd(290, 14)
	gcd(14, 10)
		gcd(10, 4)
			gcd(4, 2)
				gcd(2, 0)
```

Now that we reached $$b = 0$$, we've determined that $$\gcd(290, 14) = 2$$.

It turns out, we can use what is known as the **extended Euclidean algorithm** to determine coefficients $$u, v$$ in $$au + bv = \gcd(a, b)$$. This is something we will look at when determining modular inverses.

<br>

<a name='lcm'>

### Lowest Common Multiples
---

</a>

Recall, when determining the greatest common divisor of two numbers, we took the lower of the two powers for each prime base. Our exponents in the resulting canonical representation were of the form $\min(a_i, b_i)$.

With the **lowest common multiple**, $$\text{lcm}(a, b)$$, we end up doing the opposite. Let's consider an example – let's determine $$\text{lcm}(1200, 2520)$$.

<div align=center>

$$\text{gcd}(1200, 2520) = 2^{min(4, 3)} \cdot 3^{min(1, 2)} \cdot 5^{min(2, 1)} \cdot 7^{min(0, 1)} = 2^3 \cdot 3^1 \cdot 5^1 \cdot 7^0 = 120$$

$$\text{lcm}(1200, 2520) = 2^{max(4, 3)} \cdot 3^{max(1, 2)} \cdot 5^{max(2, 1)} \cdot 7^{max(0, 1)} = 2^4 \cdot 3^2 \cdot 5^2 \cdot 7^1 = 25200$$

</div>

Intuitively speaking, a divisor will always be less than or equal to a number, while a multiple will always be greater than or equal to a number. $$2^4$$ divides both $$2^4$$ and $$2^3$$, so we choose $$4$$ to be the exponent on $$2$$ in our LCM.

In general, we have the following formula, given $$a = p_1^{a_1} p_2^{a_2} ... p_k^{a_k}$$ and $$b = p_1^{b_1} p_2^{b_2} ... p_k^{b_k}$$:

<div align=center>

$$\boxed{\text{lcm}(a, b) = p_1^{\max(a_1, b_1)} p_2^{\max(a_2, b_2)} ... p_k^{\max(a_k, b_k)}}$$

</div>

<br>

We will end this note with the proof of the following fact:

<div align=center>

$$a \cdot b = \text{lcm}(a, b) \cdot \gcd(a, b)$$

</div>

To be rigorous, we need to first start by proving the fact that for any two real numbers $$x, y$$, $$\max(x, y) + \min(x, y) = x + y$$. 

- Case 1: $$x > y$$: $$\max(x, y) + \min(x, y) = x + y$$
- Case 2: $$x = y$$: $$\max(x, y) + \min(x, y) = x + x = y + y = x + y$$
- Case 3: $$x < y$$: $$\max(x, y) + \min(x, y) = y + x = x + y$$

You can also reason about this intuitively – if one of the elements is the maximum, the other will be the minimum.

Now, the proof comes easily from the definitions of greatest common divisor and lowest common multiple:

<div align=center>

$$\begin{align*} \text{lcm}(a, b) \cdot \gcd(a, b) &= p_1^{\max(a_1, b_1)} p_2^{\max(a_2, b_2)} ... p_k^{\max(a_k, b_k)} \cdot p_1^{\min(a_1, b_1)} p_2^{\min(a_2, b_2)} ... p_k^{\min(a_k, b_k)} \\\ &= p_1^{\max(a_1, b_1) + \min(a_1, b_1)} p_2^{\max(a_2, b_2) + \min(a_2, b_2)} ... p_k^{\max(a_k, b_k) + \min(a_k, b_k)} \\\ &= p_1^{a_1 + b_1} p_2^{a_2 + b_2} ... p_k^{a_k + b_k} \\\ &= a \cdot b \end{align*}$$

</div>  

The last step comes from the definition of canonical form multiplication we saw above.

<br>
