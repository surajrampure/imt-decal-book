# Extensions of the Binomial Theorem

We will now look at a few extensions of the binomial theorem and the thought process we used in deriving it.

<br>

## The "Trinomial" Theorem?

What if we would like to expand something of the form $$(x + y + z)^n$$? One option is to treat either $$x + y$$ or $$y + z$$ as a single term, and use the binomial theorem. However, once again, we can treat this as a combinatorial problem on its own.

Suppose a general term in the expansion of $$(x + y + z)^n$$ contains $$a$$ $$x$$s, $$b$$ $$y$$s and $$c$$ $$z$$s. Then, we must have that $$a + b + c = n$$, since the total number of parentheses we choose from in the expansion must be exactly $$n$$. We can then say the following:

$$
t_{a, b, c} = \frac{n!}{a! b! c!} x^a y^b z^c
$$

The coefficient $$\frac{n!}{a!b!c!}$$ comes from the number of ways to arrange $$a$$ $$x$$s, $$b$$ $$y$$s and $$c$$ $$z$$s (think back to counting the number of permutations of MISSISSIPPI).

### Example
Let's calculate the coefficient of the term containing $$x^4$$ in the expansion of $$(x - 3x^{-2} + 4)^8$$:

$$t_{a, b, c} = \frac{8!}{a! b! c!} x^a (-3x^{-2})^b (4)^c$$
$$= (-1)^b \frac{8!}{a!b!c!}3^b4^c x^{a-2b}$$

Setting $$x^{a - 2b} = x^4$$, we require $$a - 2b = 4$$, with the constraints that $$0 \leq a, b, c \leq 8$$ and $$a + b + c = 8$$. If we set $$a = 4$$ and $$b = 0$$, we satisfy the given constraints. We can use this solution as a starting point to find the remaining solutions:

-   $$a = 4, b = 0, c = 4$$

-   $$a = 6, b = 1, c = 1$$

We then find the general terms corresponding to each of these two triplets:

$$t_{4, 0, 4} = (-1)^0 \frac{8!}{4!0!4!} 3^0 4^4 x^4 = 17920x^4$$
$$t_{6, 1, 1} = (-1)^1 \frac{8!}{6!1!1!}3^14^1x^4 = - 336x^4$$

Then, in the final expansion, the term containing $$x^4$$ is $$t_{4, 0, 4} + t_{6, 1,1} = 17920x^4 - 336x^4 = 17584x^4$$, and the coefficient of $$x^4$$ is $$17584$$.

### Generalization

Note that can write the expansion of a trinomial raised to an exponent
as a sum, though it is slightly less meaningful:

$$
(x + y + z)^n = \sum_{a, b, c | a + b + c = n} \frac{n!}{a!b!c!}x^ay^bz^c
$$

<br>

## The Multinomial Theorem

We can generalize this even further. Let's introduce the **multinomial coefficient**:

$$
{n \choose k_1, k_2, ... k_m} = \frac{n!}{k_1!k_2! ... k_m!}
$$ 

Under the assumption $$k_1 + k_2 + ... + k_m = n$$, this term is the number of ways to select one subset of size $$k_1$$, one subset of size $$k_2$$, ... and one subset of size $$k_m$$ from a group of $$n$$ items. Notice that with $$m = 2$$, this is the same as the binomial coefficient that we're used to.

Then: 

$$
(x_1 + x_2 + ... + x_m)^n = \sum_{k_1 + k_2 + ... + k_m = n} {n \choose k_1, k_2, ... k_m} \prod_{i = 1}^m x_i^{k_i}
$$

**Question**: How many terms are in the initial sum? 
This corresponds to the number of non-negative integer solutions to $$k_1 + k_2 + ... + k_m = n$$, which is a stars-and-bars counting problem! Here we have $$n$$ stars and $$m$$ bins, meaning $$m-1$$ bars, meaning we have $${n + m - 1 \choose m-1}$$ unique terms in the first expansion. (Some combinations of terms may end up being the same when $$x_i$$, $$x_j$$ contain common variables). 

<br>

## Product of Two Binomial Expansions

Let's switch gears. Rather than expanding from binomials to trinomials or general multinomials, what if we instead take a look at the product of two binomials, each raised to different exponents? Let's illustrate this with an example!

