# Arithmetic Sequences and Series

An **arithmetic sequence** is defined by a starting term  and a common difference . In the sequence, the difference between consecutive terms is constant \(and equal to the common difference\). For example:

is an arithmetic sequence with first term  and common difference .

Notice that the second term is the first term with the common difference added once, and the third term is the first with the common difference added twice. Then:

represents the th term in the series, assuming that we start counting at 1. \(Recall that when we studied the binomial theorem, our general term was 0-indexed\)

## Sum of an Arithmetic Sequence

### Sum of First  Natural Numbers

Before we derive the formula for an arithmetic series, i.e. the sum of an arithmetic sequence, we will look at the sum of perhaps the most naturally arithmetic series – the set of \(positive\) natural numbers!

Suppose we want to find the sum of the first  natural numbers, that is:

We can rewrite  backwards:

Notice that the first term in the top line and first term in the bottom line add to , as do the second terms, third terms, and so on and so forth. It should be noted that  is precisely the sum of the first and last terms of the sequence we are trying to sum.

You'll want to remember this formula, as it shows up in several different fields. We'll also show several other ways to prove it in Chapter 6.

### Sum of a General Arithmetic Sequence

Let's repeat the analysis above, but for an arbitrary arithmetic series. Suppose we want to find the sum of the first  terms of a series; we'll denote this as .

In the case of the natural numbers, when we added the two different forms of , the corresponding sum had  terms, each of which was . Now,  will be the sum of  terms, each of which are equal to , which is the sum of the first and last terms of the arithmetic sequence we're summing.

Therefore, the sum of the first  terms of an arithmetic sequence with first term  and common difference  is .

There is an easier way to remember this: since  is the first term and  is the last term,  represents the sum of the first and last numbers in the series. We can then also remember the formula as

Since there is a common difference between terms, the value  represents the average value of an element in the series. The sum is the result of treating the series as if each value were replaced with the average.

