# The Foundations of Active Time Theory
 
## Introduction

Our understanding of the nature of time and space has been predominantly shaped by theories that treat them as a placid and inactive backdrop – an arena where the drama of existence plays out. However, the inert notion of spacetime assumed by models from classical mechanics to general relativity and quantum field theory, struggles to address some fundamental questions. How did the informational capacity for matter and physical laws actually emerge in the first place? What gave rise to the arrow of time? Did spacetime simply pop into existence or has it always existed? 

The traditional perspective, which posits the Big Bang as the commencement of time, appears illogical when considering that the Big Bang, being fundamentally a process, inherently requires the pre-existence of time for its occurrence. Without time, the very fabric of events, motion, and change ceases to exist.To overcome these profound limitations, a radically novel conceptualization of time’s essence is imperative. [The Active Time Hypothesis (ATH)](https://github.com/maherabdelsamie/Active-Time-Hypothesis2) offers such a groundbreaking shift - one that bestows time itself with generative, directive, and adaptive capacities. No longer an impassive coordinate, time assumes the role of a dynamic primordial entity, one whose intrinsic creativity breathes existence into being, while guiding and optimizing evolutionary processes.  

Three interrelated properties provide the cornerstones of ATH. The generative faculty leads time to spontaneously induce fluctuations,events and changes. In effect, time’s own ability to generate perturbations, engenders the emergence of proto-space itself. As these primal acts of creation repeat and compound, consistent patterns coalesce into the fields and systemic behaviors that manifest as physical laws. Hence, the directive property signifies time as an orchestrator nudging existence toward orderly progression rather than random meandering. Finally, recognizance of time’s adaptable pace depending on context, adds a metabolistic quality adjusting system evolution rates.  

By reconstituting time as an eternally uncertain, active essence, continuously spawning causal chains, self-organizing resonances, and probabilistic differentiation, ATH promises a profoundly more nuanced explanation for our universe’s becoming. The following sections further elucidate the mechanisms underlying these temporal capacities both conceptually and through supportive computational models.


## The Active Properties of Time

The generative faculty represents time’s inherent capacity to spontaneously induce events, fluctuations and changes – prime movers sparking the genesis of existence itself. One can envisage time’s generative impulse precipitating localized ripples that coalesce into the very notion of “where” they emerge. The beginnings of a proto-space takes shape as the canvas upon which time’s creativity crafts primordial phenomena. In a manner akin to vacuum fluctuations of quantum field theory, time kindles bursts of causal chains, weaving the earliest tapestry of occurrences.

As these acts of temporal genesis repeat, consistent behaviors and properties manifest as patterns –Order emerges from generative randomness. This phenomenon reflects time’s directive property, subtly nudging the evolutionary trajectory of events in a law-abiding manner. Such spontaneously self-organizing regularities can be perceived as the blueprints for physical laws that come to govern all existence. They determine interactions within emergent fields and phenomena, shaping matter itself. In a way, time sculpts dynamics of its own progeny via continuous feedback guiding further propagation. 

Finally, recognizance of time’s inherently context-sensitive pace introduces adaptability to this framework. Just as external factors can dilate or contract perceived duration, ATH proposes temporal flow itself can expand, slow or ripple in tune with states within the systems it generates. Such plasticity to modulate rate of occurrence-chains allows optimization of evolutionary processes, ratcheting complexity. This adaptive variability can also enable phase transitions ofeternal uncertainties into resonances and primordial information to precipitate particles. 

Positioning time as an endlessly active medium, brimming with generative tension, continuously reifying its own resonant progeny through directive laws and adaptive pacing, provides profound insight into the becoming of our cosmos. The computational models explore algorithmic encoding of said mechanisms in finer detail.

## Computational Modeling Methods

In our investigation of the Active Time Theory (ATH), we employed a computational approach, leveraging Python's robust capabilities for numerical analysis and network simulation. Our methodological framework was designed to encapsulate the generative, directive, and adaptive properties of time as stipulated by ATH. The core of our computational model is a dynamic network, constructed and evolved through a series of Python functions that algorithmically represent ATH's conceptual tenets.

### Network Creation and Evolution
We initiated our model by constructing a directed graph, representing a temporal network with nodes symbolizing computational events and weighted edges depicting causal associations. This network was not static; it evolved over time under the influence of ATH's principles, implemented through specific Python functions.

#### Generative Function:
The generative aspect of time was modeled through a function `generative_func(t)`, which introduces stochastic perturbations to the network. This function encapsulates the idea of time inducing spontaneous events, akin to quantum fluctuations. Here's the implementation:

```python
def generative_func(t):
    return S(t)

def S(t, std_dev=0.01):
    u1 = np.random.rand()
    u2 = np.random.rand()
    z0 = np.sqrt(-2.0 * np.log(u1)) * np.cos(2.0 * np.pi * u2)
    return std_dev * z0
```

#### Directive Function:
To model the directive property of time, directing the network's evolution, we used `directive_func(weight, t)`. This function adjusts the network's edge weights, signifying the influence of time in shaping the network's trajectory:

```python
def directive_func(weight, t):
    Phi = np.abs(weight)
    return G(Phi, t)

def G(Phi, t, k=0.01):
    return -k * np.abs(Phi)
```

#### Adaptive Function:
The adaptive nature of time, adjusting to the network's state, was captured through `adaptive_func(psi)`. This function reflects the concept of time altering its pace in response to the system's evolution:

```python
def adaptive_func(psi):
    return A(psi)

def A(Phi, m=0.01):
    return m * np.abs(Phi)
```

#### Network Evolution:
The network was evolved over a series of steps, during which the edge weights were adjusted by the generative and directive functions, while the overall network structure was modulated through preferential attachment, representing the adaptive function:

```python
def simulate_temporal_network(num_nodes, num_steps, edge_prob=0.5, t=0):
    G = nx.DiGraph()

    # Network Initialization
    # Creating nodes and establishing initial connections based on edge probability
    for i in range(num_nodes):
        for j in range(i + 1, num_nodes):
            if np.random.rand() < edge_prob:
                # Adding an edge with a randomly assigned weight
                G.add_edge(i, j, weight=np.random.rand())

    # Network Evolution
    for step in range(num_steps):
        # Iterating over each edge to apply the generative and directive functions
        for i, j, data in G.edges(data=True):
            # Updating the weight of the edge based on generative and directive influences
            data['weight'] += generative_func(t) + directive_func(data['weight'], t)

        # Applying the adaptive function through preferential attachment
        adaptive_func_preferential(G, m=0.01)

    return G

def adaptive_func_preferential(G, m=0.01):
    degrees = np.array([degree for node, degree in G.degree()])
    prob_dist = degrees / degrees.sum()
    selected_node = np.random.choice(list(G.nodes()), p=prob_dist)

    # Decision to add or remove an edge based on a random threshold
    if np.random.rand() < m:
        # Adding a new edge
        target_node = np.random.choice(list(set(G.nodes()) - {selected_node}))
        G.add_edge(selected_node, target_node, weight=np.random.rand())
    else:
        # Removing an existing edge
        neighbors = list(G.neighbors(selected_node))
        if len(neighbors) > 0:
            target_node = np.random.choice(neighbors)
            G.remove_edge(selected_node, target_node)
```

### Spatial Mapping and Dimensionality Reduction
To visualize and analyze the network's structural properties, we employed Principal Component Analysis (PCA). This technique reduced the high-dimensional adjacency matrix of the network to a lower-dimensional space, facilitating the interpretation of its complex structure:

```python
def map_to_spatial_coordinates(G):
    adjacency_matrix = nx.to_numpy_array(G)
    pca = PCA(n_components=3)
    transformed = pca.fit_transform(adjacency_matrix)
    return transformed, pca
```

This computational model, rooted in Python and its scientific libraries, provided a framework for exploring the intricate dynamics proposed by ATH. The implementation of generative, directive, and adaptive functions within a networked system allowed us to simulate and observe the emergent properties of a temporal network under ATH's influence. The results, as elaborated in the subsequent section, offer compelling insights into the validity and implications of ATH, showcasing the profound potential of computational methods in theoretical physics and cosmology.


## Results

Inspection of the degree distribution reveals an asymmetry, with most nodes exhibiting a modest number of connections and a select few hub nodes being disproportionately more connected. This profile indicates the emergence of scale-invariant organizational principles reminiscent of real-world networks. 

Dimensionality reduction analysis on the temporal connectivity matrix uncovers that the primary principal axes capture the preponderance of information. Significant data compression into more compact latent embeddings is achievable without appreciable loss. Thus the technique extracts the core relational encoding within the noise.

Mapping nodes into spatial coordinates based on the primary reduced dimensions unveils hallmarks of clustered small-world architectures. Densely intra-linked neighborhoods centered on hubs become visible, while sparser bridges maintain short inter-cluster paths, rather than all nodes linking homogeneously. This demonstrated capacity of self-organization into topologies matching real systems further cements plausibility.

Together, the outputs showcase ATH mechanisms manifesting complexity from simplicity. Rudimentary generative, directive and adaptive rules flower sophisticated structures displaying efficiency, resilience and evolvability - cornerstones of natural designs. The model hence provides a causally coherent explanation for the inception of order from formless unpredictability based on time’s inherent creativity.

## Discussion & Conclusion

The Active Time Hypothesis marks a seismic shift from conventional assumptions of placid spacetime passively hosting existence, to reconceptualizing time as an eternal creative essence seeding reality through intrinsic self-organization. Where dominant physics narratives rely on abstract mathematical constructs devoid of causal logic, ATH grounds our cosmos’ becoming in iterative generative, instructive and adaptive acts of temporal genesis.

Positioning unpredictive uncertainty as the cornerstone of reality readily explains the emergence of order without invoking mystical external intervention. Computationally encoding time’s capacities exposes this profound concept’s plausibility - simple stochastic equations, when composed into an evolutionary simulation, spontaneously blossom complex forms and functions. The model essentially recapitulates abiogenesis and self-assembly of order from noise.

The model outputs validate core ATH mechanisms, showcasing time’s inherent generative capacity instigating events, adapting network architectures and sculpting self-reinforcing dynamics to direct progression. PCA visualization reveals spatial coordinates emerge from purely temporal relationship data. This substantiates time as the essential substrate for dimensionality and existence itself to crystallize within. 

By reconstituting time’s essence to emphasize its perpetually active, morphing uncertainty at the heart of reality, ATH frees cosmogony from illogical infinite density singularities. An elegant framework centering temporal randomness and resonance naturally unifies quantum probabilities with relativistic continua. The arising worldview provides profound and intuitively causal explanations for our cosmos by empowering time as the eternal wellspring of being.


## Further Validation using Quantum Simulations

A study by Abdelsamie titled "[The Active Time Hypothesis: Unveiling Temporal Dynamics in Quantum Entanglement](https://github.com/maherabdelsamie/Active-Time-Hypothesis2)" constructs computational models to examine signatures of time’s active faculties in quantum contexts. Employing discrete encodings of the generative, directive and adaptive properties proposed by ATH, this work simulates a two-qutrit quantum system with and without temporal agency. 

The outputs reveal increased entanglement entropy, uncertainty and complexity emerging from time’s simulated capacities to spontaneously perturb systems and reinforce resonant dynamics. This aligns with ATH’s suggestion that time’s inherent creativity seeds not just cosmological emergence, but also distinctly quantum phenomena.

By substantiating measurable impacts of ascribing generative and instructive abilities to time even in microscopic quantum systems, this research further cements ATH’s viability as a foundational premise. The demonstration of quantum entanglement itself arising from basic algorithmic translations of time’s hypothetical properties encourages deeper interrogation of temporal dynamics’ role across scales of reality.


![1](https://github.com/maherabdelsamie/Active-Time-Hypothesis4/assets/73538221/412691d9-0563-421e-a738-fe5b41077f44)
![2](https://github.com/maherabdelsamie/Active-Time-Hypothesis4/assets/73538221/423a7d5e-af79-41c4-bf5d-546a30939737)
![3](https://github.com/maherabdelsamie/Active-Time-Hypothesis4/assets/73538221/7b17ce25-93c2-4876-88ea-bf129e1d4e1d)


---

# Installation
The simulation is implemented in Python and requires the following libraries:
- numpy
- networkx
- matplotlib
- scikit-learn
- scipy

You can install these libraries using pip:

```bash
pip install numpy
pip install networkx
pip install matplotlib
pip install scikit-learn
pip install scipy
```

### Usage
Run the simulation by executing the `main.py` file. You can modify the parameters of the simulation by editing the `main.py` file.

```
python main.py
```
## Run on Google Colab

You can run this notebook on Google Colab by clicking on the following badge:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1VEY4kIU5PembbrU_WLPmPioof58BuKoE?usp=sharing)

## License
This code is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License. - see the LICENSE.md file for details.

## Citing This Work

If you use this software, please cite it using the information provided in the `CITATION.cff` file available in this repository.
 
 
