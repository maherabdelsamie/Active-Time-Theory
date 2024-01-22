import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from scipy.stats import norm

# Entanglement Code Functions (used in ATH Code)
def S(t, std_dev=0.01):
    u1 = np.random.rand()
    u2 = np.random.rand()
    z0 = np.sqrt(-2.0 * np.log(u1)) * np.cos(2.0 * np.pi * u2)
    return std_dev * z0

def G(Phi, t, k=0.01):
    return -k * np.abs(Phi)

def A(Phi, m=0.01):
    return m * np.abs(Phi)

# ATH Code: Modified Generative Function
def generative_func(t):
    return S(t)

# ATH Code: Modified Directive Function
def directive_func(weight, t):
    Phi = np.abs(weight)
    return G(Phi, t)

# ATH Code: Adaptive Function for Particle Simulation
def adaptive_func(psi):
    return A(psi)

# ATH Code: Preferential Attachment Function (Unchanged)
def adaptive_func_preferential(G, m=0.01):
    degrees = np.array([degree for node, degree in G.degree()])
    prob_dist = degrees / degrees.sum()
    selected_node = np.random.choice(list(G.nodes), p=prob_dist)

    if np.random.rand() < m:
        target_node = np.random.choice(list(set(G.nodes) - {selected_node}))
        G.add_edge(selected_node, target_node, weight=np.random.rand())
    else:
        if len(list(G.neighbors(selected_node))) > 0:
            target_node = np.random.choice(list(G.neighbors(selected_node)))
            G.remove_edge(selected_node, target_node)

# Function to create and simulate the temporal network
def simulate_temporal_network(num_nodes, num_steps, edge_prob=0.5, t=0):
    G = nx.DiGraph()
    for i in range(num_nodes):
        for j in range(i + 1, num_nodes):
            if np.random.rand() < edge_prob:
                G.add_edge(i, j, weight=np.random.rand())

    for _ in range(num_steps):
        for i, j, data in G.edges(data=True):
            data['weight'] += generative_func(t) + directive_func(data['weight'], t)
        adaptive_func_preferential(G)

    return G

# Function to map network to spatial coordinates
def map_to_spatial_coordinates(G):
    adjacency_matrix = nx.to_numpy_array(G)
    pca = PCA(n_components=3)
    transformed = pca.fit_transform(adjacency_matrix)
    return transformed, pca

# Creating and simulating the temporal network
num_nodes = 50
num_steps = 100
G = simulate_temporal_network(num_nodes, num_steps)
spatial_coordinates, pca = map_to_spatial_coordinates(G)

# Plotting Section
# Plot 1: Node Degree Distribution
degrees = [G.degree(n) for n in G.nodes()]
plt.figure(figsize=(10, 6))
plt.hist(degrees, bins=20, density=True)
plt.title('Node Degree Distribution')
plt.xlabel('Degree')
plt.ylabel('Density')
plt.show()

# Plot 2: PCA Scree Plot
var_exp = pca.explained_variance_ratio_
cum_var_exp = np.cumsum(var_exp)
plt.figure(figsize=(10, 6))
plt.bar(range(1, len(var_exp) + 1), var_exp, alpha=0.6, align='center',
        label='Individual explained variance')
plt.step(range(1, len(cum_var_exp) + 1), cum_var_exp, where='mid',
         label='Cumulative explained variance')
plt.ylabel('Explained variance ratio')
plt.xlabel('Principal components')
plt.title('PCA Scree Plot')
plt.legend(loc='best')
plt.show()

# Plot 3: Spatial Coordinates from Temporal Network
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(spatial_coordinates[:, 0], spatial_coordinates[:, 1], spatial_coordinates[:, 2])
ax.set_title('Spatial Coordinates from Temporal Network')
plt.show()
