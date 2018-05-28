# Introduction to Sets

In this section, we will look at the formal definition of a set, a subset, and identify various operations that act on multiple sets. We also introduce the idea of the universal set and a compliment. One notion omission is any discussion on the size of a set; we save this for the next section.

<br>

### Definition

In mathematics, a **set** is a well-defined collection of objects. By well-defined, we mean that for any object $$x$$, we can easily determine whether or not $$x$$ is an element (also referred to as a "member") of the set. Formally, if $$S$$ is a set, we write $$x \in S$$ to state that $$x$$ is in the set $$S$$, and $$x \not \in S$$ to state the opposite. 

We define sets in one of two ways:
- By listing out all of the elements in the set, e.g. $$A_1 = \{1, 3.14, -15, \pi + e\}$$, $$A_2 = \{..., -3, -2, -1, 0, 1, 2, ...\}$$ or $$A_3 = \{ \text{Lebron, Jordan, Kobe} \}$$
- By stating a property that determines the set, e.g. $$A_4 = \{x \big| x + 3 \: \text{is prime} \}$$ or $$A_5 = \{t : t^2 - 5t + 6 = 0 \}$$

Some remarks:
- The symbols $$:$$ and $$\big|$$ both translate to "such that", and precede the condition for inclusion into a set. 
- It should be noted that sets can either have finitely many elements, as in $$A_1$$, $$A_3$$ and $$A_5$$, or infinitely many elements, as in $$A_2$$ and $$A_4$$ above. This is a concept we will explore further later in the chapter.

<br>

### Subsets
Given some set $$A$$, another set $$B$$ is a **subset** of $$A$$ if and only if every element in $$B$$ is also an element of $$A$$. Symbolically, we represent this relationship as $$B \subset A$$ (just like with $$\geq, >, \leq, <$$ signs, the $$\subset$$ sign opens towards the larger set), and it's opposite (i.e. $$B$$ is not a subset of $$A$$) as $$B \not \subset A$$. Equivalently, we can say $$A$$ is a **superset** of $$B$$.

For example, if $$A = \{1, 5, 7, 9, 12\}$$ and $$B = \{7, 12\}$$, we can say $$B \subset A$$, but also that $$\{5, 6\} \not \subset A$$.

What if two sets $$A$$ and $$B$$ are subsets of one another – what can we infer about $$A$$ and $$B$$? This would have to mean every element in $$A$$ is in $$B$$, and every element in $$B$$ is in $$A$$. It turns out that this is the exact condition for set equality. Formally, we can say two sets $$A$$ and $$B$$ are **equal** if and only if both $$A \subset B$$ and $$B \subset A$$; in this case we could also write $$A = B$$. 

All sets are subsets of themselves. We say set $$B$$ is a **proper subset** of $$A$$ when $$B \subset A$$ and $$A \neq B$$.


<br>


### Set Operations
We will now look at four operations that act on multiple sets – union, intersection, difference and product. Note that these operations are all **closed**, meaning that the results are all also sets (as opposed to being elements of sets, or numbers, or anything else). 

<br>

#### Union
The **union** of two sets $$A, B$$ is the set of everything contained by either $$A$$ or $$B$$. Formally:

$$A \cup B = \{x \big| x \in A \: \text{or} \: x \in B \}$$

For example, if $$A = \{1, 5, 7\}$$ and $$B = \{2, 3, 7, 8\}$$, $$A \cup B = \{1, 2, 3, 5, 7, 8\}$$. Note that even though there was a 7 in both sets, the 7 is not repeated within the set. It is also worth noting that finite sets need not necessarily be ordered; we could equivalently write $$A = \{5, 7, 1\}$$ and $$A \cup B = \{8, 5, 1, 3, 2, 7 \}$$. 

For any set $$A$$:
- $$A \cup A = A$$ (Justification: $$\{x \big| x \in A \: \text{or} \: x \in A\} = \{x \big| x \in A \}$$)
- $$A \cup \emptyset = A$$ (Justification: $$\{x \big| x \in A \: \text{or} \: x \in \emptyset\} = \{x \big| x \in A \}$$)

<br>

#### Intersection
The **intersection** of two sets $$A, B$$ is the set of everything contained in both $$A$$ and $$B$$. Formally:

$$A \cap B = \{x \big| x \in A \: \text{and} \: x \in B \}$$

Using the same examples as before, $$A \cap B = \{7 \}$$.

