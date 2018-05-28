# Functions

We now have enough background to introduce functions in a formal way. 

**Note**: We briefly mention the idea of the set of real numbers in some of the following examples, though we have not yet described what the real number set is. That's because we think it's best to study the definition of a function before we study the various number sets (covered in the next section). However, the usage of the real numbers here is not very detailed nor significant, but feel free to ask questions for clarification!

<br>

### Definition

We say $$f$$ is a **function** with _domain_ $$A$$ and _codomain_ $$B$$ if $$f \subset A \times B $$ such that for every element in $$A$$, there is exactly one element in $$B$$. Symbolically, we represent this as $$f : A \rightarrow B$$.

<br>

Recall from the last section, the cross product $$A \times B$$ of two sets $$A, B$$ is another set, that contains all possible combinations of one element in $$A$$ and one element in $$B$$. For example, if $$A = \{\text{"Hi"}, \text{"Hey"} , \text{"Hello"}\}$$ and $$B = \{5, 10, 15 \}$$, we would have

$$A \times B = \{ (\text{"Hi"}, 5), (\text{"Hi"}, 10), (\text{"Hi"}, 15), (\text{"Hey"}, 5), (\text{"Hey"}, 10), (\text{"Hey"}, 15), (\text{"Hello"}, 5), (\text{"Hello"}, 10), (\text{"Hello"}, 15) \}$$

We form a function $$f$$ by removing elements from $$A \times B$$ such that there are only as many elements as there are in $$A$$. The following is an example of some function $$f$$, sending elements from $$A$$ to $$B$$:

$$f = \{ (\text{"Hi"}, 10), (\text{"Hey"}, 5), (\text{"Hello"}, 5) \}$$

We say $$A$$ is the **domain**, as it represents all possible inputs, and $$B$$ is the **codomain**, as it represents all possible outputs; as a result, we say that $$f(A) = B$$. However, the **image**, or **range**, is the set of all actual outputs of a function. In the example $$f$$ above, the image would not be $$B$$, since 15 is never actually an output (though it is a possible output); instead, the range would be the set $$\{5, 10 \}$$. Notice that the domain in this case isn't even a set of numbers. In virtually all cases, you will be dealing with functions with numbers as both inputs and outputs, but it's important to see that there's nothing inherently numeric about the definition of a function.

