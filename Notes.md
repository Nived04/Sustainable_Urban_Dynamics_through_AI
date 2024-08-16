## Learning Notes:

### Terminologies:
-Node Adaptive Learning
-GCN (Graph Convolutional Network)
-Optimal Transport
-Wasserstein Distance

### Notes:
**Graph Attention Networks (GATs)**
- **Concept**: GATs are a type of neural network used to analyze graphs by focusing on the importance of connections between nodes.
- **Intuitive Explanation**:
  - Imagine a graph as a network of friends, where each node (person) is connected to others.
  - To predict something about a node, GATs don't just consider all connections equally. Instead, they assign different levels of importance (or "attention") to each connection.
  - The importance of each connection is not predefined; it's learned during the training process using a neural network, allowing the model to adjust how much attention one node pays to another based on their features.
  - The attention mechanism uses **softmax** normalization to ensure that all attention scores add up to 1, similar to distributing a pie fairly among friends.
  - The attention weights are not computed using a simple dot product (as in some other models). Instead, they're learned through a small neural network, often a convolutional one, making the model more flexible and powerful.


**Wasserstein Distance**
- **Definition**: A distance function measuring the difference between two probability distributions using some metric space \( M \).
- **Intuitive Explanation**: 
  - Think of it as moving a pile of dirt from one location to another.
  - Each distribution can be visualized as a collection of vertical strips or bars. The task is to move each bar of one distribution to match another distribution using the minimum effort.
  - This effort required to move the "dirt" from one pile to another is what we call the Wasserstein Distance.
- **Mathematical Expression**:
  $$
  W_p(\mu, \nu) := \left( \inf_{\gamma \in \Gamma(\mu, \nu)} \int_{M \times M} d(x, y)^p \, d\gamma(x, y) \right)^{\frac{1}{p}},
  $$
  where \( \Gamma(\mu, \nu) \) represents the collection of all measures on \( M \times M \) with marginals \( \mu \) and \( \nu \) on the first and second factors respectively. This set \( \Gamma(\mu, \nu) \) is also known as the set of all **couplings** of \( \mu \) and \( \nu \).
  