For any set $$A$$:
- $$A \cap A = A$$ (Justification: $$A \cap A = \{x \big| x \in A \: \text{and} \: x \in A \} = \{x \big| x \in A\}$$)
- $$A \cap \emptyset = \emptyset$$ (Justification: $$A \cap \emptyset = \{x \big| x \in A \: \text{and} \: x \in \emptyset \} = \{x \big| x \in \emptyset\}$$)

If $$A \cap B = \emptyset$$, we say $$A$$ and $$B$$ are **disjoint** – they share no elements.


<br>

#### Difference
The **difference** of two sets $$A, B$$ is the set of everything contained in $$A$$ but not contained in $$B$$. Formally:

$$A - B = \{x \big| x \in A, x \not \in B \}$$

With our example, $$A - B = \{1, 5\}$$. Notice that the difference operation is the first set operation that we've studied in which the other matters. $$A \cup B = B \cup A$$ and $$A \cap B = B \cap A$$, but $$A - B \neq B - A$$ – unlike the union and intersection, the difference operation is not **symmetric**. 

<br>

#### Cartesian Product
The **Cartesian product** of two sets $$A, B$$ is the set of all possible combinations of one element in $$A$$ and one element in $$B$$. Quite literally:

$$A \times B = \{(x, y) \big| x \in A, y \in B  \}$$

Let's use a smaller example – let $$A = \{1, 2, 3\}$$ and $$B = \{x, y, z\}$$. Then, we have

$$A \times B = \{(1, x), (1, y), (1, z), (2, x), (2, y), (2, z), (3, x), (3, y), (3, z) \}$$

Notice that the Cartesian product is also not symmetric – if we instead looked at $$B \times A$$, each of the ordered pairs in the set above would be flipped.

<br>

While we only defined the above set operations on two sets, since the result of any of these operations is also a set, we can combine these operations in any way we want. For example, $$A \cup B \cup C$$ can be thought of as $$(A \cup B) \cup C$$, or $$A \cup (B \cup C)$$. We can't assign parentheses as arbitrarily when we combine operations, though: $$(A \cap B) \cup C \neq A \cap (B \cup C)$$ in general.

Note on vector spaces: Algebraic vector spaces are actually defined by a Cartesian product, of the real numbers. The symbol $$\mathbb{R}^n$$ refers to the Cartesian product of the set of real numbers (which we have yet to define) with itself $$n$$ times, i.e. the set of all real-valued vectors with $$n$$ elements.

<br>

### The Complement

Often when dealing with sets, we work relative to some _universal_ set, which contains all relevant objects. For example, when choosing three students from a class of thirty, the set of all students in the class refers to the universe, and any particular subset of three students we choose can denote our set of interest. Using a numerical example, if we let the universe be $$U = \{1, 2, 3, 4, 5, 6, 7, 8, 9, 10\}$$, any set $$A$$ we deal with will be a subset of $$U$$.

Suppose $$A = \{1, 2, 4, 8\}$$. Sometimes, we want to consider the set of elements that are **not** in $$A$$ – this is known as the **complement** of $$A$$. Without a universe, this is impossible to quantify, but with a universe this is quite easy. In our case, the complement of $$A$$ (denoted $$A'$$, $$A^{c}$$ or $$\bar{A}$$) is $$A^c = \{3, 5, 6, 7, 9\}$$. In general:

$$A^c = \{x \big| x \not \in A, x \in U \}$$

<br>

#### De Morgan's Laws
We can actually combine the idea of the complement of a set with the union and intersection operations, by **De Morgan's Laws**, as follows:
- $$(A \cup B)^c = A^c \cap B^c$$
- $$(A \cap B)^c = A^c \cup B^c$$

Since we have yet to cover formal proof techniques, we save the proof for Chapter 3. However, it should be noted that De Morgan's Laws allow us to convert from a union to an intersection, and vice versa.

Let's work out an example as a sanity check. Suppose again that $$U = \{1, 2, 3, 4, 5, 6, 7, 8, 9, 10\}$$, $$A = \{1, 2, 4, 8\}$$ and $$B = \{3, 4\}$$. Then:

$$(A \cup B)^c = \{1, 2, 3, 4, 8 \}^c \\ = \{5, 6, 7, 9\} \\ = \{3, 5, 6, 7, 9\} \cap \{1, 2, 5, 6, 7, 8, 9, 10\}
\\ = A^c \cap B^c$$

You should work out the second case on your own, and verify that it works.