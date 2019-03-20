<title>Binomial Theorem – IMT DeCal</title>


# Binomial Theorem
---

<br>

<!--

Jump to:
- [Motivation](#motivation)
- [The Combinatorial Approach](#combinatorial)
- [The Binomial Theorem, Formalized](#formal)
- [The General Term](#general)
- [Applications](#applications)
	- [Sum of Coefficients](#sumcoef)
	- [Determining Coefficients without Expansion](#withoutexp)
	- [Sum of $$n$$-th row of Pascal's Triangle](#pascal)
- [Extensions](#extensions)
	- [The "Trinomial" Theorem?](#trinomial)
	- [The Multinomial Theorem](#multinomial)
	- [Product of Two Binomial Expansions](#product)

-->

In this note, we will extend our discussion of the combinatorial term and Pascal's triangle into a useful concept in algebra, known as the binomial theorem. Recall, a binomial is a polynomial with two terms, where terms are items joined by addition. A trinomial is a polynomial with three terms.


<a name='motivation'>

## Motivation
---

</a>


Consider the following expansion of the product of two binomials:

<div align=center>

$$
(a + b) (c + d)  = a(c + d) + b(c + d) = ac + ad + bc + bd
$$

</div>

To compute the final expansion, we multiplied every combination of terms in the first polynomial by terms in the second polynomial. In this example, we multiplied two different binomials --- polynomials with two terms --- both of which were used two different variables. Let's concentrate our efforts on a simpler case, that is, binomials multiplied by themselves.

What if we wanted to expand $$(x + y)^2$$? We can follow the same technique as above --- multiply $$x$$ by $$x + y$$, yielding $$x^2 + xy$$, and $$y$$ by $$x + y$$, yielding $$xy + y^2$$ and sum the result, yielding $$x^2 + 2xy + y^2$$.

What if instead we wanted to expand $$(x + y)^3$$? One approach is to write $$(x+y)^3$$ as $$(x+y)(x+y)(x+y)$$, and manually try and multiply every combination of one item from the first bracket, one item in the
second bracket, and one item in the third bracket. If we were to do this, we would expand in the following way:

<div align=center>

$$(x+y)(x+y)(x+y) = xxx + xxy + xyx + xyy + yxx + yxy + yyx + yyy$$

</div>

However, if we were to try to expand $$(x+y)^4$$ in this way, we'd have a mess on our hands. Another approach is to recognize that $$(x + y)^3$$ is the product of $$(x+y)^2$$, which we know to be $$x^2 + 2xy + y^2$$, with $$x + y$$. We can then multiply each term in $$x^2 + 2xy + y^2$$ by each term in $$x + y$$, to yield the final expansion of $$x^3 + 3x^2y + 3xy^2 + y^3$$. Sure, this works, however with exponents greater than $$3$$ one can see that this process becomes messy.

<br>

<a name="combinatorial">

## The Combinatorial Approach
---

</a>

<br>

Let's approach this problem differently. Consider the expansion of $$(x + y)^3$$, which we can write as $$(x+y)(x+y)(x+y)$$. We know that each term in its expansion must contain one term from each polynomial being multiplied. Since the only possible terms are $$x$$ and $$y$$, and there are three polynomials being multiplied, the each term in the expansion of $$(x+y)^3$$ will contain either 3 $$x$$s, $$2$$ $$x$$s and 1 $$y$$, 1 $$x$$ and 2 $$y$$s, or 3 $$y$$s. Now, we need to determine the number of $$x^3$$, $$x^2y$$, $$xy^2$$ and $$y^3$$ terms that exist.

To determine the coefficient on $$x^3$$, we think, how many ways can we choose 3 $$x$$s, from a possible 3? This is precisely $${3 \choose 3}$$. Similarly, to determine the coefficient on $$xy^2$$, we ask, how many ways can we choose 1 $$x$$ from a possible of 3? Again, this is $${3 \choose 1}$$. We don't need to consider the number of ways to choose the $$y$$s in these cases, as whatever isn't chosen to be an $$x$$ is automatically a $$y$$. Putting all of this together, we have:

<div align=center>

$$(x + y)^3 = {3 \choose 3}x^3 + {3 \choose 2} x^2y + {3 \choose 1} xy^2 + {3 \choose 0} y^3 = x^3 + 3x^2y + 3xy^2 + y^3$$

</div>

This confirms our result from the previous section. One point of interest is the fact that since $${3 \choose i} = {3 \choose 3 - I}$$, we can treat our coefficients as either the number of ways to choose $$x$$s OR the number of ways to choose $$y$$s. This means that we can also write the above result as:

<div align=center>

$$(x + y)^3 = {3 \choose 0}x^3 + {3 \choose 1} x^2y + {3 \choose 2} xy^2 + {3 \choose 3} y^3 = x^3 + 3x^2y + 3xy^2 + y^3$$

</div>

In general, we can write $$(x + y)^n$$ as:

<div align=center>

$$(x+y)^n = (x+y)(x+y)(x+y)...(x+y)$$

</div>

To simplify the expansion, we need to determine the number of ways to choose $$n$$ $$x$$s, $$n-1$$ $$x$$s and 1 y, $$n-2$$ $$x$$s and 2 $$y$$s, so on and so forth, until we find the number of ways to choose $$n$$ $$y$$s. The result is presented in the following section.

<br>

<a name='formal'>

## The Binomial Theorem, Formalized
---

</a>

The binomial theorem states the following: 

<div align=center>

$$\boxed{(x + y)^n = {n \choose 0}x^n + {n \choose 1}x^{n-1}y + {n \choose 2}x^{n-2}y^2 + ... + {n \choose n-1}xy^{n-1} + {n \choose n}y^n = \sum_{k = 0}^n {n \choose k} x^{n-k}y^k}$$

</div>

It is worth noting that since we're using the combinatorial term to determine coefficients, the coefficients in the expansion of $$(x + y)^n$$ are the entries in the $$n$$-th row of Pascal's triangle. However, rarely will we expand $$(x + y)^n$$ itself; we will typically expand more complicated binomials raised to other exponents.

Also, the term that we've introduced as the combinatorial term – $${n \choose k}$$ – is sometimes referred to as the "binomial coefficient", because of its significance in the binomial theorem. 

#### Example

Let's determine the expansion of $$(3a^2 - 2b)^5$$. In this case, we have $$x = 3a^2$$, $$y = -2b$$ and $$n = 5$$.

<div align=center>

$$
\begin{aligned}
(3a^2 - 2b)^5 &= {5 \choose 0} (3a^2)^5 + {5 \choose 1} (3a^2)^4 (-2b) + {5 \choose 2} (3a^2)^3 (-2b)^2 + {5 \choose 3} (3a^2)^2 (-2b)^3 + {5 \choose 4} (3a^2) (-2b)^4 + {5 \choose 5}(-2b)^5 \\\ &= 243a^{10} - 810a^8b + 1080a^6b^2 - 720a^4b^3 + 240 a^2b^4 - 32b^5 \end{aligned}
$$

</div>

<br>

<a name='general'>

## The General Term
---

</a>

We define the $$k$$-th term in the expansion of a binomial as $$\boxed{t_k = {n \choose k} x^{n-k}y^k}$$, with $$k$$ ranging from 0 to $$n$$.

In the expansion of $$(3a^2 - 2b)^5$ from the previous section, the general term is:

<div align=center>

$$
\begin{aligned}
t_k &= {5 \choose k} (3a^2)^{5 - k} (-2b)^k \\\ &= {5 \choose k} 3^{5-k} a^{10 - 2k} (-1)^k 2^k b^k \\\ &= (-1)^k {5 \choose k} 2^k 3^{5-k} a^{10 - 2k}b^k \end{aligned}
$$

</div>

You may be asking yourself why we've written the general term this way. With the $$(-1)^k$$ at the front, we can quickly tell whether a term is positive or negative. By splitting the $$2$$, $$3$$, $$a$$ and $$b$$, each exponential base is isolated, simplifying the multiplication process (i.e. we don't need to multiply $$3$$ and $$a^2$$ and then raise that to an exponent; instead, we raise $$3$$ and $$a^2$$ to exponents separately, as we are more likely to know the powers of $$3$$ on their own).


Let's look at another example, namely, the expansion of $$(x^5 - \frac{1}{x^2})^7$$.

<div align=center>

$$
\begin{aligned} t_k &= {7 \choose k} (x^5)^{7-k}(-x^{-2})^{k} \\\ &= (-1)^k {7 \choose k} x^{35 - 5k} x^{-2k} \\\ &= (-1)^k {7 \choose k} x^{35 - 7k} \end{aligned}
$$

</div>

Since $$x^5 - x^{-2}$$ is a function of only one variable, $$x$$, we were able to combine $$(x^5)^{7-k}$$ and $$(x^{-2})^{k}$$ into a single $$x$$ term. Therefore, the general term only contains one variable, instead of two as in the previous example. We will use this fact in the next section to aid us in determining coefficients for arbitrary terms.

<br>

<a name='applications'>

## Applications
---

</a>

Now, we'll look at some of the more direct applications of the binomial theorem. 

<a name='sumcoef'>

### Sum of Coefficients
---

</a>

<br>

In the expansion of an instance of the binomial theorem, if one sets all variables equal to 1, then the result is the sum of the coefficients of in the expansion. Let's consider $$f(x) = (2x - 3x^2)^4$$. If we set $$x = 1$$, then $$f(1) = (-1)^4 = 1$$, telling us that the sum of coefficients in the expansion of $$f(x)$$ should be $$1$$. We can verify this via expansion:

<div align=center>

$$
\begin{aligned}
f(x) &= (2x - 3x^2)^4 \\\ &= {4 \choose 0}(2x)^4 + {4 \choose 1}(2x)^3(-3x^2) + {4 \choose 2}(2x)^2(-3x^2)^2 + {4 \choose 3}(2x)(-3x^2)^3 + {4 \choose 4}(-3x^2)^4 \\\ &= 16x^4 - 96x^5 + 216x^6 - 216x^7 + 81x^8 \\\ \\\ \implies f(1) &= 16 - 96 + 216 - 216 + 81 = -80 + 81 = 1 \end{aligned}$$

</div>

This also works with multivariate binomials, i.e. binomials that are functions of more than one variable (as all previous examples were). In addition to verifying this on your own, you should also think about why this technique works overall. Feel free to ask questions.

An interesting result in the above example is that no matter how large $$n$$ is, the sum of the coefficients in $$(2x - 3x^2)^n$$ is always either $$1$$ or $$-1$$, depending on whether $$n$$ is even or odd. This is interesting, as when $$n = 1000$$, terms of the form $${1000 \choose k}$$ can be on the order of $$10^{30}$$, yet the sum of coefficients is still just $$1$$ - fascinating!

<br>

<a name='pascal'>

### Sum of $$n$$-th row of Pascal's Triangle
---

</a>

The parallels between the binomial theorem and Pascal's triangle were outlined earlier in this article. However, the binomial theorem gives us another way to prove that the sum of the $$n$$-th row of Pascal's triangle is $$2^n$$.

Recall, in Chapter 4, we determined that $${n \choose 0} + {n \choose 1} + ... + {n \choose n} = 2^n$$ by reasoning about the cardinality of the power set for a set of size $$n$$ - in creating a subset of a set of size $$n$$, there are two options for each item, either to include that item or to not include that item. This yields $$2^n$$, which should be the same as taking $0$ items (${n \choose 0}$), or $1$ item (${n \choose 1}$), and so on and so forth.

However, let's look at the expansion of $$(1 + 1)^n$$: 

<div align=center>

$$\begin{aligned} 2^n = (1 + 1)^n &= {n \choose 0}1^n + {n \choose 1}1^{n-1} \cdot 1 + {n \choose 2} 1^{n-2} \cdot 1^2 + ... + {n \choose n-1}1^1 \cdot 1^{n-1} + {n \choose n}1^n \\\ &= {n \choose 0} + {n \choose 1} + ... + {n \choose n-1} + {n \choose n} \end{aligned}$$

</div>

Neat!

<br>

<a name='withoutexp'>

### Determining Coefficients without Expansion
---

</a>

Consider the expansion of $$(2x^3 + x^{-1})^8$$. You should verify that it has the general term $$t_k = {8 \choose k} 2^{8-k}x^{24 - 4k}$$. In the exponent for $$x$$, since there is a $$-4k$$ term, we know that consecutive terms decrease in their exponent by $$4$$ - the first term has exponent $$24$$, the second exponent $$20$$, and so on. (You may be able to see this without calculating the general term, as the "difference in power" between $$2x^3$$ and $$x^{-1}$$ is $$-4$$.)

Suppose we want to find the coefficient on $$x^{16}$$ in the expansion. In the general term, we can set the exponent, $$24-4k$$, equal to $$16$$, and solve for the term number ($$k$$), which in this case is $$2$$. We then can plug $$2$$ into the general term to find $$t_2 = {8 \choose 2}2^{8-2}x^{16}$$, yielding that the coefficient is $${8 \choose 2}2^{8-2} = 56 \cdot 32 = 1792$$.

What if we were asked for the coefficient on $$x^{10}$$? Upon solving $$24 - 4k = 10$$, we yield the solution $$k = \frac{7}{2}$$. However, this doesn't make any sense - $$k$$ represents the term number in the expansion, and must be an integer between $$0$$ and $$8$$ inclusive. Therefore, in this case, there is no $$x^{10}$$ term in the expansion, and we can report that there is no solution.

<br>

<a name='extensions'>

## Extensions
---

</a>


<a name='trinomial'>

### The "Trinomial" Theorem?
---

</a>

What if we would like to expand something of the form $$(x + y + z)^n$$? One option is to treat either $$(x + y)$$ or $$(y + z)$$ as a single term, and use the binomial theorem. However, once again, we can treat this as a combinatorial problem on its own.

Suppose a general term in the expansion of $$(x + y + z)^n$$ contains $$a$$ $$x$$s, $$b$$ $$y$$s and $$c$$ $$z$$s. Then, we must have that $$a + b + c = n$$, since the total number of parentheses we choose from in the expansion must be exactly $$n$$. We can then say the following:

<div align=center>

$$
t_{a, b, c} = \frac{n!}{a! b! c!} x^a y^b z^c
$$

</div>

The coefficient $$\frac{n!}{a!b!c!}$$ comes from the number of ways to arrange $$a$$ $$x$$s, $$b$$ $$y$$s and $$c$$ $$z$$s (think back to counting the number of permutations of MISSISSIPPI).

#### Example

Let's calculate the coefficient of the term containing $$x^4$$ in the expansion of $$(x - 3x^{-2} + 4)^8$$:

<div align=center>

$$
\begin{aligned} t_{a, b, c} &= \frac{8!}{a! b! c!} x^a (-3x^{-2})^b (4)^c
\\\ &= (-1)^b \frac{8!}{a!b!c!}3^b4^c x^{a-2b} \end{aligned}$$

</div>

Setting $$x^{a - 2b} = x^4$$, we require $$a - 2b = 4$$, with the constraints that $$0 \leq a, b, c \leq 8$$ and $$a + b + c = 8$$. If we set $$a = 4$$ and $$b = 0$$, we satisfy the given constraints. We can use this solution as a starting point to find the remaining solutions:

-   $$a = 4, b = 0, c = 4$$

-   $$a = 6, b = 1, c = 1$$

We then find the general terms corresponding to each of these two triplets:

<div align=center>

$$\begin{aligned} t_{4, 0, 4} &= (-1)^0 \frac{8!}{4!0!4!} 3^0 4^4 x^4 = 17920x^4 \\\ t_{6, 1, 1} &= (-1)^1 \frac{8!}{6!1!1!}3^14^1x^4 = - 336x^4 \end{aligned}$$

</div>

Then, in the final expansion, the term containing $$x^4$$ is $$t_{4, 0, 4} + t_{6, 1,1} = 17920x^4 - 336x^4 = 17584x^4$$, and the coefficient of $$x^4$$ is $$17584$$.


#### Generalization

Note that can write the expansion of a trinomial raised to an exponent
as a sum, though it is slightly less meaningful:

<div align=center>
$$
(x + y + z)^n = \sum_{a, b, c :  a + b + c = n} \frac{n!}{a!b!c!}x^ay^bz^c
$$
</div>

<br>

<a name='multinomial'>

### The Multinomial Theorem
---

</a>

We can generalize this even further. Let's introduce the **multinomial coefficient**:

<div align=center>

$$
\boxed{{n \choose k_1, k_2, ... k_m} = \frac{n!}{k_1!k_2! ... k_m!}}
$$ 

</div>

Under the assumption $$k_1 + k_2 + ... + k_m = n$$, this term is the number of ways to select one subset of size $$k_1$$, one subset of size $$k_2$$, ... and one subset of size $$k_m$$ from a group of $$n$$ items. Notice that with $$m = 2$$, this is the same as the binomial coefficient that we're used to.

Then: 

<div align=center>

$$
(x_1 + x_2 + ... + x_m)^n = \sum_{k_1 + k_2 + ... + k_m = n} {n \choose k_1, k_2, ... k_m} \prod_{i = 1}^m x_i^{k_i}
$$

</div>

<br>

<a name='product'>

### Product of Two Binomial Expansions
---

</a>

Let's switch gears. Rather than expanding from binomials to trinomials or general multinomials, what if we instead take a look at the product of two binomials, each raised to different exponents? Let's illustrate this with an example!

Let $$f(x, y) = (2x - 3y)^5$$ and $$g(x, y) = (x^3 - 3xy^2)^9$$. Our goal will be to find the general term of the product $$f(x, y) \cdot g(x, y)$$, and determine the existence of certain terms.

First, we find the general term of each, using the index variable $$i$$ for $$f(x, y)$$ and $$k$$ for $$g(x, y)$$ (these choices are arbitrary, but we need some way of differentiating the two, as you will see). You should verify these on your own:

<div align=center>

$$
\begin{aligned} t_i &= (-1)^i {5 \choose i} 2^{5-i} 3^i x^{5-i} y^i \\\ t_k &= (-1)^k {9 \choose k} 3^k x^{27-2k} y^{2k} \end{aligned}$$

</div>

Now, to find the general term of the product, we take the product of the two general terms:

<div align=center>

$$
\begin{aligned} t_{i, k} &= (-1)^i {5 \choose i} 2^{5-i} 3^i x^{5-i} y^i (-1)^k {9 \choose k} 3^k x^{27-2k} y^{2k} \\\ &= (-1)^{i+k} {5 \choose i} {9 \choose k} 2^{5-i} 3^{i+k} x^{32 - i - 2k} y^{i+2k} \end{aligned}
$$

</div>

This tells us that the product of the $$i$$th term of $$f(x)$$ and $$k$$th term of $$g(x)$$ is $$t_{i, k}$$. Since we separated our exponential bases in the individual general terms, it was easy to combine bases in the product. 

We are now well equipped to answer the following questions:
- What are all terms containing $$x^{20}$$ in the expansion of $$f(x, y) \cdot g(x,y)$$?
- What is the coefficient of $$x^{12}y^{10}$$ in the expansion of $$f(x, y) \cdot g(x, y)$$?

We will walk through the solution of the first problem as an example, while the latter is left as an exercise.

<br>

#### Problem Setup

Using $$f(x, y)$$ and $$g(x, y)$$ as before, we want to find all terms containing $$x^{20}$$. Our analysis will be similar to what it was when we looked at the expansion of trinomials. Since the exponent on $$x$$ is $$32 - i - 2k$$, we are looking for all integer solutions to the following problem:

<div align=center>

$$32 - i - 2k = 20$$
<br>
$$\text{s.t. } 0 \leq i \leq 5, 0 \leq k \leq 9$$

</div>

(Note: "s.t." means "such that".)

We know that the first line reduces to $$i + 2k = 12$$. One way to determine these solutions assuming the equation only contains two variables is to find the simplest solution that minimizes one variable and maximizes the other – such as $$i = 0, k = 6$$ – and iteratively increase the minimum and decrease the maximum until all solutions are found.

After finding $$i = 0, k = 6$$, we can reduce $$k$$ by $$1$$ to find $$i = 2, k = 5$$. Doing so again yields $$i = 4, k = 4$$ which we know is the last solution as setting $$k = 3$$ yields $$i = 6$$ which is out of the range of possible values for $$i$$.

Now that we have our three solutions, our problem reduces to plugging in the values of $$i$$ and $$k$$ into our expanded term. 

<div align = center>

$$t_{0, 6} = (-1)^{0 + 6} {5 \choose 0}{9 \choose 6} 2^{5-0} 3^{0 + 6} x^{32 - 0 - 2 \cdot 6} y^{0 + 2 \cdot 6} = 1959552x^{20}y^{12}$$
<br><br>
$$t_{2, 5} = (-1)^{2 + 5} {5 \choose 2}{9 \choose 5} 2^{5-2} 3^{2+5}x^{32 - 2 - 2 \cdot 5}y^{2 + 2 \cdot 5} = -22044960x^{20}y^{12}$$
<br><br>
$$t_{4, 4} = (-1)^{4 + 4} {5 \choose 4}{9 \choose 4} 2^{5-4} 3^{4+4} x^{32 - 4 - 2 \cdot 4} y^{4 + 2 \cdot 4} = 8266860x^{20}y^{12}$$

</div>

It should also be noted that the multiplication of these large numbers isn't exactly a skill that one needs to develop to be successful; no reasonable assessment (at least in this course) will ask for you to do this by hand, and leaving terms in the form $${5 \choose 2}{9 \choose 5}2^3 3^7 x^{20} y^{12}$$ is perfectly fine.

<br>





