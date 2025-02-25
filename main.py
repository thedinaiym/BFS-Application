import streamlit as st
import random
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

st.title("Mini Site: Logical BFS Family Tree")
st.write("""
**BFS (Breadth-First Search)** is a graph traversal algorithm that starts from a selected node and explores all its immediate neighbors before moving on to the next level. It is widely used to find the shortest path in unweighted graphs and to discover all connected nodes.

In this application, we simulate a logical family tree: if a person's first name matches another person's last name, they are likely related (e.g., parent-child). Enjoy the interactive visualization!

**Key BFS Steps:**
1. **Initialization**: Select a starting node, add it to a queue, and mark it as visited.
2. **Traversal**: Dequeue a node, visit all its unvisited neighbors, and add them to the queue.
3. **Repeat**: Continue until the queue is empty, thus exploring the graph level by level.
""")

if st.button("Generate"):
    first_names = ["John", "Emily", "Michael", "Sarah", "David", "Emma", "Daniel", "Olivia", "Smith", "Johnson"]
    last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Miller", "Emily", "Michael", "David", "Daniel"]
    
    num_persons = 10
    persons = {}
    for i in range(num_persons):
        first = random.choice(first_names)
        last = random.choice(last_names)
        persons[i] = f"{first} {last}"
    
    st.subheader("Dataset of Persons")
    for pid, name in persons.items():
        st.write(f"ID {pid}: {name}")
    
    graph = {i: set() for i in range(num_persons)}
    for i in range(num_persons):
        first_i, last_i = persons[i].split()
        for j in range(i + 1, num_persons):
            first_j, last_j = persons[j].split()
            if first_i == last_j or first_j == last_i:
                graph[i].add(j)
                graph[j].add(i)
    
    st.write("### Graph Construction Logic:")
    st.write("""
For each person, we compare their first name and last name with others. If one person's first name matches another's last name, 
a connection is established. This simulates, for example, a child inheriting the parent's last name.
""")
    
    st.write("### BFS Function Code:")
    st.code("""
def bfs_tree(start, graph):
    visited = set()            # Set to track visited nodes
    queue = deque([start])     # BFS queue initialized with the starting node
    tree_edges = []            # List to store BFS tree edges
    while queue:
        current = queue.popleft()    # Dequeue the current node
        if current not in visited:
            visited.add(current)     # Mark the node as visited
            for neighbor in graph[current]:
                if neighbor not in visited:
                    tree_edges.append((current, neighbor))  # Record the edge
                    queue.append(neighbor)  # Enqueue the neighbor
    return tree_edges, visited
    """, language="python")
    
    def bfs_tree(start, graph):
        visited = set()           
        queue = deque([start])    
        tree_edges = []           
        while queue:
            current = queue.popleft()
            if current not in visited:
                visited.add(current)
                for neighbor in graph[current]:
                    if neighbor not in visited:
                        tree_edges.append((current, neighbor))
                        queue.append(neighbor)
        return tree_edges, visited

    start_person = random.choice(list(persons.keys()))
    st.write("Starting BFS from:", persons[start_person])
    
    tree_edges, visited_nodes = bfs_tree(start_person, graph)
    
    st.subheader("BFS Tree Edges:")
    if tree_edges:
        for edge in tree_edges:
            st.write(f"{persons[edge[0]]} -> {persons[edge[1]]}")
    else:
        st.write("No logical BFS connections found from the selected node.")
    
    G = nx.Graph()
    for i, name in persons.items():
        G.add_node(i, label=name)
    for i, neighbors in graph.items():
        for j in neighbors:
            G.add_edge(i, j)
    
    pos = nx.spring_layout(G, seed=42)
    plt.figure(figsize=(8, 6))
    nx.draw(G, pos, with_labels=True, labels=persons,
            node_color='lightblue', edge_color='gray', node_size=1500, font_size=10)
    
    if tree_edges:
        nx.draw_networkx_edges(G, pos, edgelist=tree_edges, edge_color='red', width=2)
    
    st.subheader("Graph and BFS Tree Visualization")
    st.pyplot(plt.gcf())
