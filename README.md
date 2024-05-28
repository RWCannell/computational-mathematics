## Computational Mathematics
### Bisection Method
The _Bisection Method_ is a root-finding algorithm. Consider a function `f(x)` that is continuous over the interval `[a, b]`. We begin by taking the midpoint of the interval, i.e.
```bash
c = a + (b - a)/2 = (a + b)/2
```
If `f(c) = 0`, then we've found a root and we can stop the process.   

If `f(a)*f(c) < 0`, then that means `f(a)` and `f(c)` have different signs. This means that there exists an x-value between `a` and `c` such that the function `f` evaluated at that point is zero. To get closer to that point, we shorten the interval by creating a new interval where the midpoint `c` is the new end of the interval, i.e. 
```bash
[a, b] --> [a, c]
```
If `f(a)*f(c) > 0`, then both `f(a)` and `f(c)` have the same sign, so no root exists between `[a, c]`. Since no root exists inside this interval, we construct a shorter interval where the midpoint `c` becomes the beginning of the interval, i.e.
```bash
[a, b] --> [c, b]
```
This process continues until a root is found or until the _tolerance_ has been reached. It's important to set a _tolerance_ value so that we don't end up creating an infinite loop.   

A [python script](python/bisection_method.py) has been created using the bisection method to approximate a root of a continuous function `f(x)` within the interval `[a, b]`.   