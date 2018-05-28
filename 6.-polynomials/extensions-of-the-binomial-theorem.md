# Extensions of the Binomial Theorem

We will now look at a few extensions of the binomial theorem and the thought process we used in deriving it.

## The "Trinomial" Theorem?

What if we would like to expand something of the form ? One option is to treat either  or  as a single term, and use the binomial theorem. However, once again, we can treat this as a combinatorial problem on its own.

Suppose a general term in the expansion of  contains  s,  s and  s. Then, we must have that , since the total number of parentheses we choose from in the expansion must be exactly . We can then say the following:

The coefficient  comes from the number of ways to arrange  s,  s and  s \(think back to counting the number of permutations of MISSISSIPPI\).

### Example

Let's calculate the coefficient of the term containing  in the expansion of :

Setting , we require , with the constraints that  and . If we set  and , we satisfy the given constraints. We can use this solution as a starting point to find the remaining solutions:

* * 
We then find the general terms corresponding to each of these two triplets:

Then, in the final expansion, the term containing  is , and the coefficient of  is .

### Generalization

Note that can write the expansion of a trinomial raised to an exponent as a sum, though it is slightly less meaningful:

## The Multinomial Theorem

We can generalize this even further. Let's introduce the **multinomial coefficient**:

Under the assumption , this term is the number of ways to select one subset of size , one subset of size , ... and one subset of size  from a group of  items. Notice that with , this is the same as the binomial coefficient that we're used to.

Then:

**Question**: How many terms are in the initial sum? This corresponds to the number of non-negative integer solutions to , which is a stars-and-bars counting problem! Here we have  stars and  bins, meaning  bars, meaning we have  unique terms in the first expansion. \(Some combinations of terms may end up being the same when ,  contain common variables\).

## Product of Two Binomial Expansions

Let's switch gears. Rather than expanding from binomials to trinomials or general multinomials, what if we instead take a look at the product of two binomials, each raised to different exponents? Let's illustrate this with an example!

Let  and . Our goal will be to find the general term of the product , and determine the existence of certain terms.

First, we find the general term of each, using the index variable  for  and  for  \(these choices are arbitrary, but we need some way of differentiating the two, as you will see\). You should verify these on your own:

Now, to find the general term of the product, we take the product of the two general terms:

This tells us that the product of the th term of  and th term of  is . Since we separated our exponential bases in the individual general terms, it was easy to combine bases in the product.

We are now well equipped to answer the following questions:

* What are all terms containing  in the expansion of ?
* What is the coefficient of  in the expansion of ?

We will walk through the solution of the first problem as an example, while the latter is left as an exercise.

### Problem Setup

Using  and  as before, we want to find all terms containing . Our analysis will be similar to what it was when we looked at the expansion of trinomials. Since the exponent on  is , we are looking for all integer solutions to the following problem:

We know that the first line reduces to . One way to determine these solutions assuming the equation only contains two variables is to find the simplest solution that minimizes one variable and maximizes the other – such as  – and iteratively increase the minimum and decrease the maximum until all solutions are found.

After finding , we can reduce  by  to find . Doing so again yields  which we know is the last solution as setting  yields  which is out of the range of possible values for .

Now that we have our three solutions, our problem reduces to plugging in the values of  and  into our expanded term.

* * * 
In this example, it turned out that the exponent on  exactly matched the exponent on  – this was simply a coincidence, and plugging in arbitrary values of  and  into the general term shows that this result isn't always the case.

It should also be noted that the multiplication of these large numbers isn't exactly a skill that one needs to develop to be successful; no reasonable assessment \(at least in this course\) will ask for you to do this by hand, and leaving terms in the form  is perfectly fine.