Let $$f(x, y) = (2x - 3y)^5$$ and $$g(x, y) = (x^3 - 3xy^2)^9$$. Our goal will be to find the general term of the product $$f(x, y) \cdot g(x, y)$$, and determine the existence of certain terms.

First, we find the general term of each, using the index variable $$i$$ for $$f(x, y)$$ and $$k$$ for $$g(x, y)$$ (these choices are arbitrary, but we need some way of differentiating the two, as you will see). You should verify these on your own:

$$
t_i = (-1)^i {5 \choose i} 2^{5-i} 3^i x^{5-i} y^i \\
t_k = (-1)^k {9 \choose k} 3^k x^{27-2k} y^{2k}
$$

Now, to find the general term of the product, we take the product of the two general terms:

$$
t_{i, k} = (-1)^i {5 \choose i} 2^{5-i} 3^i x^{5-i} y^i (-1)^k {9 \choose k} 3^k x^{27-2k} y^{2k}
\\ =(-1)^{i+k} {5 \choose i} {9 \choose k} 2^{5-i} 3^{i+k} x^{32 - i - 2k} y^{i+2k}
$$

This tells us that the product of the $$i$$th term of $$f(x)$$ and $$k$$th term of $$g(x)$$ is $$t_{i, k}$$. Since we separated our exponential bases in the individual general terms, it was easy to combine bases in the product. 

We are now well equipped to answer the following questions:
- What are all terms containing $$x^{20}$$ in the expansion of $$f(x, y) \cdot g(x,y)$$?
- What is the coefficient of $$x^{12}y^{10}$$ in the expansion of $$f(x, y) \cdot g(x, y)$$?

We will walk through the solution of the first problem as an example, while the latter is left as an exercise.

<br>

### Problem Setup

Using $$f(x, y)$$ and $$g(x, y)$$ as before, we want to find all terms containing $$x^{20}$$. Our analysis will be similar to what it was when we looked at the expansion of trinomials. Since the exponent on $$x$$ is $$32 - i - 2k$$, we are looking for all integer solutions to the following problem:

$$
32 - i - 2k = 20, 
\:0 \leq i \leq 5, 0 \leq k \leq 9
$$
We know that the first line reduces to $$i + 2k = 12$$. One way to determine these solutions assuming the equation only contains two variables is to find the simplest solution that minimizes one variable and maximizes the other – such as $$i = 0, k = 6$$ – and iteratively increase the minimum and decrease the maximum until all solutions are found.

After finding $$i = 0, k = 6$$, we can reduce $$k$$ by $$1$$ to find $$i = 2, k = 5$$. Doing so again yields $$i = 4, k = 4$$ which we know is the last solution as setting $$k = 3$$ yields $$i = 6$$ which is out of the range of possible values for $$i$$.

Now that we have our three solutions, our problem reduces to plugging in the values of $$i$$ and $$k$$ into our expanded term. 

- $$t_{0, 6} = (-1)^{0 + 6} {5 \choose 0}{9 \choose 6} 2^{5-0} 3^{0 + 6} x^{32 - 0 - 2 * 6} y^{0 + 2*6} = 1959552x^{12}y^{12}$$
- $$t_{2, 5} = (-1)^{2 + 5} {5 \choose 2}{9 \choose 5} 2^{5-2} 3^{2+5}x^{32 - 2 - 2*5}y^{2 + 2*5} = -22044960x^{12}y^{12}$$
- $$t_{4, 4} = (-1)^{4 + 4} {5 \choose 4}{9 \choose 4} 2^{5-4} 3^{4+4} x^{32 - 4 - 2*4} y^{4 + 2*4} = 8266860x^{12}y^{12}$$

In this example, it turned out that the exponent on $$x$$ exactly matched the exponent on $$y$$ – this was simply a coincidence, and plugging in arbitrary values of $$I$$ and $$k$$ into the general term shows that this result isn't always the case.

It should also be noted that the multiplication of these large numbers isn't exactly a skill that one needs to develop to be successful; no reasonable assessment (at least in this course) will ask for you to do this by hand, and leaving terms in the form $${5 \choose 2}{9 \choose 5}2^3 3^7 x^{12} y^{12}$$ is perfectly fine.