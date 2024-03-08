import graph_tool.all as gt

# Courtesy of Gemini
#  - This never worked!!


# Create the graph
g = gt.Graph(directed=True)

# Vertex properties (for labels and types)
vprop_label = g.new_vertex_property("string")
vprop_type = g.new_vertex_property("string")
g.vertex_properties["label"] = vprop_label
g.vertex_properties["type"] = vprop_type

# Add nodes
concept_nodes = {}  # Store concept nodes for easy reference
nodes = [
    ("Questions", "Concept"), ("Thinking", "Concept"), ("Positions", "Concept"), 
    ("Individuals", "Concept"), ("Evidence", "Concept"),
    ("What are the ethical implications of AI in healthcare?", "Question"),
    ("Alex Doe", "Individual"),
    ("AI should enhance, not replace...", "Position") 
]

for label, type_ in nodes:
    v = g.add_vertex()
    vprop_label[v] = label
    vprop_type[v] = type_
    if type_ == "Concept":
        concept_nodes[label] = v 

# Add Edges
edges = [
    ("Alex Doe", "What are the ethical implications of AI in healthcare?", "Raises"),
    ("What are the ethical implications of AI in healthcare?", "Thinking", "Explores"),
    ("Alex Doe", "AI should enhance, not replace...", "Holds"),
    # ... Add more edges 
]

# for src_label, tgt_label, edge_type in edges:
#     src_vertex = next((v for v, l in g.vertices() if vprop_label[v] == src_label), None)
#     tgt_vertex = next((v for v, l in g.vertices() if vprop_label[v] == tgt_label), None)
#     if src_vertex and tgt_vertex:
#         g.add_edge(src_vertex, tgt_vertex)  # Create the edge

# ... previous code 

for src_label, tgt_label, edge_type in edges:
    src_vertex = g.vertices()  # Get the vertex (assuming only one)
    if src_vertex:  
        src_vertex = next((v for v, l in [src_vertex] if vprop_label[v] == src_label), None)  # Wrap in a list
        # ... rest of the edge creation logic


# Basic Visualization
gt.graph_draw(
    g, 
    vertex_text=g.vertex_properties["label"], 
    vertex_font_size=9,
    vertex_fill_color=g.vertex_properties["type"],  # Color by type
    output_size=(600, 600), 
    output="qtpie_graph.png"
) 
