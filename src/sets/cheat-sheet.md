<title>Sets and Logic Cheat Sheet – IMT DeCal</title>

# Sets and Logic Cheat Sheet

_by Sagnik Bhattacharya, Suraj Rampure_<br>
_Last modified: March 21, 2019_

---

<br>

This chart summarizes all of the notation we've seen so far regarding sets, functions, and propositional logic.

<br>

<div align=center>

| **Symbol**  | **Name** | **Description** | **Example** | 
| ---          | ---        | ---             | ---         | 
| $$\\{ \\}$$ | set | used to define a set | $$S = \\{ 1, 2, 3, 4, ... \\}$$|
| $$\\in$$      | in, element of | used to denote that an element is part of a set | $$1 \\in {1, 2, 3}$$ |
| $$\\not \\in$$ | not in, not an element of | used to denote than an element is not part of a set | $$4 \\not \\in {1, 2, 3}$$ | 
| $$\\mid S \\mid$$ | cardinality | used to describe the size of a set (refers to the number of unique elements if the set is finite) | $$S = \\{1, 2, 2, 2, 3, 4, 5, 5 \\}$$<br> $$\\mid S \\mid = 5$$ |
| $$:$$, $$\\mid$$ | such that | used to denote a condition, usually in set-builder notation or in a mathematical definition | $\\{x^2 : x + 3 \\text{ is prime}\\}$ | 
| $$\\subseteq$$ | subset | set $$A$$ is a subset of set $$B$$ when each element in $$A$$ is also an element in $$B$$ | $$A = \\{ 1, 2 \\}$$ <br> $$B = \\{ 2, 1, 4, 3, 5 \\}$$ <br> $$A \\subseteq B$$ | 
| $$\\subset$$ | proper subset | set $$A$$ is a proper subset of set $$B$$ when each element in $$A$$ is also an element in $$B$$ **and** $$A \\neq B$$ | $$A = \\{ 1, 2, 3, 4, 5 \\}$$ <br> $$B = \\{ 2, 1, 4, 3, 5 \\}$$ <br> $$A \\subseteq B$$ is true but $$A \\subset B$$ is not true | 
| $$\\supseteq$$ | superset | set $$A$$ is a superset of set $$B$$ when $$B$$ is a subset of $$A$$ | $$A = \\{ 2, 4, 6, 7, 8 \\}$$ <br> $$B = \\{ 2, 4, 8 \\}$$ <br> $$A \\supseteq B$$ | 
| $$\\cup$$ | union | a set with the elements in set $$A$$ **or** in set $$B$$ | $$A = \\{1, 2\\}$$ <br> $$B = \\{2, 3, 5\\}$$ <br> $$A \\cup B = \\{1, 2, 3, 5\\}$$ |
| $$\\cap$$ | intersection | a set with the elements in set $$A$$ **and** in set $$B$$ | $$A = \\{1, 2\\}$$ <br> $$B = \\{2, 3, 5\\}$$ <br> $$A \\cap B = \\{2\\}$$ |
| $$\\emptyset$$ | the empty set | the set with no elements | $$\\{1, 2, 3\\} \\cap \\{4, 5, 6\\} = \\emptyset$$ |
| $$-$$, $$\\backslash$$ | set difference | elements in set $$A$$ that are not in $$B$$ | $$A = \\{1, 2, 3, 4\\}$$ <br> $$B = \\{2, 3, 5, 8\\}$$ <br> $$A - B = \\{1, 4\\}$$ <br> $$B - A = \\{5, 8\\}$$ |
| $$\\times$$ | Cartesian product | a set containing all possible combinations of one element from $$A$$ and one element from $$B$$ | $$A = \\{1, 2\\}$$ <br> $$B = \\{3, 4\\}$$ <br> $$A \\times B = \\{(1, 3), (2, 3), (1, 4), (2, 4)\\}$$ <br> $$B \\times A = \\{(3, 1), (3, 2), (4, 1), (4, 2)\\}$$ |
| $$A^c$$ | complement | a set containing the elements of the universe $$U$$ that are not in set $$A$$ | $$U = \\{1, 2, 3, 4, 5\\}, A = \\{2, 4\\} \\implies A^c=\\{1, 3, 5\\}$$
| $$f : A \\rightarrow B$$ | function | the function $$f$$ maps elements of the set $$A$$ to elements of the set $$B$$; $$A$$ is the domain and $$B$$ is the codomain | $$f(x) = x^2+5$$ is an example of a function $$f : \\mathbb{R} \\rightarrow \\mathbb{R}$$ |
| $$f : x \\mapsto x^3$$ | mapping/function | the function maps any $$x$$ to $$x^3$$; this notation refers to elements of sets rather than sets themselves | $$f(x) = x^2+5$$ can be written as $$f: x \\mapsto x^2+5$$ |
| $$\\mathbb{N}$$ | the set of natural numbers | the set of naturals numbers starting at $$1$$ | $$\\mathbb{N} = \\{1, 2, 3, ...\\}$$ |
| $$\\mathbb{N}_0$$ | the set of whole numbers | the set of whole numbers starting at $$0$$ | $$\\mathbb{N}_0 = \\{0, 1, 2, 3, ...\\}$$ |
| $$\\mathbb{Z}$$ | the set of integers | the union of the whole numbers with their negatives | $$\\mathbb{Z} = \\{..., -3, -2, -1, 0, 1, 2, 3, ...\\}$$ |
| $$\\mathbb{Q}$$ | the set of rational numbers | the set of all possible combinations of one integer divided by another, with the latter integer being non-zero, i.e., $$\\mathbb{Q} = \\{ \\frac{p}{q} : p, q \\in \\mathbb{Z}, q \\neq 0\\}$$ | $$\\{\\frac{1}{2}, \\frac{5}{14}, \\frac{-17}{3}\\} \\subset \\mathbb{Q}$$ | 
| $$\\wedge$$ | conjunction/and | $$P \\wedge Q$$ is true if both $$P$$ **and** $$Q$$ are true | if $$P = (2 \\text{ is prime}), Q = (8 \\text{ is a perfect cube})$$ then $$P \\wedge Q$$ is true |
| $$\\vee$$ | disjunction/or | $$P \\vee Q$$ is true if either $$P$$ **or** $$Q$$ is true | if $$P = (2 \\text{ is prime}), Q = (4 \\text{ is a perfect square})$$ then $$P \\vee Q$$ is true |
| $$\\neg$$ | negation | $$\\neg P$$ is true if $$P$$ is false and vice versa | if $$P = (\\text{35 is prime})$$ then $$\\neg P$$ is true |
| $$\\implies$$ | implication | $$P \\implies Q$$ means that $$Q$$ is true whenever $$P$$ is true (but it does **not** say anything about what happens when $$P$$ is false) | if $$P = (x \\text{ is divisible by 4})$$, $$Q = (x \\text{ is even})$$ then $$P \\implies Q$$ (but note that $$P \\nrightarrow Q$$) |
| $$\\iff$$ | if and only if (iff) | $$P \\implies Q$$ **and** $$Q \\implies P$$ | if $$P = (\\text{it is new year})$$ and $$Q = (\\text{it is January 1})$$ then $$P \\iff Q$$ |
| $$\\forall$$ | for all | refers to all the elements in a set | if $$A = \\{2, 4, 10\\}$$ then $$x \\in \\mathbb{N} \\text{ } \\forall x \\in A$$ |
| $$\\exists$$ | there exists | refers to the existence of at least one of something | $$\\exists x \\in \\mathbb{N}_0 : x = -x$$ | 
| $$\\oplus$$ | XOR | either $$P$$ is true or $$Q$$ is true but not both | if $$P = (\\text{Donald Trump is a Democrat})$$ and $$Q = (\\text{Hillary Clinton is a Democrat})$$ then $$P \\oplus Q$$ is true, but if $$P = (\\text{Donald Trump is a Republican})$$ then $$P \\oplus Q$$ is false |

</div>
