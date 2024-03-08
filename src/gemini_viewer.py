from pyvis.network import Network

def print_graph_details(graph):
    print("Nodes and their attributes:")
    for node, attrs in graph.nodes(data=True):
        print(f"{node}: {attrs}")
    
    print("\nEdges and their attributes:")
    for source, target, attrs in graph.edges(data=True):
        print(f"{source} -> {target}: {attrs}")

# Prepare the node data (with tooltips)
nodes = [
    {"id": "1", "label": "Questions", "group": 'Concept', "title": "Fundamental inquiries driving AI exploration."},
    {"id": "2", "label": "Thinking", "group": 'Concept', "title": "Critical and philosophical thinking on AI"}, 
    # ... add other nodes with unique string IDs
]

# Prepare the edge data (with tooltips) - Make sure to reference the correct node IDs
edges = [
    {"from": "1", "to": "2", "label": "Raises", "title": "Alex Doe poses this question"}, 
    # ... add other edges, ensuring 'from' and 'to' match node IDs
]


# ... (Rest of your code remains the same)

# Create the network object 
net = Network(height='600px', width='100%', directed=True)

# Customize appearance (optional)
# net.node_color_highlight = { 
#     # ... color definitions
# } 

# Add data
net.add_nodes(nodes)
net.add_edges(edges)

# Enable physics (adjust parameters as desired)
net.set_options(""" 
var options = {
  physics: {
    enabled: true, 
    barnesHut: {
      gravitationalConstant: -2000,
      centralGravity: 0.3,
      springLength: 95,
      springConstant: 0.04,
      damping: 0.09,
      avoidOverlap: 0.4
    }
  }
}
""")

 # Print the graph details
print_graph_details(G)

# Generate the visualization
net.show("qtpie_graph_dig.html")  
