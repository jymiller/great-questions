"""
This file is no longer needed. The functionality has been moved to the main app file, great-questions/src/st_app.py.
"""

import streamlit as st
import csv
import os

def load_graph_data(data_dir):
    """
    Load nodes and edges from CSV files into dictionaries for easy access.

    :param data_dir: Path to the data dir.  Expects to find a nodes.csv and edges.csv file.
    :return: Two dictionaries - nodes indexed by their IDs and edges as a list of tuples.
    """

    nodes_csv_path = os.path.join(data_dir, 'nodes.csv')
    edges_csv_path = os.path.join(data_dir, 'edges.csv')

    # Load nodes indexed by ID for quick lookup
    nodes = {}
    with open(nodes_csv_path, mode='r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            nodes[row['id']] = row

    # Load edges as a list of (from, to, title) tuples
    edges = []
    with open(edges_csv_path, mode='r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            edges.append((row['from'], row['to'], row['title']))

    return nodes, edges

def find_individuals_questions(nodes, edges):
    """
    Find and list the questions raised by individuals.

    :param nodes: Dictionary of nodes indexed by ID.
    :param edges: List of edges as tuples (from, to, title).
    :return: List of tuples (individual_name, question) representing the questions individuals are asking.
    """
    individuals_questions = []

    for edge in edges:
        if edge[2] == 'Raises':  # Checking for 'Raises' relationship
            from_node = nodes.get(edge[0])
            to_node = nodes.get(edge[1])
            if from_node and to_node and from_node['label'].startswith('Individual:') and to_node['label'].startswith('Question:'):
                individual_name = from_node['label'].replace('Individual: ', '')
                question = to_node['label'].replace('Question: ', '')
                individuals_questions.append((individual_name, question))

    return individuals_questions

def display_page():
    st.title("Show Questions")
    st.write("This page displays questions from a data source.")
    # Add your code here to fetch and display questions

    data_dir = os.getenv('DATA_DIR')
    
    nodes, edges = load_graph_data(data_dir)
    individuals_questions = find_individuals_questions(nodes, edges)

    for individual, question in individuals_questions:
        st.write(f"{individual} is asking: {question}")
