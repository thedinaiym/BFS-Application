# Mini Site: Introduction to BFS 🚀
## Welcome to the Mini Site: Introduction to BFS project! This interactive application, built with Streamlit, demonstrates the Breadth-First Search (BFS) algorithm in a fun and engaging way. Enjoy exploring graphs and learning about BFS through interactive visualizations! 🎉

## What is BFS? 🤔
Breadth-First Search (BFS) is a graph traversal algorithm that starts at a selected node and explores all of its immediate neighbors first, then moves on to their neighbors, and so on. BFS is widely used in various applications such as:

### Shortest Path Finding: In unweighted graphs.
### Networking: Discovering the connections between nodes.
### Social Media: Analyzing friend networks.
### Web Crawling: Systematically browsing the internet.
### Game Development: Navigating through maps and solving puzzles.
### About This Application 🌟
This application is designed to help you understand BFS by providing the following interactive features:

### Dataset Generation: Randomly generates a dataset of persons using English first and last names.
### Graph Construction: Builds an undirected random graph where nodes represent persons and edges represent potential connections (with a probability of 0.3).
### BFS Traversal: Executes BFS starting from a random node and constructs a BFS tree.
### Visualization: Displays the entire graph using NetworkX and matplotlib, highlighting the BFS tree edges in red for clarity.
When you click the "Generate" button, the app will create a new random dataset, construct the graph, perform the BFS traversal, and then show you both the list of BFS tree edges and a visual representation of the graph.

How to Run the Application 🏃‍♂️
Clone the Repository:

bash
git clone <repository_url>
cd <repository_directory>
Install the Dependencies: Make sure you have Python installed. Then install the required packages:

bash
pip install streamlit networkx matplotlib
Run the App: Start the Streamlit app by running:

bash
streamlit run app.py
Interact with the App:

Click the "Generate" button to see a new dataset and graph.
Watch as the BFS algorithm traverses the graph from a random starting node.
Enjoy the dynamic visualization of the graph and BFS tree!
