# The Five Proofs

We will now look at five proofs of the same result – that the sum of the first $$n$$ natural numbers is $$\frac{n(n+1)}{2}$$. It turns out that we've actually already seen many of these, but this serves as a consolidation.

<br>

## 1: Arithmetic Sum Formulation

The first proof is one we used when deriving the formula of the sum of a general arithmetic series. Once again, let $$S$$ represent the value of the summation.

$$
S = 1 + 2 + 3 + ... + (n-2) + (n-1) + n
$$

We can rewrite $$S$$ backwards:

$$
S = 1 + 2 + 3 + ... + (n-2) + (n-1) + n \\
S = n + (n-1) + (n-2) + ... + 3 + 2 + 1
$$

Notice that the first term in the top line and first term in the bottom line add to $$n+1$$, as do the second terms, third terms, and so on and so forth. 

$$
2S = (n+1) + (n+1) + (n+1) + ... + (n+1) + (n+1) + (n+1) \\
\implies 2S = n(n+1) \\
\implies S = \frac{n(n+1)}{2}
$$

Therefore, $$\sum_{I = 1}^n = \frac{n(n+1)}{2}$$.

<br>

## 2: Combinatorial Proof

We'e also seen the second proof before, as an example of a combinatorial proof. 