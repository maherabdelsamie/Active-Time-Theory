import numpy as np
import scipy.integrate
import matplotlib.pyplot as plt
import networkx as nx

# Temporal field operator
def phi_t(E, t):
    return np.exp(1j * E * t)

# Modified energy function based on a simple harmonic oscillator model
def E(t):
    omega = 1.0
    return 0.5 * omega**2 * t**2

# Temporal wavefunction with modified integration bounds
def psi_t(t, E_func, lower_bound, upper_bound):
    try:
        integrand = lambda E: np.exp(-1j * E * t) * phi_t(E, t)
        integral_result, _ = scipy.integrate.quad(integrand, lower_bound, upper_bound)
        return integral_result
    except Exception as e:
        print(f"Integration error: {e}")
        return 0

# Central difference for discrete derivative
def central_difference(psi, t_values):
    dt = t_values[1] - t_values[0]
    return (np.roll(psi, -1) - np.roll(psi, 1)) / (2 * dt)

# Improved momentum operator using central difference
def p_operator(psi, t_values):
    return -1j * central_difference(psi, t_values)

# Position operator implementation (time itself)
def q_operator(psi, t_values):
    return t_values * psi

# Commutator [q, p] in a discrete setting
def commutator(q_op, p_op, psi, t_values):
    q_psi = q_op(psi, t_values)
    p_psi = p_op(psi, t_values)
    return q_psi * p_psi - p_psi * q_psi

# Create a weighted graph representing temporal interactions
def create_weighted_graph(n_nodes):
    G = nx.random_regular_graph(d=3, n=n_nodes)
    for u, v, d in G.edges(data=True):
        d['weight'] = np.random.rand()
    return G

# Evolve the state ψ over the network G
def evolve_state_over_network(G, psi):
    A = nx.to_numpy_array(G, weight='weight')
    return np.dot(A, psi)

# Compute a simplified version of curvature for the graph G
def compute_curvature(G):
    curvature = np.zeros(len(G))
    for node in G:
        curvature[node] = np.sum([G[node][nbr].get('weight', 1) for nbr in G[node]])
    return curvature

# Compute simplified geodesic paths in the graph G
def compute_geodesics(G, start_node):
    paths = nx.single_source_shortest_path_length(G, start_node)
    return paths

# Parameters
lower_bound = -10
upper_bound = 10
t_values = np.linspace(0, 10, 100)

# Calculate the temporal wavefunction
psi_values = np.array([psi_t(t, E, lower_bound, upper_bound) for t in t_values])

# Calculate commutator
commutator_values = commutator(q_operator, p_operator, psi_values, t_values)

# Temporal network model
G_t_weighted = create_weighted_graph(len(t_values))
evolved_psi = evolve_state_over_network(G_t_weighted, psi_values)

# Curvature and geodesics
curvature_values = compute_curvature(G_t_weighted)
start_node = 0
geodesic_paths = compute_geodesics(G_t_weighted, start_node)

# Visualization
plt.figure(figsize=(18, 10))

plt.subplot(2, 3, 1)
plt.plot(t_values, np.abs(psi_values)**2)
plt.title("Temporal Wavefunction |ψ(t)|²")
plt.xlabel("Time")
plt.ylabel("Probability")

plt.subplot(2, 3, 2)
plt.plot(t_values, np.real(commutator_values))
plt.title("Commutator [q, p]")
plt.xlabel("Time")
plt.ylabel("Commutator Value")

plt.subplot(2, 3, 3)
nx.draw(G_t_weighted, with_labels=True, node_color='blue', node_size=50, edge_color='grey')
plt.title("Weighted Temporal Network Graph")

plt.subplot(2, 3, 4)
plt.plot(t_values, np.abs(evolved_psi)**2)
plt.title("Evolved Temporal State |ψ(t)|² after Network")
plt.xlabel("Time")
plt.ylabel("Probability")

plt.subplot(2, 3, 5)
plt.plot(range(len(curvature_values)), curvature_values)
plt.title("Simplified Curvature of Temporal Network")
plt.xlabel("Node")
plt.ylabel("Curvature Value")

plt.subplot(2, 3, 6)
plt.plot(list(geodesic_paths.keys()), list(geodesic_paths.values()))
plt.title("Geodesic Paths from Node 0")
plt.xlabel("Node")
plt.ylabel("Path Length")

plt.tight_layout()
plt.show()
