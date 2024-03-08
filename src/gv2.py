"""
This is the latest working Graph Visualization script. It fetches environment variables, loads graph data from CSV files, creates a NetworkX graph, and visualizes the graph using pyvis. The graph is saved to an HTML file and opened in a web browser for viewing.
"""
from pyvis.network import Network
import networkx as nx
import webbrowser
import os
import csv

def fetch_env_vars():
    """
    Fetch environment variables for data and project directories.
    Returns a dictionary with the environment variables if found, or raises an exception if any are missing.
    """
    data_dir = os.getenv('DATA_DIR')
    project_dir = os.getenv('PROJECT_DIR')

    if not data_dir or not project_dir:
        missing_vars = []
        if not data_dir:
            missing_vars.append('DATA_DIR')
        if not project_dir:
            missing_vars.append('PROJECT_DIR')
        raise EnvironmentError(f"Missing environment variables: {', '.join(missing_vars)}")

    return {"DATA_DIR": data_dir, "PROJECT_DIR": project_dir}

def load_graph_data_vis(data_dir):
    """
    Load graph data from CSV files located in the specified data directory.
    Returns entities and relationships as lists of dictionaries.
    """
    entities_path = os.path.join(data_dir, 'nodes.csv')
    relationships_path = os.path.join(data_dir, 'edges.csv')

    entities = []
    with open(entities_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            entities.append(row)

    relationships = []
    with open(relationships_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            relationships.append(row)
  
    # """
    # Placeholder for a function that loads graph data from files or other sources.
    # Returns hardcoded entities and relationships for demonstration purposes.
    # """
    # # This is where you'd load your data from CSV files or other data sources
    # entities = [
    #     {"id": "Q1", "label": "Question: What are the ethical implications of AI in healthcare?", "title": "Category: Ethics", "color": "#FFC300"},
    #     {"id": "I1", "label": "Individual: Alex Doe", "title": "Affiliation: Tech Ethics Group\nInterests: Ethical AI, Data Privacy", "color": "#DAF7A6"},
    #     {"id": "P1", "label": "Position: AI should enhance, not replace, human decision-making in healthcare.", "title": "Presented by: Alex Doe", "color": "#C70039"},
    # ]
    # relationships = [
    #     {"from": "I1", "to": "Q1", "title": "Raises"},
    #     {"from": "I1", "to": "P1", "title": "Holds"},
    #     {"from": "P1", "to": "Q1", "title": "Supports"},
    # ]
    return entities, relationships

def create_graph(entities, relationships):
    """
    Create and return a NetworkX graph from entities and relationships.
    """
    G = nx.DiGraph()
    print(entities)
    print(relationships)
    for entity in entities:
        G.add_node(entity["id"], label=entity["label"], title=entity["title"], color=entity["color"])
    for rel in relationships:
        G.add_edge(rel["from"], rel["to"], title=rel["title"])
    return G

def visualize_graph(G, output_file_path):
    """
    Visualize the graph G and save it to the specified HTML file.
    """
    nt = Network(notebook=False, height="750px", width="100%", bgcolor="#222222", font_color="white")
    nt.from_nx(G)
    nt.save_graph(output_file_path)
    print(f"Graph saved to {output_file_path}. Opening this file in a web browser to view the graph.")
    webbrowser.open('file://' + os.path.abspath(output_file_path))

def main():
    try:
        env_vars = fetch_env_vars()
    except EnvironmentError as e:
        print(e)
        return

    # Assuming validation has passed and environment variables are available
    output_file_path = os.path.join(env_vars['DATA_DIR'], 'knowledge_graph.html')
    data_dir = env_vars['DATA_DIR']  # Fetch the data directory from environment variables

    entities, relationships = load_graph_data_vis(data_dir)
    G = create_graph(entities, relationships)
    visualize_graph(G, output_file_path)

if __name__ == "__main__":
    main()
