# great-questions
# Project Overview

**Goal:** The primary goal is to build a web-based application that identifies interesting questions from discussions on web pages. This tool will serve as a proof of concept demonstrating capabilities in Python, Streamlit, and integrating advanced concepts such as knowledge graphs and generative AI. The project will also explore enterprise data cataloging techniques for organizing and managing the information gathered from the web.

## Testing Git Action now!

This is a test of updating this README and pushing it back to repo
Let's see what happens...

## Architecture Diagram

![Architecture Diagram](/images/gq-diag.webp)

Please refer to the simplified, decluttered 2D architecture diagram previously provided. This diagram visually represents the structured organization of the application's components and the data flow between them.

## Components Description

### 1. User Interface (Streamlit App)
Allows users to input a URL for analysis and displays identified questions, summaries, and knowledge graph visualizations.
   
### 2. Web Scraping Module
Fetches and extracts content from the provided URL using components:
   - Webpage Fetcher
   - Content Extractor

### 3. NLP Module
Processes the extracted text to identify questions and generate summaries. It includes:
   - Question Identifier
   - Summarization Tool
   - Entity Recognition (for knowledge graph integration)

### 4. Knowledge Graph
Visualizes relationships between entities identified in the content. It consists of:
   - Graph Database
   - Visualization Tool

### 5. Cataloging System
Organizes and classifies web pages and reports into a structured catalog. It encompasses:
   - Database for metadata
   - Classification System
   - Management UI

### 6. CI/CD Pipeline (GitHub Actions)
Automates testing, building, and deployment processes.

## Required Technologies

- **Streamlit:** For building the user interface.
- **Beautiful Soup and Requests:** For web scraping functionalities.
- **NLTK or spaCy:** For natural language processing tasks.
- **Neo4j or NetworkX:** For creating and managing the knowledge graph.
- **SQLite/PostgreSQL:** For the cataloging system's database.
- **GitHub Actions:** For CI/CD pipeline automation.
- **Docker:** For containerization and deployment.

## Development Plan

1. **Set Up Development Environment:** Install required technologies and set up a GitHub repository with CI/CD using GitHub Actions.
   
2. **Build the Web Scraping Module:** Implement fetching and content extraction functionalities to process URLs input by users.

3. **Develop the NLP Module:** Create the logic for identifying questions and generating summaries from the extracted content.

4. **Implement the Knowledge Graph:** Integrate entity recognition from the NLP module to populate the knowledge graph with entities and their relationships.

5. **Create the Cataloging System:** Develop the database schema and UI for managing the catalog of web pages and reports, incorporating classification and organization logic.

6. **User Interface Development:** Build the front end using Streamlit, incorporating functionality for users to input URLs, and display questions, summaries, and knowledge graph visualizations.

7. **Integration and Testing:** Integrate all components, ensuring data flows correctly between modules. Perform comprehensive testing to identify and fix issues.

8. **Deployment:** Containerize the application using Docker and deploy it using a suitable cloud service provider or Streamlit Sharing.

9. **Documentation and Feedback:** Document the application's functionality, setup, and usage instructions. Gather user feedback for future enhancements.
