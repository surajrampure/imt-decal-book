# Common Proof Techniques

Throughout this section, we will introduce some of the most famous and most common proof techniques that are used to verify the truth of a mathematical statement. Remember, all of these techniques assume you have some basic information present and attempt to use the information you have to arrive at the correct conclusion.

### Index
* Direct Proof
* Proof by Contradiction
* Proof by Contraposition
* Proof by Cases

<br>

## Direct Proof

The direct proof is the simplest type of proof. In a direct proof, given certain information, we determine the validity of some other information. Direct proofs are often used in mathematical formulas, where simple arithmetic manipulations of given information can get us where we need to be.

### Example

**Consider $$x, y, z \in Z^+$$. Prove that if $$x \big| y$$ and $$x \big| z$$, then $$y + z$$.**

The first step in each proof is representing the information that we are allowed to assume, using precise mathematical notation. We are given that $$x$$ divides $$y$$ and that $$x$$ divides $$z$$. In mathematical notation, this means that there are integers $$a_1$$ and $$a_2$$ such that $$a_1 \cdot x = y$$ and $$a_2 \cdot x = z$$. Furthermore, since we are told $$x, y$$ and $$z$$ all belong to the set of positive integers, we know that $$a_1, a_2$$ must also be positive. There is not much more information we can garner from this now, so we look at what we are trying to prove. 

By writing out equations relating $$x$$ and $$y$$ (and $$x$$ and $$z$$), we have concrete information that we can use in our proof. Then:

$$
y+z = a_1 \cdot x + a_2 \cdot x = (a_1 + a_2) \cdot x
$$

We have shown that $$y+z$$ can be written as some positive integer – precisely, $$a_1 + a_2$$ – multiplied by $$x$$, hence proving $$x$$ divides $$y+z$$. This example gives us the natural flavor of direct proofs – we assume and work with the information we have, and reformulate it to match what we want to prove in some capacity.

<br>

## Proof by Contradiction

Proof by contradiction is one of the most widely used proof techniques, and it stems from a really nice observation. The problem statement remains the same; we are trying to prove some statement $$S$$. We begin by assuming not $$S$$ – that is, that $$S$$ is false - and prove that there is some piece of information that is both true and false at the same time. Since this can not happen, we know that our initial assumptions must be false. Since our initial assumption was that $$S$$ was false, we know this cannot be the case, thus $$S$$ must be true, proving our statement.

The contradiction can come about in many ways. For example, showing two things that cannot be equal as equal – such as $$0 = 2$$ – or showing some given information (which was told to us to be true) is false if statement $$S$$ is false. Whatever the contradiction might be, this proof technique presents a relatively straightforward way to prove the validity of the statement without worrying about the specific reason why the statement it holds. In specific, proof by contradiction is powerful when trying to prove a statement which implies non-existence of some entity.

### Example

**Prove that there is no greatest even integer.**

Let us think for a second why we would not want to use direct proof. To use a direct proof, we would need to somehow consider every single case and prove that it is not possible, which is extremely difficult. Instead, we go by proof of contradiction.

Instead, let us assume that there is a greatest even integer. Let us call this greatest even integer $$M$$. Define $$N$$ to be $$M+2$$. Then, $$N$$ is an even integer and it is strictly greater than $$M$$. Hence, $$M$$ is not the greatest even integer, which contracts our earlier assumption. This means that there is no greatest even integer.

### Example

**Prove that the negative of an irrational number is irrational.**

To prove this using a direct proof, we would need to show that there is no number for which this is not true. Instead, we go by the way of contradiction. We assume the statement is not true. The negation of this sentence states that there is *some* irrational number for which its negation is actually rational. Call this number $$x$$. So, $$-x = \frac{a}{b}$$, for $$a, b \in Z$$. We can multiply each side by $$-1$$ and obtain that $$x = -\frac{a}{b} = \frac{-a}{b}$$. It is important to note that $$-a$$ is still an integer, as is $$b$$. So, $$x$$ is actually equal to the division of two integers, which proves it to be rational. But, we assumed $$x$$ to be irrational to begin with. A number can not be rational and irrational at the same time, so we have arrived at a contradiction. Hence, our initial assumption must have been incorrect, and there does not exist any irrational number for which its negation is rational.

Getting a handle on this proof technique is tricky, and only practice can really solidify a true understanding of it.

<br>

