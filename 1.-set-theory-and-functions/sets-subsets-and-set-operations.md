# Sets, Subsets and Set Operations

In this section, we will look at the formal definition of a set, a subset, and identify various operations that act on multiple sets. We also introduce the idea of the universal set and a compliment. One notion omission is any discussion on the size of a set; we save this for the next section.

## Definition

In mathematics, a **set** is a well-defined collection of objects. By well-defined, we mean that for any object , we can easily determine whether or not  is an element \(also referred to as a "member"\) of the set. Formally, if  is a set, we write  to state that  is in the set , and  to state the opposite.

We define sets in one of two ways:

* By listing out all of the elements in the set, e.g. ,  or 
* By stating a property that determines the set, e.g.  or 

Some remarks:

* The symbols  and  both translate to "such that", and precede the condition for inclusion into a set. 
* It should be noted that sets can either have finitely many elements, as in ,  and , or infinitely many elements, as in  and  above. This is a concept we will explore further later in the chapter.

## Subsets

Given some set , another set  is a **subset** of  if and only if every element in  is also an element of . Symbolically, we represent this relationship as  \(just like with  signs, the  sign opens towards the larger set\), and it's opposite \(i.e.  is not a subset of \) as . Equivalently, we can say  is a **superset** of .

For example, if  and , we can say , but also that .

What if two sets  and  are subsets of one another – what can we infer about  and ? This would have to mean every element in  is in , and every element in  is in . It turns out that this is the exact condition for set equality. Formally, we can say two sets  and  are **equal** if and only if both  and ; in this case we could also write .

All sets are subsets of themselves. We say set  is a **proper subset** of  when  and .

## Set Operations

We will now look at four operations that act on multiple sets – union, intersection, difference and product. Note that these operations are all **closed**, meaning that the results are all also sets \(as opposed to being elements of sets, or numbers, or anything else\).

### Union

The **union** of two sets  is the set of everything contained by either  or . Formally:

For example, if  and , . Note that even though there was a 7 in both sets, the 7 is not repeated within the set. It is also worth noting that finite sets need not necessarily be ordered; we could equivalently write  and .

For any set :

*  \(Justification: \)
*  \(Justification: \)

### Intersection

The **intersection** of two sets  is the set of everything contained in both  and . Formally:

Using the same examples as before, .

For any set :

*  \(Justification: \)
*  \(Justification: \)

If , we say  and  are **disjoint** – they share no elements.

### Difference

The **difference** of two sets  is the set of everything contained in  but not contained in . Formally:

With our example, . Notice that the difference operation is the first set operation that we've studied in which the other matters.  and , but  – unlike the union and intersection, the difference operation is not **symmetric**.

### Cartesian Product

The **Cartesian product** of two sets  is the set of all possible combinations of one element in  and one element in . Quite literally:

Let's use a smaller example – let  and . Then, we have

Notice that the Cartesian product is also not symmetric – if we instead looked at , each of the ordered pairs in the set above would be flipped.

While we only defined the above set operations on two sets, since the result of any of these operations is also a set, we can combine these operations in any way we want. For example,  can be thought of as , or . We can't assign parentheses as arbitrarily when we combine operations, though:  in general.

Note on vector spaces: Algebraic vector spaces are actually defined by a Cartesian product, of the real numbers. The symbol  refers to the Cartesian product of the set of real numbers \(which we have yet to define\) with itself  times, i.e. the set of all real-valued vectors with  elements.

## The Complement

Often when dealing with sets, we work relative to some _universal_ set, which contains all relevant objects. For example, when choosing three students from a class of thirty, the set of all students in the class refers to the universe, and any particular subset of three students we choose can denote our set of interest. Using a numerical example, if we let the universe be , any set  we deal with will be a subset of .

Suppose . Sometimes, we want to consider the set of elements that are **not** in  – this is known as the **complement** of . Without a universe, this is impossible to quantify, but with a universe this is quite easy. In our case, the complement of  \(denoted ,  or \) is . In general:

### De Morgan's Laws

We can actually combine the idea of the complement of a set with the union and intersection operations, by **De Morgan's Laws**, as follows:

* * 
Since we have yet to cover formal proof techniques, we save the proof for Chapter 3. However, it should be noted that De Morgan's Laws allow us to convert from a union to an intersection, and vice versa.

Let's work out an example as a sanity check. Suppose again that ,  and . Then:

You should work out the second case on your own, and verify that it works.

