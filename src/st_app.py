import streamlit as st
import os
import openai
import webbrowser
import csv
import requests
from bs4 import BeautifulSoup 
import networkx as nx
from pyvis.network import Network
from PIL import Image
from pages import show_questions, add_node_edge, scrape_url
# Load your API key from an environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")


# Attempt to fetch environment variables and test if they exist
DATA_DIR = os.getenv('DATA_DIR')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
PROJECT_DIR = os.getenv('PROJECT_DIR')
image_path = os.path.join(PROJECT_DIR, 'images', 'overview_image.png')
data_dir = os.getenv('DATA_DIR')

# Function to validate environment variables
def validate_env_vars():
    missing_vars = []
    if not DATA_DIR:
        missing_vars.append('DATA_DIR')
    if not OPENAI_API_KEY:
        missing_vars.append('OPENAI_API_KEY')
    if not PROJECT_DIR:
        missing_vars.append('PROJECT_DIR')
    return missing_vars

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
    return entities, relationships

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

def display_overview():
    """Function to display the overview of the application."""
    st.title("Great Questions")
    st.write("""
        Welcome to the Great Questions app! This app is a demonstration of a knowledge graph application that allows users to interact with a graph of questions, individuals, and their relationships. The app provides a front-end interface to various functionalities, including displaying questions, adding nodes or edges to the graph, and scraping data from a specified URL.
        """)
    
    # Load and display an image
    
    try:
        image = Image.open(image_path)
    except Exception as e:
        print(e)  # This will print the error message if the image cannot be opened

    # Resize by height while maintaining the aspect ratio
    target_height = 500
    aspect_ratio = image.width / image.height
    new_width = int(target_height * aspect_ratio)
    image = image.resize((new_width, target_height))
    # st.image(image_path, use_column_width=True)
    # st.image(image, height=400)
    st.image(image)

    st.write("""
        This application provides a front-end interface to various functionalities:
        - **Show Questions**: Display questions from a data source.
        - **Add Node/Edge**: Allow users to add nodes or edges to a graph.
        - **Scrape URL**: Scrape data from a specified URL.
        """)

def show_questions():
    st.title("Show Questions")
    st.write("This page displays questions from a data source.")
    # Add your code here to fetch and display questions

    data_dir = os.getenv('DATA_DIR')
    
    nodes, edges = load_graph_data(data_dir)
    individuals_questions = find_individuals_questions(nodes, edges)

    for individual, question in individuals_questions:
        st.write(f"{individual} is asking: {question}")


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
 
def show_vis():
 
    # Assuming validation has passed and environment variables are available
    output_file_path = os.path.join(data_dir, 'knowledge_graph.html')
    print(data_dir)
    entities, relationships = load_graph_data_vis(data_dir)
    G = create_graph(entities, relationships)
    visualize_graph(G, output_file_path)

# -------------------
# Web Scraping Section
# -------------------
def fetch_page(url):
    """Fetch the HTML content of the specified URL"""
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError if the response status code is 4XX/5XX
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None

# -------------------
# Parsing Section
# -------------------
def parse_content(html_content):
    """Parse the fetched HTML content and extract relevant information"""
    # Example: extracting all paragraph texts
    soup = BeautifulSoup(html_content, 'html.parser')
    paragraphs = [p.text for p in soup.find_all('p')]
    return paragraphs

def extract_questions(text):
    """
    Uses OpenAI's API to extract questions from the given text.
    """
    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",  # Adjust according to the latest available models
            messages=[
#                {"role": "system", "content": "You are a helpful assistant."},
                 {"role": "system", "content": "You are a helpful assistant."},

                # {"role": "user", "content": f"Extract all questions from the following text: {text}"}

                # This prompt was generated through some back and forth with ChatGPT 3.5 and 4.0.  V4.0 refined the prompt to work with V3.5  which is cool
                 {"role": "user", "content": f"Please read the provided article and extract only the direct questions that are aimed at prompting reflection or strategic thinking about an organization's future, capabilities, market adaptation, and service personalization. Focus on questions that challenge the reader to consider how advancements in AI could transform their organizational strategies, enable new possibilities, broaden their market reach, or enhance customization and personalization efforts. Ignore any direct questions that do not directly relate to these themes.: {text}"}
            ]
        )
 #       extracted_text = response.choices[0].message["content"]
#        extracted_text = response["choices"][0]["message"]["content"]
        extracted_text = response.choices[0].message.content
        return extracted_text.strip()
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def scrape_question_page():
    """"Function to scrape the question page"""
    # Define the URL of the page you want to scrape
    st.title("Scrape URL")
    st.write("This page allows users to scrape data from a specified URL.")
    # Example input for URL
    url = st.text_input("Enter the URL to scrape")
    scrape_button = st.button("Scrape")
    if scrape_button:
        st.write(f"Scraping data from: {url}")
    # Add your code here to perform the web scraping
    
    # Step 1: Fetch the page
    html_content = fetch_page(url)

    if html_content:
        # Step 2: Parse the page
        extracted_data = parse_content(html_content)

        # Step 3: Process the extracted data (TODO)
        # This is where you might save data to a file, analyze it, or perform other processing.
        # For demonstration, we'll just print the extracted paragraph texts.
        for paragraph in extracted_data:
            st.write(paragraph)

    questions = extract_questions(extracted_data)
    st.write("Extracted Questions:")
    st.write(questions)
           


# Main app function
def main():
    missing_vars = validate_env_vars()
    if missing_vars:
        st.error("Missing environment variables: " + ", ".join(missing_vars) + ". Please set these variables and restart the app.")
        return

    # Sidebar for navigation
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ('Overview', 'Show Questions', 'Show Visualization', 'Scrape URL'))

    # Display the appropriate page
    if page == 'Overview':
        display_overview()
    elif page == 'Show Questions':
        show_questions()
    elif page == 'Show Visualization':
        show_vis()
    elif page == 'Scrape URL':
        scrape_question_page()
        
if __name__ == "__main__":
    main()
