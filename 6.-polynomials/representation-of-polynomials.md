# Representation of Polynomials

## Definition

A polynomial is a function that consists solely of terms of the form , where  is a non-negative integer, and  is a real number. As a function, it takes real numbers as an input and returns real numbers as outputs \(\). More formally, we define an th degree polynomial in the following way:

We say a polynomial has degree  if  is the largest power of  that has a non-zero coefficent.

, ,  and  are all examples of polynomials, of degrees 1, 2, 14 and 0, respectively. Furthermore, these are all polynomials written in **standard form** – that is, the form defined above. We will look at different representations of polynomials shortly.

The degree of a polynomial defines several of its key features, which we will investigate throughout this chapter.

## Point Representation

The first key feature is that **a polynomial of degree  is uniquely determined by a set of  points**. This is a concept you may be familiar with, in regards to a line – given any two points in the Cartesian plane, there is exactly one line \(i.e. a polynomial of degree 1\) that passes through these points. It's impossible to draw a different line that also passes through these two points. However, given just one point in the plane, there is an infinite number of points that pass through it.

This applies of polynomials of all degrees. Any three points uniquely determine a parabola \(a polynomial of degree 2\), however given any two or fewer points, an infinite number of parabolas pass through them. Any 74 points uniquely determine a polynomial of degree 73, however any 73 or fewer points have an infinite number of degree 73 polynomials passing through them.

Consider the set of points . These three points uniquely determine a degree 2 polynomial - you should verify on your own that this polynomial is . Since  is the only polynomial of degree 2 that passes through these points exactly, the set of points  is an equivalent way of representing . We call this the **point representation** of polynomials.

![](https://github.com/surajrampure/imt-decal-book/tree/fdeb8cfa411012087a4db0ea4d97745f91128a37/assets/Screen%20Shot%202018-03-13%20at%2011.00.01%20PM.png%20=%20250x)

We can easily convert between standard form and the point representation - given some degree  polynomial, we can plug in  points into it and record the  pairs  and call this our point representation. The question you may be asking, though, is how can we do the opposite - how can we find the standard form of a polynomial given the point representation, without repeated guessing and checking? How can we find that  is the polynomial defined by ? This process is called **interpolation**, and we will cover it in the following section.

## Interpolation

The question we're now investigating is, given a set of  points, how can we find the degree  polynomial that uniquely interpolates it?

Odds are, you've seen the degree 1 case before. Given two points  and , we find the slope of the line passing through the points as . We then substitute  and either of the two given points into  to solve for , giving us both coefficients. We need something more general, though, and there's no natural extension to this process.

Suppose we're given five points,  and . Since we know that we're searching for a degree 4 polynomial, we could create . Substituting each of the five points into  would give us a solvable system of 5 equations and 5 unknowns. These equations would be as follows:

However, solving this system of equations and unknowns would take quite some time. Luckily, there exists a more intuitive way to construct . Since there is only one such degree 4 polynomial that passes through these five points, both methods should \(and do\) result in the same .

### Lagrange Interpolation

Instead of trying to create  at once, let's try and create five smaller polynomials, that we can then sum to create . For each provided point ,  being the first point we were given, we want to craft a sub-polynomial  with the following properties:

* * 
In other words, sub-polynomial  should evaluate to 1 if  is passed in, and to 0 if any of the other four s are passed in \(we will see why this structure is important very soon\). We can create such a sub-polynomial, for each , as follows:

For clarity, let's calculate  and  \(corresponding to  and , respectively, as these were the first and third points given to us\).

The second-to-last step of the above expansions best illustrate why we've chosen to craft our sub-polynomials in this way; if we were to evaluate , the numerator and denominator would be exactly the same. If we were to instead evaluate  or , since  are all factors of the numerator the result would be 0.

We're almost done. We can now say that our final polynomial  is constructed as follows:

This is where the  values of each of the given points come into play. Looking at our example more closely, we have:

From the way each  was constructed, , and so on and so forth, as we expected. Doing the arithmetic yields the original polynomial, .

This entire process is known as **Lagrange Interpolation**. It is named after Lagrange, a famous French mathematician. Lagrange Interpolation is still tedious, though not nearly as tedious as the initial approach from the start of this section. You should practice this process on your own; create your own polynomial of degree , pick  points on it, and see if you can correctly reconstruct your polynomial.

It should be noted though, that mastering the arithmetic, while important, isn't the goal of learning this material. This material is presented so that you can add it to your mathematical toolbox.

