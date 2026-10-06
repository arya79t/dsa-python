# Why does sorting generally take n log n?

Think about sorting as repeatedly dividing the problem into smaller pieces, then doing work to combine them.

Eg:  8 → 4 → 2 → 1

That's: log₂(8) = 3 levels.
For n elements, that's roughly 

    log n levels.

But at each level, we still have to process all n elements.

So: work per level × number of levels

    n × log n = O(n log n)
