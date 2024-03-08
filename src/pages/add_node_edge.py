import streamlit as st

def display_page():
    st.title("Add Node/Edge")
    st.write("This page allows users to add nodes or edges to a graph.")
    # Example form for adding a node/edge
    with st.form("add_node_edge_form"):
        node = st.text_input("Node Name")
        edge = st.text_input("Edge Connection")
        submit_button = st.form_submit_button("Add Node/Edge")
        if submit_button:
            st.write(f"Node {node} and Edge {edge} added.")
            # Add your code here to handle the addition of a node/edge