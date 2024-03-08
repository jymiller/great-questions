import streamlit as st
import os
from pages import show_questions, add_node_edge, scrape_url

# Attempt to fetch environment variables and test if they exist
DATA_DIR = os.getenv('DATA_DIR')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
PROJECT_DIR = os.getenv('PROJECT_DIR')
image_path = os.path.join(PROJECT_DIR, 'images', 'overview_image.png')

# Function to validate environment variables
def validate_env_vars():
    missing_vars = []
    if not DATA_DIR:
        missing_vars.append('DATA_DIRECTORY')
    if not OPENAI_API_KEY:
        missing_vars.append('OPENAI_API_KEY')
    if not PROJECT_DIR:
        missing_vars.append('PROJECT_DIR')
    return missing_vars

# Main app function
def main():
    missing_vars = validate_env_vars()
    if missing_vars:
        st.error("Missing environment variables: " + ", ".join(missing_vars) + ". Please set these variables and restart the app.")
        return

    # Sidebar for navigation
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ('Overview', 'Show Questions', 'Add Node/Edge', 'Scrape URL'))

    # Display the appropriate page
    if page == 'Overview':
        display_overview()
    elif page == 'Show Questions':
        show_questions.display_page()
    elif page == 'Add Node/Edge':
        add_node_edge.display_page()
    elif page == 'Scrape URL':
        scrape_url.display_page()

def display_overview():
    """Function to display the overview of the application."""
    st.title("Great Questions")
    st.image(image_path, use_column_width=True)
    st.write("""
        This application provides a front-end interface to various functionalities:
        - **Show Questions**: Display questions from a data source.
        - **Add Node/Edge**: Allow users to add nodes or edges to a graph.
        - **Scrape URL**: Scrape data from a specified URL.
        """)

if __name__ == "__main__":
    main()
