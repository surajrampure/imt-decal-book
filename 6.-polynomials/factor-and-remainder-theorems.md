# Factor and Remainder Theorems

Before we can look at and explain the existence of complex roots, there are two fundamental theorems that we need to discuss.

## Factor Theorem

The factor theorem states that **for all polynomials , if  is a root of , meaning that , then  is a factor of .**

As an example, since we can factor  into , we know that .

\vspace{.1in} Let's continue.

The other key property of polynomials determined by their degree are their number of roots. You may have learned before that a real-valued polynomial with real coefficients of degree $n$ has anywhere between $0$ and $n$ roots, depending on its specifics. However, we can actually make a stronger claim.

\vspace{.1in} **All real-valued polynomials with real coefficients of degree $n$ have exactly $n$ roots, with some possibly complex roots.**

\vspace{.1in} Let's disect this. The first class of polynomial we encounter with varying numbers of roots is the parabola, of degree $2$. You may have studied before that parabolas have one of the following:

* $2$ roots, meaning they intercept the $x$ axis twice
* $1$ root, meaning they sit on the $x$ axis \(this is actually known as a double root\)
* $0$ roots, meaning that they sit completely above or completely below the $x$ axis

Recall, given a quadratic of the form $f\(x\) = ax^2 + bx + c$, the solutions to $f\(x\) = 0$ are given by 

The three cases above come from the three different states of the discriminant, $b^2 - 4ac$. When $b^2 - 4ac &gt; 0$, there are two distinct roots. When $b^2 - 4ac = 0$, the \"plus-or-minus\" term vanishes, leaving a double root at $x = -\frac{b}{2a}$. The case we're now interested in is when $b^2 - 4ac &lt; 0$, where we would previously claim there to be \"no solution\" since we cannot take the square root of a negative number. In fact, there are still two perfectly valid solutions ---- they're just not real numbers.

\vspace{.1in} **Complex Numbers**

Complex numbers, as discussed earlier in the course, are a superset of the real numbers. We can represent a complex number $z$ in **rectangular form** as $z = a + bi$, where $a, b$ are real numbers and $i$ is the imaginary unit defined by $i^2 = -1$. We say $a$ is the \"real part\" and $bi$ is the \"imaginary part.\" We can represent the set of real numbers as complex numbers, with $b = 0$.

\vspace{.1in} The simplest parabola that has complex roots is $p\(x\) = x^2 + 1$, which sits one unit above the $x$ axis, centered on the $y$ axis. It has roots $x\_1 = i$ and $x\_2 = -i$, respectively, which you can verify with the quadratic equation.

\vspace{.1in} An important consequence of our new, stronger definition of the number of roots of a polynomial is that **all polynomials are now completely factorable into linear terms**, whereas previously this was not the case. Previously, we could factor $x^2 + 5x + 6$ and $x^2 - 16$ into $\(x+2\)\(x+3\)$ and $\(x-4\)\(x+4\)$, respectively, because we knew these polynomials in standard form had roots. However, now we can factor $x^2 + 1$ as well, into $\(x-i\)\(x+i\)$, by the factor theorem. In general,

for some real constant $a$. Remember, our polynomials still only take and return real numbers as inputs and outputs, and all coefficients are still real numbers. It's just the roots that are potentially complex.

\vspace{.1in} **Complex Root Pairs**

As it turns out, complex roots always occur in pairs. No real polynomial can have only a single complex root, or three complex roots, or any odd number of complex roots. Furthermore:

This says that if a complex number is a root of a real polynomial, its **complex conjugate** must also be a root. Conjugates are defined exactly as above -- the conjugate of $z = a + bi$ is $\bar{z} = a - bi$. Complex conjugates are defined this way for the following reason:

When multiplying a complex number by its conjugate, the imaginary parts fall out and we're left with a real number. In particular, this real number $z\bar{z} = \|z\|^2$ is the **square of the magnitude** of the complex number, i.e. the squared distance from $0$.

\vspace{.1in} Let's justify why $a + bi$ and $a - bi$ will always exist together as roots. By the factor theorem, if they are both roots of some $p\(x\)$ of degree $n$:   

The product $\(x - \(a + bi\)\)\(x - \(a - bi\)\)$ yields a completely real polynomial. This real polynomial, multiplied by the rest of $\(x - r_1\)\(x - r\_2\)...\(x-r_{n-2}\)$, which is assumed to be real, will result in a real $p\(x\)$. However, if $\(x - \(a + bi\)\)$ were multipled by $\(x - \(c + di\)\)$, for some general complex number $c + di$, the resulting last term of $p\(x\)$ would contain complex terms, meaning that $p\(x\)$ would have complex coefficients, going against our definition set in the beginning.

