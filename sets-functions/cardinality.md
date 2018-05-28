# Cardinality, Principle of Inclusion-Exclusion

In the previous section, we studied various properties of sets and interactions between sets. Here, we formalize the concept of the size of a set. We will only deal with finite sets in this note; we will look more at the size of infinite sets when we look at the sets of numbers. 

<br>

### Definition
For a finite set $$S$$, we define the **cardinality** of $$S$$, or $$\big| S \big|$$, to be the number of elements in $$S$$. For example, if $$S = \{1, 2, 3, 4, 5\}$$, we say $$\big| S \big| = 5$$. 

Previously, we said if two sets were subsets of one another, then those two sets were equal. We can translate that definition over to the idea of cardinality as well: if two sets $$A, B$$ are such that $$\big| A \big| \leq \big| B \big| $$ and $$\big| B \big| \leq \big| A \big|$$, then $$\big| A \big| = \big| B \big|$$. It turns out there is a special name for the relationship between two sets with equal sizes – we say these two sets have a **bijection** between them. We will study bijections more when we look at functions.

#### Set Operations
Since the result of the set operations we studied earlier were also sets, it is natural to want to look at the cardinalities of the results of these operations. With the Cartesian product, we have $$\big| A \times B \big| = \big| A \big| \cdot \big| B \big|$$, since each element in $$A \times B$$ features one element in $$A$$ and one element in $$B$$. Refer to the example in the previous section if you are having trouble seeing why this is true.

However, for the other operations, the generalization doesn't come so easily. For the intersection and difference of $$A$$ and $$B$$, it really depends on the nature of the sets. However, there is a nice way of thinking about the cardinality of the union of two (or more) sets, which we will look at now.

<br>

### Principle of Inclusion-Exclusion for Two Sets

First, we look at the size of the union of two disjoint sets. If $$A \cap B = \emptyset$$, it is relatively clear that $$\big| A \cup B \big| = \big| A \big| + \big| B \big|$$. A rough justification is as follows: Start off with $$A \cup B$$ being empty, and add elements. We add all $$\big| A \big|$$ elements in $$A$$. Since none of the elements in $$B$$ have already been added, we now add all $$\big| B \big|$$ elements in $$B$$, yielding a total size of $$\big| A \cup B \big| = \big| A \big| + \big| B \big|$$.

We now want to find $$\big| A \cup B \big|$$, in terms of $$\big| A \big|$$ and $$\big| B \big|$$, where $$A, B$$ aren't necessarily disjoint. To proceed, we make a simple but powerful realization:
- All elements in $$A$$ are either only in $$A$$, or in both $$A \cap B$$
- All elements in $$B$$ are either only in $$B$$, or in both $$A \cap B$$

This means we can actually write $$A = (A - B) \cup (A \cap B)$$ and $$B = (B - A) \cup (A \cap B)$$. Furthermore, $$A - B$$ and $$A \cap B$$ are disjoint (think about why this is true), as are $$B-A$$ and $$A \cap B$$. 

$$A \cup B$$, the quantity we want, consists of everything that is only in $$A$$, everything that is only in $$B$$, and the intersection of $$A$$ and $$B$$, with the intersection counted exactly once. That is, $$A \cup B = (A - B) \cup (B - A) \cup (A \cap B)$$. But, by adding $$\big| A \big|$$ and $$\big| B \big|$$, we are left with $$\big| A \big| + \big| B + \big| = \big| (A - B) \cup (A \cap B) \big| + \big| (B-A) \cup (A \cap B) \big| = \big|(A-B) + (B-A) \big| + 2\big|A \cap B  \big|$$ (by the above theorem on disjoint sets). However, counting $$\big| A \cap B \big|$$ twice, when we only want to count it once. Subtracting this intersection yields the statement of the Principle of Inclusion-Exclusion with two sets.

<br>

**Theorem (Principle of Inclusion-Exclusion)**

For two finite sets $$A$$ and $$B$$,
$$
\big| A \cup B \big| = \big| A \big| + \big| B \big| - \big| A \cap B \big|
$$

<br>

**Example**

All 150 high school seniors at Billy High are required to take at least one of Calculus or Statistics. 100 students are enrolled in Statistics, and 70 are enrolled in Statistics. How many are enrolled in both?

Let $$C$$ be the set of students taking Calculus, and $$S$$ be the set of students taking Statistics. We are given $$\big| C \cup S \big| = 100$$, $$\big| C \big| = 70$$ and $$\big| S \big| = 100$$, and we are asked to find $$\big| C \cap S \big|$$. We substitute our known values into the Principle of Inclusion-Exclusion theorem to yield $$100 = 70 + 100 - \big| C \cap S\big|$$, implying that there are $$\big| C \cap S \big| = 20$$ students taking both Calculus and Statistics.

<br>

**Example 2**

We will now introduce a universe into our problem. Suppose now that at the same high school of 150 seniors, students aren't necessarily required to take either Calculus or Statistics; they can elect to take neither. If 25 students are taking both, 100 students are taking Calculus and 20 students are taking neither, how many students are taking Statistics?

At this stage, we have two unknowns – the size of $$\big| C \cup S \big|$$ and the size of $$\big| S \big|$$. We need two equations in terms of these unknown quantities to solve for them. We can use the Principle of Inclusion-Exclusion to find $$\big| C \cup S \big| = 100 + \big| S \big| - 25$$. Where do we go now?

The trick in this question is that we're actually given the size of the universe, $$\big| U \big| = 150$$. Our solution lies in this realization – either a student is taking one of the courses, or they are not. The sum of the number of students in each of these disjoint groups must be 150. We are given that 25 students aren't taking either course, meaning $$150 = \big| C \cup S \big| + 25$$, i.e. $$\big| C \cup S \big| = 125$$, allowing us to solve $$\big| S \big| = 50$$.

The corollary we used in this problem is stated formally below.

<br>

**Corollary**

If $$A, B \subset U$$, then

$$\big| U \big| = \big| A \cup B \big| + \big| A^c \cap B^c \big|$$

<br>