In the following [image](https://upload.wikimedia.org/wikipedia/commons/6/64/Codomain2.SVG), the red area represents the domain, the blue the codomain, and the yellow the range. 

<img src="https://upload.wikimedia.org/wikipedia/commons/6/64/Codomain2.SVG" alt="domain-codomain-range" style="width: 400px;"/>


In general, subsets of $$A \times B$$ are known as **relations**. Not all relations are functions, but all functions are relations (since all functions are subsets of $$A \times B$$). Consider the following relation $$g \subset A \times B$$:

$$g = \{ (\text{"Hi"}, 5), (\text{"Hi"}, 15), (\text{"Hey"}, 15), (\text{"Hello"}, 10) \}$$

$$g$$ in this case is not a function, since it has two different outputs for the input of "Hi". 

<br>

#### Representation

In order to define a function $$f$$, we need to specify the domain, codomain, and how to _map_ elements of the domain to the codomain. We can do this in two ways:
- List out the pairs (as we did for the examples above)
- Specify a rule that describes how to get from input to corresponding output

The functions you have experience with likely all come from a subset of the latter class, that is, functions that have rules that are algebraic. However, rules need not be algebraic. Consider the following rule $$f$$, that maps positive integers to positive integers (a set we will define in the next section but take for granted now):

$$f(x) = \text{the } x^{th} \text{ smallest prime number}$$

$$f$$ is indeed a valid function, as are the various algebraic functions you have seen before: $$f(x) = x^2$$, $$g(x) = \frac{sin(x^4)}{e^{tan x}}$$, and so on. Another way of writing algebraic functions is $$f: x \mapsto x^2$$; we can even drop the $$f$$ and simply write $$x \mapsto x^2$$ if we don't need to give the function a name. This is read as "the mapping that sends $$x$$ to $$x^2$$."  This symbol is similar to the $$\rightarrow$$ we use when defining the domain and codomain of a function, but there is a subtle difference.

However, something like $$x^2 + y^2 = 1$$ is not a function, as for each $$x$$ there are two $$y$$ values, and vice versa.

Side Note: Some functions do not have _closed form representations_. A common example is $$f(x) = \int_{-\infty}^x e^{-t^2}dt$$ – this is a perfectly valid function, however there is no way to express it other than as an integral or limit of an infinite sum.

<br>

### Injections and Surjections

There are two classes of functions we will now look at.

#### Injections
We say a function $$f : A \rightarrow B$$ is injective, or **one-to-one**, if no two elements in the input have the same output. Formally we say

$$f(x_1) = f(x_2) \implies x_1 = x_2$$

or equivalently, 

$$x_1 \neq x_2 \implies f(x_1) \neq f(x_2)$$

The first of these statements says if two inputs have the same output, then the inputs must be equal. The second says if two inputs are not equal, then their outputs can't be equal.

Examples of injections are $$f(x) = e^x$$ and $$g(x) = \sqrt{x}$$, while $$f(x) = x^2$$ is not an injection over its entire domain (all real numbers), since $$-a$$ and $$a$$ both map to $$a^2$$. However, if we restrict the set of inputs to $$f : x \mapsto x^2$$ to be only non-negative real numbers (or only non-positive real numbers), then it is an injection!

**insert set diagrams**

#### Surjections
We say a function $$f : A \rightarrow B$$ is surjective, or **onto**, if every element in $$B$$ has is mapped to by an element in $$A$$. Another way of saying this is that a function is a surjection when its codomain and range are the same set (that is, all possible outputs are actually seen as outputs). Symbolically:

$$\forall \: b \in B, \: \exists \: a \in A : b = f(a)$$

$$f: x \mapsto x^2$$ is a surjection when the codomain is the set of all non-negative real numbers (and domain is the set of all real numbers), as every number greater than or equal to $$0$$ exists as an output (since all non-negative numbers have a square root). However, when the codomain is the set of all real numbers, positive and negative (and domain is still all real numbers), then $$f(x) = x^2$$ is not a surjection, as there is no real number $$x$$ such that $$x^2 = -1$$. If we let the set of positive integers be both our domain and codomain, again, $$x \mapsto x^2$$ is not a surjection, because not every positive integer is a square.

**insert set diagrams**

One way to remember the correspondence between the terms "surjection" and "onto": the _sur_ in surjective means "on" in French!

<br>

### Bijections

A function can be injective or not, and surjective or not, as we saw above. However, when a function is both injective and surjective, it also belongs to another class of functions, one with many desirable properties.

#### Definition
A function $$f$$ is bijective if and only if it is both injective and surjective. That is, a function is a bijection if and only if no two elements in the domain map to the same element in the range, and every element in the codomain has something mapping to it from the domain.

**TODO: Insert picture**

For example, if we let our domain and codomain be the set of non-negative real numbers, we have that the function given by $$x \mapsto \sqrt{x}$$ is a bijection. The map given by $$x \mapsto x^2$$ is a bijection if we use the non-negative real numbers as our domain and codomain, however if we let our domain and codomain be all real numbers, it is not a bijection.

One notion regarding sets we have yet to talk about is the size of a set, known as a set's **cardinality**. For sets of finite size, the cardinality is the number of unique elements in the set. However, for sets of infinite size, such as the set of all integers or all real numbers, cardinality becomes harder to define. What we can do, though, is determine whether or not two sets have the same cardinality. **We say two sets have the same cardinality if and only if there exists a bijection between the two sets.** This is an idea we will explore further in the following section, on the sets of numbers.  

#### Permutations

A **permutation** is a bijection whose domain and codomain are the same set. One way to think of a permutation is a "shuffling" of a set; for example, if we let our domain and codomain both be the set $$S = \{ 1, 2, 3, 4 \}$$, a permutation on this set could be the mapping given by $$f: \{ (1, 3), (2, 2), (3, 4), (4, 1) \}$$.  We will study permutations further when we deal with combinatorics. 
