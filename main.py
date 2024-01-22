import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from scipy.stats import norm

# Step 1 - Spatial Emergence

def create_temporal_network(num_nodes, edge_prob=0.5):
    G = nx.DiGraph()
    for i in range(num_nodes):
        for j in range(num_nodes):
            if i != j and np.random.rand() < edge_prob:
                weight = np.random.rand()
                G.add_edge(i, j, weight=weight)
    return G

def simulate_network_evolution(G, num_steps, generative_func, directive_func, adaptive_func):
    for _ in range(num_steps):
        for i, j, data in G.edges(data=True):
            data['weight'] += generative_func() + directive_func(data['weight'])
        adaptive_func(G)

def map_to_spatial_coordinates(G):
    adjacency_matrix = nx.adjacency_matrix(G).todense()
    pca = PCA(n_components=3)
    transformed = pca.fit_transform(adjacency_matrix)
    return transformed, pca

def generative_func():
    return np.random.normal(loc=0, scale=0.1)

def directive_func(weight):
    k = 0.5
    return -k * weight

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

# Step 2 - Particle Generation and Tracking

class Particle:
    def __init__(self, position, momentum, mass, charge):
        self.position = position
        self.momentum = momentum
        self.mass = mass
        self.charge = charge
        self.kinetic_energy = 0.5 * mass * np.linalg.norm(momentum)**2

def generate_particles(num_particles, generative_func):
    particles = []
    for _ in range(num_particles):
        position = np.random.rand(3)
        momentum = np.random.rand(3)
        mass = np.random.rand()
        charge = np.random.choice([-1, 1])
        generative_effect = generative_func()
        particles.append(Particle(position + generative_effect, 
                                  momentum + generative_effect, 
                                  mass + generative_effect, 
                                  charge))
    return particles

def directive_interactions(particle, k=0.1):
    particle.momentum -= k * particle.momentum

def simulate_particles(particles, timesteps, generative_func, directive_func):
    momentum_history = []
    kinetic_energy_history = []

    for _ in range(timesteps):
        for p in particles:
            generative_effect = generative_func()
            p.position += p.momentum + generative_effect
            directive_func(p)
            p.kinetic_energy = 0.5 * p.mass * np.linalg.norm(p.momentum)**2
        momentum_history.append([p.momentum for p in particles])
        kinetic_energy_history.append([p.kinetic_energy for p in particles])

    return momentum_history, kinetic_energy_history

# Creating and simulating the network
num_nodes = 10
G = create_temporal_network(num_nodes)
simulate_network_evolution(G, 5, generative_func, directive_func, adaptive_func_preferential)
spatial_coordinates, pca = map_to_spatial_coordinates(G)

# Particle generation and simulation
num_particles = 10
particles = generate_particles(num_particles, generative_func)
momentum_history, kinetic_energy_history = simulate_particles(particles, 5, generative_func, directive_interactions)

# Plotting Section

# Plot 1: Node Degree Distribution
degrees = [G.degree(n) for n in G.nodes()]
plt.figure(figsize=(8, 6))
plt.hist(degrees, bins=20, density=True)
plt.title('Node Degree Distribution')
plt.xlabel('Degree')
plt.ylabel('Density')
plt.show()

# Plot 2: PCA Scree Plot
var_exp = pca.explained_variance_ratio_
cum_var_exp = np.cumsum(var_exp)
plt.figure(figsize=(8, 6))
plt.bar(range(1, len(var_exp) + 1), var_exp, alpha=0.6, align='center',
        label='Individual explained variance')
plt.step(range(1, len(cum_var_exp) + 1), cum_var_exp, where='mid',
         label='Cumulative explained variance')
plt.ylabel('Explained variance ratio')
plt.xlabel('Principal components')
plt.title('PCA Scree Plot')
plt.legend(loc='best')
plt.show()

# Plot 3: Log-Log Distribution of Edge Weights
weights = [data['weight'] for _, _, data in G.edges(data=True)]
plt.figure(figsize=(8, 6))
plt.hist(weights, bins=20, log=True, density=True)
plt.title('Log-Log Distribution of Edge Weights')
plt.xlabel('Edge Weight')
plt.ylabel('Log Density')
plt.xscale('log')
plt.yscale('log')
plt.show()

# Plot 4: Phase Space Trajectories
plt.figure(figsize=(8, 6))
for p in particles:
    plt.plot(p.position[0], p.momentum[0], marker='o')
plt.title('Phase Space Trajectories')
plt.xlabel('Position')
plt.ylabel('Momentum')
plt.show()

# Plot 5: Histogram of Interaction Events
interactions = [np.linalg.norm(p.momentum) for p in particles]
plt.figure(figsize=(8, 6))
plt.hist(interactions, bins=20)
plt.title('Histogram of Interaction Events')
plt.xlabel('Interaction Magnitude')
plt.ylabel('Frequency')
plt.show()

# Plot 6: Heatmap of Particle Density Distribution
positions = np.array([p.position for p in particles])
heatmap, xedges, yedges = np.histogram2d(positions[:, 0], positions[:, 1], bins=50)
extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]

plt.figure(figsize=(8, 6))
plt.imshow(heatmap.T, extent=extent, origin='lower')
plt.title('Heatmap of Particle Density Distribution')
plt.xlabel('X Position')
plt.ylabel('Y Position')
plt.show()

# Additional Plots

# Plot for Spatial Coordinates from Temporal Network
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(spatial_coordinates[:, 0], spatial_coordinates[:, 1], spatial_coordinates[:, 2])
ax.set_title('Spatial Coordinates from Temporal Network')
plt.show()

# Plot for Particle Position Distributions
positions = np.array([p.position for p in particles])
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(positions[:, 0], positions[:, 1], positions[:, 2])
ax.set_title('Particle Position Distributions')
plt.show()


