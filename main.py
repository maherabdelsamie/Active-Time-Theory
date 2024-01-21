import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from sklearn.manifold import LocallyLinearEmbedding, SpectralEmbedding

def create_temporal_network(num_nodes, edge_prob=0.8):
    """Create a directed weighted graph with increased edge creation probability."""
    G = nx.DiGraph()
    for i in range(num_nodes):
        for j in range(num_nodes):
            if i != j and np.random.rand() < edge_prob:
                weight = np.random.rand()
                G.add_edge(i, j, weight=weight)
    return G





def simulate_network_dynamics(G, num_steps=5):
    """Simulate changes in the network over time."""
    for _ in range(num_steps):
        node_a, node_b = np.random.randint(0, len(G), 2)
        if G.has_edge(node_a, node_b):
            G.remove_edge(node_a, node_b)
        else:
            G.add_edge(node_a, node_b, weight=np.random.rand())


from sklearn.manifold import TSNE

def map_network_to_space(G, num_timesteps=20):
    """Map network changes to spatial evolution using t-SNE."""
    print("Mapping Network Changes to Spatial Evolution")

    previous_state = nx.to_numpy_array(G)
    coordinates = [previous_state.flatten()]

    for t in range(num_timesteps):
        simulate_network_dynamics(G)
        current_state = nx.to_numpy_array(G)
        coordinates.append(current_state.flatten())
    
    # Convert list of coordinates to NumPy array
    coordinates_array = np.array(coordinates)

    # Apply t-SNE with adjusted perplexity
    perplexity_value = min(30, num_timesteps - 1)  # Adjusting perplexity based on num_timesteps
    embedding = TSNE(n_components=3, perplexity=perplexity_value).fit_transform(coordinates_array)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    for point in embedding:
        ax.scatter(point[0], point[1], point[2], c='r', marker='o')
    ax.set_xlabel('X Axis')
    ax.set_ylabel('Y Axis')
    ax.set_zlabel('Z Axis')
    ax.set_title('Emergent Spatial Coordinates')
    plt.show()


def geometric_interpretation(G, num_timesteps=20):
    """Geometric interpretation of network dynamics."""
    print("Geometric Interpretation of Network Dynamics")
    previous_state = nx.to_numpy_array(G)
    state_trajectories = [previous_state.flatten()]
    
    for t in range(num_timesteps):
        simulate_network_dynamics(G)
        current_state = nx.to_numpy_array(G)
        state_trajectories.append(current_state.flatten())

    embedding = LocallyLinearEmbedding(n_components=3).fit_transform(state_trajectories)
    geodesic_distances = [np.linalg.norm(embedding[i+1] - embedding[i]) for i in range(len(embedding) - 1)]

    plt.figure()
    plt.plot(range(len(geodesic_distances)), geodesic_distances)
    plt.ylabel("Geodesic Distance")
    plt.xlabel("Time Step")
    plt.title("Geodesic Distance vs Time")
    plt.show()


# Run the updated function
num_nodes = 100
temporal_network = create_temporal_network(num_nodes)
map_network_to_space(temporal_network)

# Call to geometric_interpretation
geometric_interpretation(temporal_network)
plt.show()  # Show the second plot
