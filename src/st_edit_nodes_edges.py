import streamlit as st
import pandas as pd
import os

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

missing_vars = validate_env_vars()
if missing_vars:
    st.error("Missing environment variables: " + ", ".join(missing_vars) + ". Please set these variables and restart the app.")

# File paths
nodes_file_path = os.path.join(DATA_DIR, 'nodes.csv')
edges_file_path = os.path.join(DATA_DIR, 'edges.csv')

# Helper functions for CSV operations
def read_csv_data(file_path):
    return pd.read_csv(file_path) if os.path.isfile(file_path) else pd.DataFrame()

def save_csv_data(df, file_path):
    df.to_csv(file_path, index=False)

def validate_env_vars():
    # Add your validation logic here
    pass

# Initialize the app
st.title("Knowledge Graph Editor")



# Load existing data into DataFrames
nodes_df = read_csv_data(nodes_file_path)
edges_df = read_csv_data(edges_file_path)

# Display editable DataFrames with st.dataframe for a spreadsheet-like experience
st.subheader("Nodes")
nodes_display = st.dataframe(nodes_df)
st.subheader("Edges")
edges_display = st.dataframe(edges_df)

# Function to update DataFrame based on user input and save
def update_and_save_df(new_data, df, file_path, df_display):
    if not new_data.empty:
        updated_df = pd.concat([df, new_data], ignore_index=True)
        save_csv_data(updated_df, file_path)
        df_display.dataframe(updated_df)  # Update displayed DataFrame
        st.success("Data saved successfully!")

# Forms for adding new nodes and edges
with st.form("new_node"):
    st.subheader("Add New Node")
    new_node_data = {
        'id': st.text_input("Node ID"),
        'type': st.text_input("Type"),
        'name': st.text_input("Name"),
        'interests': st.text_input("Interests")
    }
    submit_node = st.form_submit_button("Add Node")
    if submit_node and new_node_data['id'] and new_node_data['type']:
        new_node_df = pd.DataFrame([new_node_data])
        update_and_save_df(new_node_df, nodes_df, nodes_file_path, nodes_display)

with st.form("new_edge"):
    st.subheader("Add New Edge")
    new_edge_data = {
        'source': st.text_input("Source Node ID", key="edge_source"),
        'target': st.text_input("Target Node ID", key="edge_target"),
        'relationship': st.text_input("Relationship", key="edge_relationship")
    }
    submit_edge = st.form_submit_button("Add Edge")
    if submit_edge and new_edge_data['source'] and new_edge_data['target']:
        new_edge_df = pd.DataFrame([new_edge_data])
        update_and_save_df(new_edge_df, edges_df, edges_file_path, edges_display)
