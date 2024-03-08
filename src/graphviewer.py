import networkx as nx
import matplotlib.pyplot as plt

# Initialize a directed graph
G = nx.DiGraph()

# Entities (nodes) to add to the graph
entities = [
    {"id": "Q1", "type": "Question", "text": "What are the ethical implications of AI in healthcare?", "category": "Ethics"},
    {"id": "I1", "type": "Individual", "name": "Alex Doe", "affiliation": "Tech Ethics Group", "interests": "Ethical AI, Data Privacy"},
    {"id": "P1", "type": "Position", "text": "AI should enhance, not replace, human decision-making in healthcare.", "presentedBy": "Alex Doe"},
]

# Relationships (edges) to add to the graph
relationships = [
    {"type": "Raises", "from": "I1", "to": "Q1"},
    {"type": "Holds", "from": "I1", "to": "P1"},
    {"type": "Supports", "from": "P1", "to": "Q1"},  # Assuming evidence is linked to the question for simplification
]

# Adding entities as nodes
for entity in entities:
    # Exclude 'type' key from the unpacking
    node_attributes = {k: v for k, v in entity.items() if k != 'type'}
    G.add_node(entity["id"], **node_attributes)

# Adding relationships as edges
for rel in relationships:
    G.add_edge(rel["from"], rel["to"], relationship=rel["type"])

# Visualizing the graph
plt.figure(figsize=(10, 8))
pos = nx.spring_layout(G)  # Positions for all nodes
nx.draw_networkx_nodes(G, pos, node_size=7000, node_color="lightblue", alpha=0.6)
nx.draw_networkx_edges(G, pos, width=2, alpha=0.5, edge_color="gray")
nx.draw_networkx_labels(G, pos, font_size=12, font_weight="bold")
edge_labels = nx.get_edge_attributes(G, 'relationship')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')
plt.title("QT-PIE Framework Knowledge Graph")
plt.axis('off')
plt.show()