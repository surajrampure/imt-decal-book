<title>Key Examples in Counting – IMT DeCal</title>

# Key Examples in Counting

_by Suraj Rampure_<br>
_Last modified: March 28, 2019_

---

<br>

This note walks through a few selected examples of interesting problems in combinatorics. It also touches on the idea of combinatorial proofs.


## 1. Number of Factors 

### How many factors does $$1200$$ have? <br>

We <i>could</i> sit down and manually enumerate through all factors of 1200, one by one - 1, 2, 3, 4, 5, 6, ... but that would take quite a bit of time. Instead, we will look at the prime factorization of 1200: $$1200 = 2^4 \cdot 3 \cdot 5^2$$.

We know each factor of 1200 will have some number of $2$s, some number of $3$s, and some number of $5$s. There are 5 options for the number of $2$s a factor could have: 0, 1, 2, 3 or 4 (meaning a factor of 1200 could either have a factor of $2^0$, or $2^1$, or $2^2$, or $2^3$, or $2^4$). Similarly, there are 2 options for the number of $3$s a factor could have (either 0 or 1) and 3 options for the number of $5$s (0, 1, or 2). 

In other words, each factor will look like $$2^a \cdot 3^b \cdot 5^c$$, where $$0 \leq a \leq 4$$, $$0 \leq b \leq 1$$ and $$0 \leq c \leq 2$$.

Since we're making three successive choices, we take the product of the number of choices at each step, yielding

<div align=center> $$\text{number of factors of } 1200 = (4 + 1) (1 + 1) (2 + 1) = 30$$</div><br>

In general, if we have $$n = p_1^{e_1} \cdot p_2^{e_2} \cdot ... \cdot p_k^{e_k}$$, the following holds:

<div align=center> $$\boxed{\text{number of factors of } n = \prod_{i = 1}^k (e_i + 1) = (e_1 + 1) \cdot (e_2 + 1) \cdot ... \cdot (e_{k - 1} + 1) \cdot (e_k + 1)} $$</div><br>

We can also extend this problem.

### How many factors does 1200 have, that are multiples of 24? <br>

We know each factor of 1200 will be of the form $$2^a \cdot 3^b \cdot 5^c$$. We now just need to determine the number of options we have for $$a, b$$ and $$c$$. Since $24 = 2^3 \cdot 3^1 \cdot 5^0$, we know that $a$ must be at least $3$ and $b$ must be at least $1$.

This restricts our set of choices: now, we have $$3 \leq a \leq 4, 1 \leq b \leq 1$$ and $$0 \leq c \leq 2$$. This means we have 2 choices for $a$ (3, 4), 1 choice for $b$ (1) and 3 for $c$ (0, 1, 2), yielding $2 \cdot 1 \cdot 3 = 6$ factors of 1200 that are multiples of 24.

<br>

## 2. Cardinality of the Power Set, Combinatorial Proofs

The power set $$P(S)$$ of a set $$S$$ is a set of all possible subsets of $$S$$. For example, if $$S = \{1, 2, 3}$$, we have $$P(S) = \\{ \emptyset , \\{1\\}, \\{2\\}, \\{3\\}, \\{1, 2\\}, \\{1, 3\\}, \\{2, 3\\}, \\{1, 2, 3\\} \\}$$.

### If $$S$$ is a set such that $$|S| = n$$, what is $$|P(S)|$$? <br>

When creating a subset of $$S$$, for each of the $$n$$ items in $$S$$, we have two options: either we include it in the subset, or do not include it in the subset. Since we have two options for each of the $$n$$ items, the total number of ways we can create a subset of $$S$$ is $$2 \cdot 2 \cdot ... \cdot 2 = 2^n$$. Therefore,

<div align=center>

$$\boxed{|S| = n \implies |P(S)| = 2^n}$$

</div>

It should be noted, however, that we can arrive at this result another way. Instead of looking at each element individually, and saying that for each element we have 2 options (include or exclude), we can look at all possible subsets. Let's consider the example, $$S = \\{\text{dog}, \text{cat}, \text{zebra} \\}$$. Then, any subset will have size 0, 1, 2, or 3.

- There is $${3 \choose 0} = 1$$ subset of size 0 - the empty set $\emptyset$
- There are $${3 \choose 1} = 3$$ subsets of size 1 - $\\{\text{dog}\\}$, $\\{\text{cat}\\}$, $\\{\text{zebra}\\}$
- There are $${3 \choose 2} = 3$$ subsets of size 2 - $\\{\text{dog}, \text{cat}\\}$, $\\{\text{dog}, \text{zebra}\\}$, $\\{\text{cat}, \text{zebra}\\}$
- There is $${3 \choose 3} = 1$$ subset of size 3 - $\\{\text{dog}, \text{cat}, \text{zebra}\\}$

Thus, the total number of subsets of $$\{1, 2, 3}$$ is $${3 \choose 0} + {3 \choose 1} + {3 \choose 2} + {3 \choose 3}$$. However, using the relationship derived above, we have that there are $$2^3$$ subsets of size 3. This implies

<div align=center>

$${3 \choose 0} + {3 \choose 1} + {3 \choose 2} + {3 \choose 3} = 2^3$$

</div>

This is not a co-incidence, and in fact, it holds in general (for $n \in \mathbb{N}$):

<div align=center>

$$\boxed{\sum_{i = 1}^n {n \choose i} = {n \choose 0} + {n \choose 1} + ... + {n \choose n} = 2^n}$$

</div>

To prove this more general statement, we can essentially repeat the argument we made for the $n = 3$ case, but for any $n$. Our argument is that both sides of the equals sign count the same quantity.

- The left hand side (LHS) counts the number of subsets of a set of size $n$ by finding the number of subsets of each size $k$, where $0 \leq k \leq n$, and then adding them together, yielding ${n \choose 0} + {n \choose 1} + ... + {n \choose n}$
- The RHS reasons that for each of the $n$ elements, there are two choices when creating a subset – include or exclude – and thus there are $2^n$ subsets

Such an argument is known as a **combinatorial proof**, one where we reason that two expressions count the same quantity, and thus must be equal.

<br>

### How many sets are subsets of $$S_1 = \\{A, B, C, D, E\\}$$ or $$S_2 = \\{D, E, F, G\\}$$?

To attack this, we need the Principle of Inclusion-Exclusion. First, we can find the number subsets of $S_1$ and $S_2$ individually, and also the number of subsets of both. 

<div align=center>

$$\text{# subsets of }S_1 \text{ or } S_2 = (\text{# subsets of } S_1) + (\text{# subsets of } S_2) - (\text{# subsets of both})$$

</div>

There are $2^5$ subsets of $S_1$, and $2^4$ subsets of $S_2$. For a set to be a subset of both, it must be a subset of their intersection, $\\{D, E\\}$ – this set only has $2^2$ subsets. Then, the total number of subsets we are looking for is $2^5 + 2^4 - 2^2 = 44$.
