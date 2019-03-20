<title>Propositional Logic – IMT DeCal</title>

# Propositional Logic
---

<br>

<!--

Jump to:
* [Propositions](#propositions)
* [Logical Operators](#logicaloperators)
	* [Conjunction](#conjunction)
	* [Disjunction](#disjunction)
	* [Negation](#negation)
		* [Exclusive OR](#xor)
* [De Morgan's Laws](#demorgan)
* [Implications](#implication)
* [Extensions of the Implication](#contra_and_conv)
	* [Contrapositive](#contra)
	* [Converse](#converse)
	* [If and only if](#iff)
* [Quantifiers](#quantifiers)
	* [De Morgan's Laws for Quantifiers](#demorgans_quantifiers)
* [Converting Sentences](#sentence_examples)

<br>

-->

Often introduced with set theory is the concept of propositional logic. Knowledge of propositional logic is crucial to formalizing proof techniques, which we will do in the following chapter. This article will be relatively interactive - it's in your best interest to do the examples yourself as you read.

<br>

<a name='propositions'>

## Propositions
---

</a>

A **proposition** is a statement that is has a definitive value - either true or false. We usually denote a proposition that depends on some variable $$x$$ is usually denoted by $$P(x)$$.

For example, "13 is prime" and "it is currently 93 degrees outside" are propositions. Each of these statements is either definitively true, or definitively false. However, statements like "LeBron James is the best basketball player of all time" or "statistics is a hard subject" are NOT propositions - they are opinions, and their "truth value" varies from person to person.

The statements "$$x$$ is prime" and $$a > b$$ are also propositions, but they depend on variables. We might use $$P(x)$$ to represent the proposition "$$x$$ is prime", and $$G(a, b)$$ to represent "$$a > b$$". For example, $$P(15)$$ is false, and $$G(10, 3)$$ is true.

<br>

<a name = 'logicaloperators'>

## Logical Operators
---

</a>

There are three commonly used **logical operators**, and each has a counterpart that we've already studied in set theory.

<a name = 'conjunction'>

### Conjunction ($$\wedge$$)
---

</a>

The **intersection** ($$\cap$$) operation over two sets corresponds to the **and** ($$\wedge$$) operation over two propositions.

The set $$A \cap B$$ is the set of elements that are in $$A$$ AND in $$B$$; similarly, the proposition $$P \wedge Q$$ is true only when both $$P$$ is true AND $$Q$$ is true. We can say $$A \cap B = \\{ x : x \in A \wedge x \in B \\}$$ . The "and" operation is sometimes referred to as a _conjunction_.

The following **truth table** defines the AND operation. It gives the output of $$P \wedge Q$$ on all possible combinations of inputs. Since $$P$$ is either true or false, and $$Q$$ is either true or false, we have four rows.

<div align=center>

| $P$ | $Q$ | $P \wedge Q$ |
| --- | --- | --- |
| T | T | T |
| T | F | F |
| F | T | F | 
| F | F | F |

</div>

<a name = 'disjunction'>

### Disjunction ($$\vee$$)
---

</a>

The **union** ($$\cup$$) operation over two sets corresponds to the **or** ($$\vee$$) operation over two propositions.

The set $$A \cup B$$ is the set of elements that are in $$A$$ OR in $$B$$; similarly, the proposition $$P \vee Q$$ is true when $$P$$ is true OR when $$Q$$ is true. We can say $$A \cup B = \\{ x : x \in A \vee x \in B \\}$$. Remember, in mathematical logic, "or" is not exclusive – if both $$P$ and $Q$$ are true, $$P \vee Q$$ is still true. The "or" operation is sometimes referred to as a _disjunction_.

Again, we give the truth table:

<div align=center>

| $P$ | $Q$ | $P \vee Q$ |
| --- | --- | --- |
| T | T | T |
| T | F | T |
| F | T | T | 
| F | F | F |

</div>

<a name = 'negation'>

### Negation ($$\neg$$)
---

</a>

The analogue of the complement of a set is the **negation** ($$\neg$$) of a proposition. We say $$\neg P$$ is true only when $$P$$ is not true, and false only when $$P$$ is not false. We can say $$A^C = \\{ x : \neg (x \in A) \\}$$.

<div align=center>

| $P$ | $\neg P$ |
| --- | --- | 
| T | F | 
| F | T |

</div>

We can use the above logical operators to create more complex logical expressions, which themselves also take on the value true or false. For example, if $$P$$ is true only when $$x$$ is prime, $$E$$ is true only when $$x$$ is positive and even, and $$U$$ is true only when $$x$$ is under 100, the expression $$P \vee (\neg E \wedge U)$$ is a logical expression that depends on $$x$$ and is true only when $$x$$ is prime or both not even and under 100.


<a name='xor'>

#### Example: Exclusive OR </a>

Another important definition at this point is the **XOR** operation, represented by the $$\oplus$$ symbol. The standard "A or B" operation evaluates to true in each of the following cases:
- Only $$A$$ is true
- Only $$B$$ is true
- Both $$A$$ and $$B$$ are true

For example, if someone asks "are you in EE 16A or CS 61A?", you answer yes, whether you're in 16A, 61A, or both. The XOR operation, instead, is exclusive – it is only true when either $$A$$ is true, or $$B$$ is true, but not both. For example, when getting a sub combo at Subway, you're asked if you want chips or a cookie – you get either chips, or a cookie, but not both. 

We mentioned above that all logical statements can be decomposed into some combination of conjunctions, disjunctions and negations. $$A \oplus B$$ should be true when either $$A$$ or $$B$$ is true, and false when both are true (or both are false). The first clause can be represented by $$A \vee B$$, and the latter by $$\neg (A \wedge B)$$. Chaining these together with a $$\wedge$$, we have

<div align=center>

$$A \oplus B \equiv (A \vee B) \wedge \neg(A \wedge B)$$

</div>

Let's prove this with a truth table.

<div align=center>

| $$A$$ | $$B$$ | $$A \oplus B$$ | $$(A \vee B) \wedge \neg(A \wedge B)$$ |
|---|---|---|---|
|True|True|False|False|
|True|False|True|True|
|False|True|True|True|
|False|False|False|False|

</div>

If we think of $$A$$ and $$B$$ being bits instead – i.e. 1 when True, 0 when False – then we have that $$A \oplus B = 1$$ when $$A + B$$ is odd, and $$A \oplus B = 0$$ when $$A + B$$ is even.


<br>

<a name='demorgan'>

## De Morgan's Laws
---

</a>

De Morgan's Laws allow us to simplify and re-write negations. Recall, we saw in **[the first note](sets-and-set-operations.html)** that the following rules apply for sets $A, B$:

<div align=center>

$$(A \cap B)^C = A^C \cup B^C$$

$$(A \cup B)^C = A^C \cap B^C$$

</div>

It turns out that the same rules apply for propositions $P, Q$!

<div align=center>

$$\neg(P \wedge Q) \equiv \neg P \vee \neg Q$$

$$\neg(P \vee Q) \equiv \neg P \wedge \neg Q$$

</div>

Notice, we flip our conjunctions into negations, and vice versa. 

We can actually use truth tables to prove De Morgan's Laws. We use truth tables to **prove** that two logical expressions are **equivalent**, i.e. that upon the same inputs, they produce the same outputs. (The $$\equiv$$ symbol translates to "equivalent.")

Let's prove the equivalence $\neg(P \wedge Q) \equiv \neg P \vee \neg Q$:

<div align=center>

| $P$ | $Q$ | $\neg(P \wedge Q)$ | $\neg P \vee \neg Q$ |
| --- | --- | --- | --- | 
| T | T | F | F |
| T | F | T | T
| F | T | T | T |
| F | F | T | T

</div>

Since the columns for $$\neg(P \wedge Q)$$ and $$\neg P \vee \neg Q$$ are identical, we say that the two expressions are equivalent. We'll leave the truth table for $$\neg(P \vee Q) \equiv \neg P \wedge \neg Q$$ as an exercise.

<br>

#### Example

Let's find the negation of the statement, "$$t$$ is even and not prime or irrational and prime". 

The first step is to convert the statement into propositional logic. We can use $$E$$ to represent the proposition "$$t$$ is even", $$P$$ for $$t$$ is prime, and $$I$$ for $$t$$ is irrational. Our statement then reads, $$(E \wedge \neg P) \vee (I \wedge P)$$.

Using De Morgan's Laws, we can propagate a negation through the expression:

<div align=center>

$$\begin{align*} \neg ((E \wedge \neg P) \vee (I \wedge P)) &\equiv \neg (E \wedge \neg P) \wedge \neg (I \wedge P) \\\ &\equiv (\neg E \vee P) \wedge (\neg I \vee \neg P) \end{align*}$$

</div>

In English, the negation reads, "$$t$$ is not even or prime, and not irrational or not prime." At this point in the course/book, we haven't started talking about how to prove such statements; for now, we're only concerned about the construction of them. We'll start proving such statements in Chapter 2.

<br>


<a name='implication'>

## Implications
---

</a>

Crucial in the study of propositional logic is the **implication** operation, which itself is a composition of the basic logical operators we saw above (though this might not be immediately obvious).

**The implication operation $$P \implies Q$$ says that if $$P$$ is true, then $$Q$$ must be true; if $$P$$ is false, it says nothing about $$Q$$ ($$Q$$ could either be true or false).** In English, implications often read "if $$P$$, then $$Q$$", or "$$Q$$ if $$P$$".

An example of an implication is the proposition "if today is Christmas, it is December.", However, if today is not Christmas, then it may or may not be December.

<div align=center>

$$\text{today is Christmas} \implies \text{the current month is December}$$

</div>

We use implications to prove statements to be true; if we can make a series of implications starting from a proposition that we know is true and ending with the proposition we want to prove, we have proven the final statement. We will explore this further in the next chapter.


As we mentioned above, the implication statement is a composition of the elementary logical operators - it turns out that $$P \implies Q \equiv \neg P \vee Q$$. The following truth table proves this equivalence:

<div align=center>

| $$P$$ | $$Q$$ | $$P \implies Q$$ | $$\neg P \vee Q$$ |
| ---   | ---   | ---              | ---               |
| True | True | True | True |
| True | False | False | False |
| False | True | True | True |
| False | False | True | True |

</div>

It's important to remember that implications are no different than conjunctions and disjunctions in the sense that they are propositonal statements with truth values. Another way to reason about the truth values of implications: Suppose I make the promise to you that if it rains tomorrow, I will give you 100 dollars. The "truth value" of this implication is whether or not I held my promise:

- If it rains tomorrow, and I give you 100 dollars, I held my promise! (T)
- If it rains tomorrow, and I don't give you 100 dollars, I did not hold my promise. (F)
- If it does not rain tomorrow, and I give you 100 dollars, I held my promise! (T)
- If it does not rain tomorrow, and I don't give you 100 dollars, I still held my promise! (T)

<br>

<a name='contra_and_conv'>

## Extensions of the Implication
---

</a>

The following are common logical expressions that are related to the implication of $$P \implies Q$$.


<a name='contra'>

### Contrapositive: $$\neg Q \implies \neg P$$
---

</a>

The contrapositive, $$\neg Q \implies \neg P$$, of an implication is actually logically equivalent to the implication itself! You should prove this to yourself using a truth table. However, without using a truth table we can see that:

<div align=center>

$$\begin{aligned}\neg Q \implies \neg P &\equiv \neg (\neg Q) \vee (\neg P) \\\ &\equiv Q \vee \neg P \\\ &\equiv \neg P \vee Q \\\ &\equiv P \implies Q \end{aligned}$$

</div>

Why does the contrapositive exist, then, if it's equivalent to the standard implication? That's a question that'll be answered in the following chapter in great detail. 

For now, let's look at an example. Consider the statement "if it is sunny outside, I will wear sunglasses". Its contrapositive is "if I don't wear sunglasses, it is not sunny outside" - both statements mean the same thing, as we expect. Another, more mathematical example: the contrapositive of the statement "if $$x$$ is even, $$x^2$$ is even" is the statement "if $$x^2$$ is not even, $$x$$ is not even".

<br>

<a name='converse'>

### Converse: $$Q \implies P$$
---

</a>

The converse, $$Q \implies P$$ of an implication, however, is not equivalent to the implication. If today is Christmas ($$P$$), then it implies that the current month is December ($$Q$$), however it being December ($$Q$$) doesn't mean that today is Christmas ($$P$$). **In general, if an implication is true, it does not mean that its converse is true!** There are some cases where a statement and its converse are both true, though. We have a name for that, which you'll read about shortly.

<br>

<a name='iff'>

### If and only iff: $$\iff$$ 
---

</a>

Another way we can represent the equivalence of two statements $$A \equiv B$$ is with the **if and only if** ($$\iff$$) symbol: $$A \iff B$$. If and only if (sometimes shortened to "iff") is a term that says one statement is true only when the other statement is true, and is false only when the other statement is false - in other words, that two statements are equivalent. **$$A \iff B$$ means that both $$A \implies B$$ and $$B \implies A$$ hold, i.e. both a statement and its converse hold**.

For example, "it is Christmas if and only if it is December 25th", which we can decompose into the two statements "it is Christmas if it is December 25th" and "it is December 25th if it is Christmas" is just a fancy way of saying "Christmas is on December 25th".

Consider the following truth table:

<div align=center>

| $$A$$ | $$B$$ | $$A \iff B$$ | $$(A \implies B) \wedge (B \implies A)$$ |
|---|---|---|---|
| True | True | True | True |
| True | False | False | False |
| False | True | False | False |
| False | False | True | True |

</div>

What this says, is that if two expressions imply one another, then they are equal. Today being Christmas implies that today is December 25th, and today being December 25th implies that today is Christmas - since these two propositions imply one another, we can say they're equivalent. 

An understanding of implication and "if and only if" statements will go a long way in understanding how proof techniques work.

Let's take a look at a few implications, alongside their contrapositives and converses.

<div align=center>

| **Statement** | **Contrapositive** | **Converse** |
| --- | --- | --- |
| **If it rains tomorrow, I will bring an umbrella.** | I will not bring an umbrella if it does not rain tomorrow. | If I bring an umbrella, it will rain tomorrow. | 
| **If the clock is between 12PM and 2PM and I am hungry, then it is lunch time.** | It is not lunchtime if the clock is not between 12PM and 2PM or I am not hungry. | If is lunchtime then the clock is between 12PM and 2PM and I am hungry. | 
| **If your final grade in this course is at least 70\%, you will pass.** | You will not pass if your final grade in this course is not at least 70\%. | If you pass this course, then your final grade is at least 70\%. | 
| **If two sets $$A, B$$ are disjoint, then the cardinality of their intersection is 0.** | The cardinality of the intersection of two sets $$A, B$$ is not 0 if they are not disjoint. | If the cardinality of the intersection of two sets $$A, B$$ is 0, they are disjoint. |

</div>

Notice that in statements 1, 2, and 3, the converse means something entirely different than the original statement. However, in the fourth statement, both the original statement (if two sets $$A, B$$ are disjoint, then the cardinality of their intersection is 0) and its converse (if the cardinality of the intersection of two sets $$A, B$$ is 0, they are disjoint) are true. 

In this case, we could say "the cardinality of the intersection of two sets $$A, B$$ is 0 if and only if they are disjoint." 

<br>


<a name='quantifiers'>

## Quantifiers
---

</a>

Quantifiers are the "glue" that allow us to write mathematical statements precisely. There are two:
- the **universal quantifier** ($$\forall$$, read as "for all"), and
- the **existential quantifier** ($$\exists$$, read as "there exists"). 

We actually used these quantifiers already in Chapter 1.2, when defining what a surjective function is. We said a function $$f: A \rightarrow B$$ is surjective when $$\forall b \in B, \exists a \in A : b = f(a)$$, which translates to "for all $$b$$ in the codomain, there exists some $$a$$ in the domain such that $$f$$ maps $$a$$ to $$b$$."

Let's illustrate their usage with examples. Suppose we want a statement to denote that all natural numbers are either even or odd. We can have $$E(x)$$ represent "$$x$$ is even" and $$U(x)$$ represent "$$x$$ is odd". Then, the statement $$\forall x \in \mathbb{N},  E(x) \vee U(x)$$ reads "for all natural numbers $$x$$, $$x$$ is even or odd". This statement happens to always be true, but something like $$\forall x \in \mathbb{N}, E(x) \wedge U(x)$$ is not true, as it is not the case that $$x$$ is both even and odd for all positive integers $$x$$. In fact, there isn't a single positive integer for which is this is true.

In general, you cannot reverse the order of different existential quantifiers. That is,

<div align=center>
$$(\forall x) (\exists y) P(x, y) \not \equiv (\exists y) (\forall x) P(x, y)$$
</div>

<br>

Let's reason about this with an example. Consider $P(x, y): y = x^2$ (note here we're implicitly letting our universe $\mathbb{U} = \mathbb{R}$). The first statement says that for all $x$, there is some $y$ such that $y = x^2$. In other words, it says that every real number $x$ has a square. This statement happens to be true. The second statement says that there is some magical $y$ that is equal to the square of every single $x$. That is, this $y$ (let's call it $y_0$) is such that $y_0 = 1^2, y_0 = \pi^2, y_0 = 100^2, ...$. This statement is definitely very false. These are both saying very different things!

<br>

<a name='demorgans_existence'>

### De Morgan's Laws for Existential Quantifiers
---
</a>

To round out our discussion on propositional logic, we need to once again look at De Morgan's Laws, but for existential quantifiers. 

<div align=center>

$$\neg(\forall x, P(x)) \equiv \exists x, \neg P(x) \\\ \neg(\exists x, P(x)) \equiv \forall x, \neg P(x)$$

</div>

As an example, suppose $$P(x)$$ is the statement "$$x$$ is prime", and suppose we restrict our universe to be the positive integers.

1. The first version tells us the statements "it is not true that $$x$$ is prime for all $$x$$" and "there exists some $$x$$ that is not prime" are equivalent
2. The second version tells us the statements "it is not true that there exists an $$x$$ that is prime" and "for all $$x$$, $$x$$ is not prime" are equivalent

Since we know that it is false that all positive integers are prime, it must be true that there is at least one positive integer that isn't prime, and indeed that is true (this is because if a statement is false, its negation must be true, and vice versa).

We can extend this principle to multivariate propositions:

<div align=center>

$$\neg ((\forall x)(\exists y)Q(x, y)) \equiv (\exists x)(\forall y) \neg Q(x, y) \\: \\: \\: \\: (1) \\\ \neg ((\exists x)(\forall y)Q(x, y)) \equiv (\forall x)(\exists y) \neg Q(x,y) \\: \\: \\: \\: (2)$$

</div>

Notice how the negation symbol propagates down the statement, flipping $\forall$ to $\exists$ and vice versa.

Let's look at an example. Suppose $$Q(x, y): y = x^2$$. For example, $$Q(3, 4)$$ is the proposition that $$4 = 3^2$$, which happens to be false. 

- _Equation 1_: The left hand side, $ \neg ((\forall x)(\exists y) \neg Q(x, y))$, states that "it is not the case that every $x$ has some $y$ such that $y = x^2$", i.e. "it is not the case that every real number $x$ has as square." The right hand side, $(\exists x)(\forall y) \neg Q(x,y)$, is "there exists some $x$, such that for all $y$, $y \neq x^2$", i.e. "there exists some real number $x$ that does not have a square." These two statements are saying the same thing: if not all real numbers have squares, there must exist some real number without a square.
- _Equation 2_: The left hand side, $\neg ((\exists x)(\forall y)Q(x, y))$, states that "it is not the case that there exists some $x$ such that for all $y$, $y = x^2$", i.e. "there is no $x$ that satisfies $y = x^2$ for all $y$." The right hand side, $(\forall x)(\exists y) \neg Q(x,y)$, says that "every $x$ has some $y$ such that $y \neq x^2$." Again, these two statements are saying the same thing: if there is no $x$ that satisfies $y = x^2$ for every single $y$, then every $x$ has some value of $y$ such that $y \neq x^2$.

These statements are slightly difficult to parse. Make sure you read them carefully!

We can even apply De Morgan's Laws to conjunctions and disjunctions AND existential quantifiers at the same time. For example, the statement

<div align=center>

$$\forall q \in \mathbb{Q}, (\exists t \in Q : qt = 1 \vee q = 0)$$

</div>

reads "all natural numbers $q$ have an inverse or are equal to 0." Its negation,

<div align=center>

$$\exists q \in Q, (\forall t \in Q:qt \neq 1 \wedge q \neq 0) $$

</div>

reads "there exists some non-zero rational number $q$ that does not have an inverse."

<br>

We can even propagate a negation through a long chain of propositions and quantifiers:

<div align=center>

$$\neg (\forall x \exists y: P(x, y) \vee Q(y)) \equiv \exists x \forall y :  \neg P(x, y) \wedge \neg Q(y)$$

</div>

<br>

<a name='sentence_examples'>

## Examples
---

</a>

Let's take a look at examples of converting sentences in English to precise, mathematical statements using the tools we've studied in this chapter. It should be noted, there isn't necessarily only one right way to re-write a statement in English into logic.

<div align=center>

| **English** | **Propositional Logic** |
|---|---|
| There exists an integer solution to the equation $$x^2 + 2x + 1 = 0$$ | $$(\exists x \in \mathbb{Z})(x^2 + 2x + 1 = 0)$$ |
| There are no three positive integers $$a$, $b$, $c$$ that satisfy the equation $$a^n + b^n = c^n$$ for any integer value of $$n$$ greater than 2. | $$\neg(\exists a,b,c,n \in \mathbb{Z}^+)(n > 2 \wedge a^n + b^n = c^n)$$ |
| $$\sqrt{2}$$ is a rational number. | $$(\exists a, b \in \mathbb{Z})(\sqrt{2} = \dfrac{a}{b})$$ | 
| For $$-1 < r < 1, r \in \mathbb{R}$$, the sum of the series $$1 + r + r^2 + r^3 + \cdots$$ is equal to $$\dfrac{1}{1-r}$$. | $$(\forall r \in \mathbb{R} : -1 < r < 1)(\sum_{n=0}^{\infty} r^n = \dfrac{1}{1-r})$$ |
| All rational numbers have a multiplicative inverse or are 0.| $$\forall q \in \mathbb{Q}, (\exists t \in Q : qt = 1 \vee q = 0)$$ |

</div>