## Proof by Contraposition

A proof by contraposition can be used when dealing with a statement of the form: Given information $$P$$, prove $$Q$$ is true.  Symbolically, the statements "$$P$$ implies $$Q$$" and "not $$Q$$ implies not $$P$$" can be written as

$$
P \implies Q
$$


and

$$
\neg Q \implies \neg P
$$

The latter is known as the **contrapositive** of the former, which is where the proof technique stems from. It is a nice fact of mathematics (and can be proven using truth tables) that the validity of $$P$$ implying $$Q$$ holds in the exact places where not $$Q$$ implies not $$P$$ holds, i.e. that $$P \implies Q \equiv \neg Q \implies \neg P$$. So, if $$P$$ implying $$Q$$ is too hard to prove, we can assume not $$Q$$ and imply not $$P$$ instead. This will intrinsically prove our original statement. 


### Example

**Prove that if $$x^2$$ is even, then $$x$$ is even.**

We can easily use a direct proof for this problem, though we will use contrapositive to introduce the general problem solving technique.

Remember, the contrapositive is of the form not $$Q$$ implies not $$P$$ (if our original problem statement reads $$P$$ implies $$Q$$). Here, $$P$$ is the statement "$$x^2$$ is even", while $$Q$$ is "$$x$$ is even." Thus, the contrapositive states that if $$x$$ is not even, then $$x^2$$ is not even either. Proving this will prove our original statement.

So we begin. If $$x$$ is not even, then $$x$$ is odd. Hence, $$x^2$$ is the product of two odd numbers, which in itself is odd. So, $$x^2$$ is not even, and we have proven the contrapositive. The validity of our original statement is then asserted.

<br>

## Proof by Cases

The last proof technique we will discuss in the section is proof by cases. In many instances, we may find it easier to view a statement as the combination of many sub-cases. By proving each possible sub-case, we can prove the validity of the full statement. The technique we use for each sub-case can be any one of the above.


### Example

**Prove that the cube of any integer is either a multiple of 9, 1 more than a multiple of 9, or one less than a multiple of 9.**

Since we are looking at multiples of 9, we should look at how numbers behave when divided by 9. We know from earlier in the course that when dividing a number by 9, the remainder can be anywhere from 0 to 8, inclusive. 

_Case 1_: $$n = 3k$$
First, we look at numbers that are divisible by 3, which we can represent as $$3k$$ for some positive integer $$k$$. Cubing $$n$$, we get $$n^3 = (3k)^3 = 27k^3 = 9(3k^3)$$. Clearly, for all $$k$$, this is a multiple of $$9$$, therefore we've proved the statement for all integers that are multiples of 3.

_Case 2_: $$n = 3k + 1$$
Next, we explore the case where there is a remainder of 1 after dividing by 3, so the number is $$3k + 1$$ for some $$k$$. Cubing $$n$$ yields $$n^3 = (3k+1)^3 = 27k^3 + 27k^2 + 9k + 1 = 9(3k^3 + 3k^2 + k) + 1$$, which shows that in this case $$n^3$$ is 1 greater than a multiple of 9. Thus, we've proved the statement for all integers that have remainder 1 when divided by 3.

_Case 3_: $$n = 3k + 2$$
The last case is when a number has a remainder of 2 when being divided by 3. This means we can write $$n$$ as $$3k+2$$; equivalently, we can write $$n$$ as being 1 less than a multiple of 3, i.e. $$n = 3k - 1$$ (think about why this is true). Then, $$n^3 = (3k-1)^3 = 27k^3 - 27k^2 + 9k - 1 = 9(3k^3 - 3k^2 + k) - 1$$, which shows in this case that $$n^3$$ is 1 less than a multiple of 9. Now, we've proved the statement for all integers that have remainder 2 when divided by 3.

We have considered three cases, and these three cases make up the whole universe of integers. Either an integer is divisible by 3, one more than a multiple of 3, or 2 more than a multiple of 3 (and consequently, 1 less than some other multiple of 3). The statement holds for these three cases, so it holds for every integer. It may not be immediately evident why splitting this problem into cases is the best way to proceed, but that is what practice is for.

<br>

Interestingly enough, there are usually multiple ways to prove any statement. In the next section, we will look at several different ways to prove a statement that we've already seen in this course – $$\sum_{i = 1}^n i = \frac{n(n+1)}{2}$$.
