# Vieta's Formulas

Vieta's formulas give us a way to interpret a polynomial in standard form, e.g. $$p(x) = 4x^2 + 3x + 3$$, in terms of its roots, without having to find the roots specifically. While there are more practical applications to this, the derivation of Vieta's formulas prove to be an interesting combinatoral problem.

<br>

## Vieta's Formulas for a Polynomial of Degree 2

**Given a polynomial of the form $$p(x) = ax^2 + bx + c$$, the sum of the roots of $$p(x)$$ is $$-\frac{b}{a}$$ and the product of the roots of $$p(x)$$ is $$\frac{c}{a}$$.**

<br>

Let's derive this! Let $$p(x)$$ be some parabola with roots $$r_1, r_2$$. By the factor theorem, we know that $$p(x) = a(x - r_1)(x - r_2)$$, for some constant $$a$$. Expanding $$p(x)$$:


$$\begin{aligned}
p(x) &= a(x - r_1)(x-r_2)\\
&= a[x^2 - (r_1 + r_2)x + r_1r_2 ] \\
&= ax^2 - a(r_1 + r_2)x + ar_1r_2
\end{aligned}$$


Comparing this expansion with $$ax^2 + bx + c$$, we see:

$$-a(r_1 + r_2) = b \implies r_1 + r_2 = -\frac{b}{a}$$

$$ar_1r_2 = c \implies r_1r_2 = \frac{c}{a}$$


We will follow a similar process to derive Vieta's formulas for degree 3. However, at this point, you should try and derive these on your own, then come back here to check your work.

<br>

## Vieta's Formulas for Polynomials of Degrees 3, 4
Assume $$p(x)$$ has roots $$r_1, r_2, r_3$$, and has the form $$p(x) = ax^3 + bx^2 + cx + d$$. Then:

$$
\begin{aligned}
p(x) &= a(x-r_1)(x-r_2)(x-r_3) \\

&= a \left[(x^3 - (r_1 + r_2 + r_3)x + (r_1r_2 + r_1r_3 + r_2r_3)x - r_1r_2r_3\right] \\

&= ax^3 - a(r_1 + r_2 + r_3)x^2 + a(r_1r_2 + r_1r_3 + r_2r_3)x - ar_1r_2r_3 \\

\end{aligned}
$$

$$\implies r_1 + r_2 + r_3 = -\frac{b}{a}$$

$$\implies r_1r_2 + r_1r_3 + r_2r_3 = \frac{c}{a}$$

$$\implies r_1r_2r_3 = -\frac{d}{a}$$

<br>

We could follow the same process to find the formulas for degrees 4, 5 and so on and so forth. However, there's a pattern here. When multiplying out $$(x - r_1)(x - r_2)(x - r_3)$$, we know our product must contain every combination of one term from the first bracket, one term from the second bracket and one term from the third bracket. Then, our choices are the following:

*   We can choose $$3$$ $$x$$s and no roots, yielding $$x^3$$

*   We can choose $$2$$ $$x$$s and one root, yielding
    $$(-r_1 - r_2 - r_3)x^2 = -(r_1+r_2+r_3)x^2$$

*   We can choose $$1$$ $$x$$ and two roots, yielding
    $$((-r_1) \cdot (-r_2) + (-r_1) \cdot (-r_3) + (-r_2) \cdot (-r_3))x = (r_1r_2 + r_1r_3 + r_2r_3)x$$

*   We can choose no $$x$$s and three roots, yielding
    $$((-r_1) \cdot (-r_2) \cdot (-r_3)) = -r_1r_2r_3$$

<br>

Each successive term is a **sum of products of roots, taken in different quantities at a time**. $$r_1 + r_2 + r_3$$ is the sum of the products of the roots, taken one at a time, since multiplying a constant by nothing is the constant itself. $$r_1r_2 + r_1r_3 + r_2r_3$$ is the sum of the product of the roots, taken two at a time – it features all 3 possible combinations of two different roots multiplied together. $$r_1r_2r_3$$ is the sum of the product of the roots, taken three at a time – there is only one way to take three items at once, and this is that one way.

Following this pattern, we can find the expansion (and Vieta's) for a degree 4 polynomial without having to do any manual expanding. Let $$p(x)$$ have roots $$r_1, r_2, r_3, r_4$$. Then, if we let $$p(x) = ax^4 + bx^3 + cx^2 + dx + e$$ we have:

$$
\begin{aligned}

r_1 + r_2 + r_3 + r_4 &= -\frac{b}{a} \\
r_1r_2 + r_1r_3 + r_1r_4 + r_2r_3 + r_2r_4 + r_3r_4 &= \frac{c}{a} \\
r_1r_2r_3 + r_1r_2r_4 + r_1r_3r_4 + r_2r_3r_4 &= -\frac{d}{a} \\
r_1r_2r_3r_4 &= \frac{e}{a}

\end{aligned}
$$


One thing to notice is that 1 term makes up the coefficient of $$x^4$$, 4 terms make up the coefficient of $$x^3$$, 6 terms make up the coefficient of $$x^2$$, 4 terms make up the coefficient of $$x$$ and 1 term makes up the coefficient of $$1$$. These numbers – 1, 4, 6, 4, 1 – are of course the 4th row of **Pascal's triangle**! This makes sense, as the coefficient of $$x^3$$ consists of the roots taken one at a time, which means there should be $${4 \choose 1} = 4$$ terms. The coefficient of $$x^2$$ consists of the roots taken two at a time, which means there should be $${4 \choose 2} = 6$$ terms.

Of course, since this is a pattern, we can generalize it to polynomials of an arbitrary degree.

<br>

## Generalized Derivation of Vieta's Formulas 


$$p(x) = \sum_{k = 0}^n a_k x^k = \sum_{k = 0}^n (-1)^{n-k} \big(\text{sum of the products of the roots of } p(x) \text{, taken } n-k \text{ at a time}  \big)x^k$$

<br>

What we did here was powerful. We took a pattern for a small $$n$$, extended it to a slightly larger $$n$$, and then generalized it for all $$n$$. We will follow a similar process in the next section, with the binomial theorem.