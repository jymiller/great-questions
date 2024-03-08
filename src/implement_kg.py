import networkx as nx
import matplotlib.pyplot as plt
from pyvis.network import Network
import webbrowser
import os
import csv

# Attempt to fetch environment variables and test if they exist
DATA_DIR = os.getenv('DATA_DIR')
PROJECT_DIR = os.getenv('PROJECT_DIR')

# Function to validate environment variables
def validate_env_vars():
    missing_vars = []
    if not DATA_DIR:
        missing_vars.append('DATA_DIRECTORY')
    if not PROJECT_DIR:
        missing_vars.append('PROJECT_DIR')
    return missing_vars

# File paths
nodes_csv_path = os.path.join(DATA_DIR, 'nodes.csv')
edges_csv_path = os.path.join(DATA_DIR, 'edges.csv')

# Function definitions
def add_node(graph, node_id, **attrs):
    graph.add_node(node_id, **attrs)

def add_edge(graph, source, target, **attrs):
    graph.add_edge(source, target, **attrs)

def visualize_graph(graph):
    nx.draw(graph, with_labels=True)
    plt.show()

def visualize_graph_interactive(graph):
    # Create a PyVis network from the NetworkX graph
    net = Network(notebook=False, height="750px", width="100%")
    net.from_nx(graph)
    
    # Update node titles for visualization
    for node in net.nodes:
        # Retrieve node attributes from the NetworkX graph
        nx_attrs = graph.nodes[node["id"]]
        # Create a title string from attributes
        title = "<br>".join(f"{key}: {value}" for key, value in nx_attrs.items())
        # Assign title to PyVis node
        node["title"] = title

    # Update edge titles for visualization
    for edge in net.edges:
        # Retrieve edge attributes from the NetworkX graph
        nx_attrs = graph.get_edge_data(edge["from"], edge["to"])
        # Create a title string from attributes
        title = "<br>".join(f"{key}: {value}" for key, value in nx_attrs.items())
        # Assign title to PyVis edge
        edge["title"] = title

    # # Save and open the visualization in a browser
    # net.show("qt_pie_graph.html")
        
    # Instead of using net.show(), directly save the graph to an HTML file
    output_file_path = "qt_pie_graph.html"
    net.save_graph(output_file_path)
    print(f"Graph saved to {output_file_path}. Please open this file in a web browser to view the graph.")

    # Ensure the path is absolute
    absolute_file_path = os.path.abspath(output_file_path)

    # Use the webbrowser module to open the file in the default browser
    webbrowser.open('file://' + absolute_file_path)


def print_graph_details(graph):
    print("Nodes and their attributes:")
    for node, attrs in graph.nodes(data=True):
        print(f"{node}: {attrs}")
    
    print("\nEdges and their attributes:")
    for source, target, attrs in graph.edges(data=True):
        print(f"{source} -> {target}: {attrs}")

# Graph initialization
G = nx.DiGraph()

# Function to read nodes from CSV and add them to the graph
def add_nodes_from_csv(graph, csv_file_path):
    with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            graph.add_node(row['id'], **{k: v for k, v in row.items() if k != 'id'})

# Function to read edges from CSV and add them to the graph
def add_edges_from_csv(graph, csv_file_path):
    with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            graph.add_edge(row['source'], row['target'], **{k: v for k, v in row.items() if k not in ['source', 'target']})

# Main logic
def main():
    # # Example of adding nodes and edges
    # add_node(G, "Individual1", type="Individual", name="Alice", interests="Ethical AI")
    # add_node(G, "Question1", type="Question", text="What are the ethical implications of AI in healthcare?")
    # add_edge(G, "Individual1", "Question1", relationship="raises")
    
    missing_vars = validate_env_vars()
    if missing_vars:
        st.error("Missing environment variables: " + ", ".join(missing_vars) + ". Please set these variables and restart the app.")
        return   
    
    # Add nodes and edges to the graph
    add_nodes_from_csv(G, nodes_csv_path)
    add_edges_from_csv(G, edges_csv_path)



    # Print the graph details
    print_graph_details(G)

    # # Visualize the graph
    # visualize_graph(G)

    # Visualize the graph interactively
    visualize_graph_interactive(G)


# Execution guard
if __name__ == "__main__":
    main()
