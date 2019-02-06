<title>Sigma and Pi Notation – Appendix</title>

# Sigma and Pi Notation
---

<br>

Jump to:
- [Sigma Notation](#summation)
	- [Properties of Sigma Notation](#sigmaproperties)
- [Pi Notation](#pi)
	- [Properties of Pi Notation](#piproperties)
	- [Factorial](#factorial)
- [Common Misconceptions](#misconceptions)


Here, we'll introduce and review some notation that you should be familiar with during this course. 

<a name='summation'>

## Sigma Notation
---

</a>

The $$\sum$$ symbol, read "sigma", is used to indicate a sum of some sequence. For example, $$\sum_{i = 1}^n i^2$$ represents the sum of the squares of all integers from 1 to $$n$$, i.e.

<div align=center>

$$\sum_{i = 1}^6 i^2 = 1^2 + 2^2 + 3^2 + 4^2 + 5^2 + 6^2$$

</div>

$i$, the index of summation, tells us where to start and end our sum.

In general, we have

<div align=center>

$$\boxed{\sum_{i = a}^b f(i) = f(a) + f(a+1) + f(a+2) + ... + f(b-1) + f(b)}$$

</div>

This is similar to a Python for-loop:

```
sum = 0
for i in range(a, b+1):
	sum += f(i)
```

Notice, in our summation notation, our ending index is _inclusive_, as opposed to a Python for-loop. 

<br>

Here are a few more examples:

<div align=center>

$$\sum_{j = 5}^{10} \frac{j}{j + 1} = \frac{5}{6} + \frac{6}{7} + \frac{7}{8} + \frac{8}{9} + \frac{9}{10} + \frac{10}{11}$$

$$\sum_{k = -2}^2 e^{5k} = e^{-10} + e^{-5} + e^5 + e^{10}$$

$$\sum_{t = 1}^\infty t^{-2} = \frac{1}{1^2} + \frac{1}{2^2} + \frac{1}{3^2} + ... $$

</div>

(Fun fact: The last example above, $$\sum_{t = 1}^\infty t^{-2}$$, is known to have the exact value $$\frac{\pi^2}{6}$$.)

<br>

<a name="sigmaproperties">

### Properties of Sigma Notation

</a>

---

#### Property 1: Linearity of Constants

<div align=center>

$$\boxed{\sum_{i = m}^n ca_i = c\sum_{i = m}^n a_i}$$

</div>

As a quick example, $$\sum_{i = 1}^3 5i = 5 + 10 + 15 = 30$$ is the same as $5 \sum_{i = 1}^3 i = 5 \cdot (1 + 2 + 3) = 5 \cdot 6 = 30$$.

A proof of this follows:

<div align=center>

$$\begin{aligned} \sum_{i = m}^n ca_i &= ca_m + ca_{m + 1} + ca_{m + 2} + ... + ca_n \\\ &= c(a_m + a_{m + 1} + a_{m + 2} + ... + a_n) \\\ &= c \sum_{i = m}^n a_i \end{aligned}$$

</div>

A corollary of this property is the following fact:

<div align=center>

$$\sum_{i = 1}^n c = cn$$

</div>

where $$c$$ is a constant that is independent of $$n$$. In fact, $$c$$ could also be replaced with some variable $$x$$; as long the quantity being summed is independent of the index of summation, this fact holds true.

<br>

#### Property 2: Separability of Two Sums

<div align=center>

$$\boxed{\sum_{i = m}^n (a_i + b_i) = \sum_{i = m}^n a_i + \sum_{i = m}^n b_i}$$

</div>

Again, a proof:

<div align=center>

$$\begin{aligned} \sum_{i = m}^n (a_i + b_i) &= (a_m + b_m) + (a_{m + 1} + b_{m + 1}) + (a_{m + 2} + b_{m + 2}) + ... + (a_n + b_n) \\\ &= (a_m + a_{m + 1} + a_{m + 2} + ... + a_n) + (b_m + b_{m + 1} + b_{m + 2} + ... + b_n) \\\ &= \sum_{i = m}^n a_i + \sum_{i = m}^n b_i \end{aligned}$$

</div>

<br>

Another useful property of sums (that isn't enough of a "property" to warrant giving it its own number) is the fact that we can separate a sum into multiple sums:

<div align=center>

$$\begin{aligned} \sum_{i = 1}^n 2^i &= \sum_{i = 1}^{n - 1} 2^i + 2^n \\\ &= \sum_{i = 1}^{n-2} 2^i + \sum_{i = n-2}^n 2^i \\\ &= \sum_{i = 1}^m 2^i + \sum_{i = m}^n 2^i \end{aligned}$$

</div>

<br>

<a name='pi'>

## Pi Notation
---

</a>

The upper-case pi symbol, $$\Pi$$, represents a product, just as the upper-case sigma symbol represented a sum. For example,

<div align=center>

$$\prod_{i = 3}^6 (x + 2^i) = (x + 2^3) (x + 2^4) (x + 2^5) (x + 2^6)$$

</div>

In general, we have

<div align=center>

$$\boxed{\prod_{i = a}^b f(i) = f(a) \cdot f(a+1) \cdot f(a+2) \cdot ... \cdot f(b)}$$

</div>

<br>

<a name="piproperties">

### Properties of Pi Notation

</a>

---

As we did for sigma notation, there are similar properties you can derive for pi notation. We won't go through the steps of proving these properties here, but they can be proven in a similar fashion.


#### Property 1: Separability of Constants


<div align=center>

$$\boxed{\prod_{i = 1}^n ca_i = c^n \prod_{i = 1}^n a_i}$$

</div>

In fact, we can rewrite the first property more generally as $$\prod_{i = m}^n ca_i = c^{m - n + 1} \prod_{i = m}^n a_i$$. The exponent of $m - n + 1$ comes from the fact that between $$m$$ and $$n$$, there are $$m - n + 1$$ integers (including both $$m$$ and $$n$$).

<br>

#### Property 2: Separability of Multiple Products

<div align=center>

$$\boxed{\prod_{i = m}^n a_ib_i = \left( \prod_{i = m}^n a_i \right) \left( \prod_{i = m}^n b_i \right)}$$

</div>

Notice, with sigma notation we were able to separate a sum of two sequences into two separate sums. With pi notation, we are able to separate a product of two sequences into two separate products. 


<br>

<a name="factorial">

### Factorial
---

</a>

There is one important function definition that can be expressed in terms of pi notation:

<div align=center>

$$\prod_{i = 1}^n i = 1 \cdot 2 \cdot 3 \cdot ... \cdot (n-1) \cdot n = n!$$

</div>

This is read as "$$n$$ **factorial**", and we will use it heavily in the counting section of the course. 

The factorial function is often implemented recursively in code:

```Py
def fact(n):
	if n == 0 or n == 1:
		return 1

	return n * fact(n-1)
```

<br>

<a name='misconceptions'>

## Common Misconceptions
---

</a>

When first learning how to manipulate sums, students often take the following equalities to be true. However, they are not: 

<div align=center>

$$\sum_{i = m}^n a_i b_i \neq \left( \sum_{i = m}^n a_i \right) \left( \sum_{i = m}^n b_i \right)$$

$$\sum_{i = m}^n \frac{a_i}{b_i} \neq \frac{\sum_{i = m}^n a_i}{\sum_{i = m}^n b_i}$$

</div>

For example, consider $$a_1 = 1, a_2 = 2, b_1 = 1, b_2 = 2$$.
- (Statement 1) LHS: $$1 \cdot 1 + 2 \cdot 2 = 5$$, RHS: $$(1 + 2) (1 + 2) = 9$$, but $$5 \neq 9$$
- (Statement 2) LHS: $$\frac{1}{1} + \frac{2}{2} = 2$$, RHS: $$\frac{1 + 2}{1 + 2} = 1$$, but $$2 \neq 1$$

The above expressions are true if we replace the sums with products, though (as seen in the Properties of Pi Notation section).

<br>

