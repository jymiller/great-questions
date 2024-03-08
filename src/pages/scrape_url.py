import streamlit as st

def display_page():
    st.title("Scrape URL")
    st.write("This page allows users to scrape data from a specified URL.")
    # Example input for URL
    url = st.text_input("Enter the URL to scrape")
    scrape_button = st.button("Scrape")
    if scrape_button:
        st.write(f"Scraping data from: {url}")
        # Add your code here to perform the web scraping