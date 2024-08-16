## Learning Notes:

### Terminologies:
-Node Adaptive Learning
-Optimal Transport
-Wasserstein Distance

### Notes:
- Wasserstein Distance
    -> Essentially a distance function measuring distance between 2 probability functions using some metric space M (definition)
    -> Sort of like moving a pile of dirt onto another pile
    -> A distribution can be thought of as a collection of vertical strips/bars and our task is to move each bar of one distribution
        to another using minimum effort -> This is Wasserstein Distance.
    -> \[
W_p(\mu, \nu) := \left( \inf_{\gamma \in \Gamma(\mu, \nu)} \int_{M \times M} d(x, y)^p \, d\gamma(x, y) \right)^{\frac{1}{p}},
\]
