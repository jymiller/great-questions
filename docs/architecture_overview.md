# Project Architecture Overview

This document provides an overview of the project's architecture, including the major components and the flow of data through the system.

## Components and Data Flow

~~~

[Web Sources]
     |
     v
[Web Scraping Module] ---> [Scraped Text Files]
     |                           |
     | (reads- future)           | (processes)
     |                           v
     +----------------> [LLM Model] --->[Extracted Nodes and Edges Files]
                                                |
                                                | (integrates)
                                                v
                                        [Knowledge Graph] ---> [Graph Visualization] (future - graph db)
                                                |                   |
                                                | (queries)         | (displays)
                                                |                   v
                                                +------------> [Streamlit Application] ---> [User Interface]

~~~

### Web Sources

The origins of the data you intend to scrape.

### Web Scraping Module

Responsible for fetching web pages and extracting relevant content. The output is typically stored as text files or directly passed as input to the next processing stage.

### Scraped Text Files

Intermediate storage for scraped data, allowing for asynchronous processing and analysis.

### LLM Model

Processes the scraped text to perform specific tasks such as extracting nodes and edges for QT-PIE (Questions, Thinking, Positions, Individuals, Evidence) framework. The output is a nodes file and an edges file representing the extracted information.

### Knowledge Graph

An advanced data structure to represent extracted information in a graph format, showing entities and their interrelations. This layer involves integrating processed data into a graph database.

### Knowledge Graph Visualization

Uses KG to generate an interactive visualization.

### Graph Database (future)

Stores the knowledge graph, facilitating efficient queries and data retrieval for analysis or visualization.

### Streamlit Application

A Python-based app that queries the knowledge graph and displays the results. The app serves as the user interface for interacting with the processed data.

### User Interface

The front end presented to the end-user, built using Streamlit, displaying the extracted and processed data from the knowledge graph.

## Data Flow Description

- Data flows from web sources through the scraping module, which reads and processes web content.
- The scraped content is either stored for later processing or directly passed to the LLM Model.
- The LLM model processes the text to extract meaningful information and integrates this data into the knowledge graph.
- The knowledge graph structures this information within a graph structure, making it accessible for visualization.
- The Streamlit application interfaces with the graph structre to retrieve and display processed data to the end-user through a web interface.

This overview provides a high-level understanding of the system's architecture and the integration of its components.

