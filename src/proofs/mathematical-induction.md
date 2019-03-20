<title>Mathematical Induction – IMT DeCal</title>

# Mathematical Induction
---

<br>

<!--

Jump to:
* [Motivation](#motivation)
* [Formalization](#formalization)
* [More Examples](#examples)
	* [Divisibility](#divisibility)
	* [Fibonacci](#fibonacci)
	* [De Moivre's Theorem](#de_moivre)
	* [Airports](#airports)

<br>

-->

<a name='motivation'>

## Motivation
---

</a>

Mathematical induction, the last proof technique we will look at, has many parallels to recursion. As an introduction, consider the following situation:

Suppose you're sitting in a massive lecture hall, and want to find out how many rows you're sitting from the front of the room. You _could_ sit there and count, but consider this basic principle:
- The person sitting in the first row knows their row number _by default_: they're in the first row!
- If one knows the row number of the person in front of them, they add 1 to get their own row number

With this principle, the first person can pass their row number to the second person, who "calculates" their row number (by adding 1) and passes it to the third person, and so on and so fourth. This is exactly how induction (and recursion, to an extent) works. 

With induction, we want to prove some property about **all natural numbers** or whole numbers (it doesn't matter if we start with 0 or 1, as you will see). 

<br>

<a name='formalization'>

## Formalization
---

</a>

Suppose the expression we want to prove is in terms of the variable $$n$$ (which is typically used for natural numbers). We follow the following three steps, in every single induction proof: 

1. **Base Case**: Establish that the statement holds for some base case. Often, this is $$n = 0$$ or $$n = 1$$, but an alternate base case may be specified in the proposition.
2. **Induction Hypothesis**: Assume that the statement holds true for $$n = k$$, for some arbitrary $$k$$.
3. **Induction Step**: Given the fact that the statement holds true for $$n = k$$, show that it holds for $$n = k + 1$$.

Let's dive right into an example. _Note: If you're uncomfortable with summation notation, refer to the note on **[Sigma and Pi Notation](../appendix/sigma-and-pi-notation.html)**._

#### Example: Sum of First $n$ Naturals

Sure, we could technically use induction to prove that $$(x + 1)^2 = x^2 + 2x + 1$$ for all natural numbers, but induction is overkill in such an example. A common example of something we may prove with induction is the following fact: 

<div align=center>

$$\sum_{i = 1}^n i = \frac{n(n+1)}{2}, \forall n \in \mathbb{N}$$

</div>

**Base Case**: $$n = 1$$ <br>
LHS: $$\sum_{i = 1}^1 i = 1$$, RHS: $$\frac{1(2)}{2} = 1$$

LHS = RHS, therefore the base case holds.

**Induction Hypothesis** <br>
Assume that $$\sum_{i = 1}^k i = \frac{k(k+1)}{2}$$, for some arbitrary integer $$k$$.

**Induction Step** <br>
Now, we need to show that $$\sum_{i = 1}^{k+1} i = \frac{(k+1)(k+2)}{2}$$, somehow using the information in the induction hypothesis.


$$\begin{aligned} \sum_{i = 1}^{k + 1} i &= \sum_{i = 1}^k i + (k + 1) \\\ &= \frac{k(k+1)}{2} + \frac{2(k+1)}{2} \\\ &= \frac{(k+1)(k+2)}{2} \end{aligned}$$

By assuming that the statement held true for $$n = k$$, we were able to come to the conclusion that the statement holds true for $$n = k + 1$$. Therefore, induction holds, and the statement holds true for all natural numbers. 

Note, we chose $$n = 1$$ to be the base case, as it wouldn't make sense to take a sum with lower limit 1 and upper limit 0.

_We will look at an alternate proof of this statement when we get to Series and Sequences. We will also provide another proof when we look at combinatorics. **This is an identity that you will be expected to know.**_

<br>

Let's introduce a more concise notation for writing out the steps of induction. Suppose that $$P(i)$$ represents the proposition we are trying to prove holds true for the value $$n = i$$. Then, we have:

- **Base Case**: Show $$P(0)$$ or $$P(1)$$ (or whatever other appropriate value)
- **Induction Hypothesis**: Assume $$P(k)$$
- **Induction Step**: Show $$P(k) \implies P(k+1)$$

Essentially, what we have is a domino effect.

<div align=center>

$$P(1) \implies P(2) \implies P(3) \implies ... \implies P(k) \implies ...$$

</div>

<br>

A few things to note:
- The majority of the work in an induction proof is in the induction step. Proving the base case is usually trivial, and in the induction hypothesis you simply state your assumption.
- The example we gave is relatively straight forward. Most of the time, you'll have to do slightly more work in order to show the implication $$P(k) \implies P(k+1)$$.

<br>

<a name='examples'>

## More Examples
---

</a>

In order to reinforce the concept of induction, we present a few examples below. **A good way to practice 
would be to attempt each problem on your own, and then compare your proof with the solution.**

<br>

<a name = 'divisibility'>

### Example: Divisibility
---

</a>

**Prove $$3 | n^3 - n$$, $$\forall n \in \mathbb{N}_0$$.**

_Note: We actually proved this proposition directly, as an example when introducing direct proofs._

**Base Case:** $$n = 0$$ <br>
3 does indeed divide 0, as we can find some integer $j$ such that $$0 = 3j$$ (namely, $$j = 0$$).

**Induction Hypothesis** <br>
Assume that $3 | k^3 - k$ for some arbitrary integer $k$.

**Induction Step** <br>
We now want to show that $$3 | [(k+1)^3 - (k+1)]$$, i.e. that we can write $$(k+1)^3 - (k+1)$$ as $$3 \cdot (\text{some integer})$$.

We know that we can write $$k^3 - k = 3j$$, for some integer $j$, from the induction hypothesis. Then:

<div align=center>

$$ \begin{align*} (k+1)^3 - (k+1) &= k^3 + 3k^2 + 3k + 1 - k - 1 \\\ &= k^3 - k + 3k^2 + 3k \\\ &= 3j + 3(k^2 + k) \\\ &= 3(j + k^2 + k) \end{align*} $$

</div>

Therefore, by induction, the statement holds true. 

<br>

<a name='fibonacci'>

### Example: Fibonacci
---

</a>

The Fibonacci sequence $$1, 1, 2, 3, 5, 8, 13, 21, 34, ...$$ is defined by the recurrence relation

<div align=center>

$$\begin{align*} F_1 = 1, F_2 = 1 \\\ F_n = F_{n-2} + F_{n-1} \end{align*}$$

</div>

**Prove that $$F_1 + F_2 + ... + F_n = F_{n + 2} - 1$$.**

**Base Case**: $$n = 1$$ <br>
$$F_1 = 1,  F_3 - 1 = 2 - 1 = 1$$, therefore the base case holds. 

**Induction Hypothesis** <br>
Assume $$F_1 + ... + F_k = F_{k + 2} - 1$$, for some arbitrary natural number $$k$$.

**Induction Step** <br>

$$\begin{aligned} F_1 + ... + F_{k + 1} &= (F_1 + ... + F_k) + F_{k + 1} \\\ &= F_{k+2} - 1 + F_{k+1} \\\ &= F_{k + 3} - 1 \end{aligned}$$

Therefore, induction holds, and the statement is true. 

<br>

<a name='de_moivre'>

### Example: De Moivre's Theorem
---

</a>

De Moivre's theorem gives us a way to exponentiate complex numbers of the form $$R(\cos t + i \sin t)$$:

<div align=center>

$$(R(\cos t + i \sin t))^n = R^n(\cos nt + i \sin nt)$$

</div>

**Prove De Moivre's theorem for $n \in \mathbb{N}_0$, using induction**. _We will need to use the sum identities for $$\sin(a + b)$$ and $$\cos(a + b)$$, that is, $$\sin(a + b) = \sin a \cos b + \cos a \sin b$$ and $$\cos(a + b) = \cos a \cos b - \sin a \sin b$$._

**Base Case**: $$n = 0$$ <br>
LHS: $$(R(\cos t + i \sin t))^0 = 1$$
RHS: $$R^0 (\cos 0t + i \sin 0t) = 1 (1 + 0) = 1$$

LHS = RHS, thus the base case holds.

**Induction Hypothesis**:  $$n = k$$ <br>
Assume $$(R(\cos t + i \sin t))^k = R^k(\cos kt + i \sin kt)$$, for some arbitrary $$k \in \mathbb{N}$$.

**Induction Step** <br> 
Now, we need to show $(R(\cos t + i \sin t))^{k+1} = R^{k+1}(\cos (k+1)t + i \sin (k+1)t)$, using the information we assumed in the hypothesis.

<div align=center>

$$\begin{align*} (R(\cos t + i \sin t))^{k+1} &= (R(\cos t + i \sin t))^k (R(\cos t + i \sin t)) \\\ &= R^k(\cos kt + i \sin kt) R (\cos t + i \sin t) \\\ &= R^{k + 1} (\cos kt \cos t + i \cos kt \sin t + i \sin kt \cos t + i^2 \sin kt \sin t) \\\ &= R^{k+1} (\cos kt \cos t - \sin kt \sin t + i (\cos kt \sin t + \sin kt \cos t))\end{align*}$$

</div>

Now, we'll need the identities given in the hint:

<div align=center>

$$\begin{align*}\cos kt \cos t - \sin kt \sin t &= \cos (kt + t) = \cos(k+1)t \\\ \cos kt \sin t + \sin kt \cos t &= \sin (kt + t) = \sin(k+1)t \end{align*}$$ 

</div>

Then:

<div align=center>

$$R^{k+1} (\cos kt \cos t - \sin kt \sin t + i (\cos kt \sin t + \sin kt \cos t)) = R^{k+1} (\cos(k+1)t + i \sin(k+1)t)$$

</div>

as required. Therefore, induction holds, and the statement holds true.

_Note: It is significantly easier to prove this statement using Euler's Identity and complex exponentials, but it's interesting to see that we're able to do this proof using induction as well._

<br>

<a name='airports'>

### Example: Airports
---

</a>

This example will illustrate the fact that not all induction proofs need be algebraic.

Suppose that there are $2n+1$ airports where $n$ is a positive integer. The distances between any two airports are all different. For each airport, there is exactly one airplane departing from it, and heading towards the closest airport. **Prove by induction that there is an airport which none of the airplanes are heading towards.**

**Base Case** <br>
$$n = 1$$: If there are 3 airports, the closest pair of airports will exchange planes. The third airport will then send a plane to one of the first two, meaning this third airport will have no incoming planes.

**Induction Hypothesis** <br>
Assume for some $k$, in $2k+1$ airports one airport has no incoming planes. 

**Induction Step** <br>
For $2(k+1) + 1 = 2k + 3$ airports, consider the two airports that are closest to one another.
This is necessarily unique, given the problem statement. These airports will exchange planes, thus reducing the problem to $2k + 1$ airports. We know the $2k+1$ case holds from the induction hypothesis.

QED.

<br>



