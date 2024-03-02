import networkx as nx
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import time

def create_hops_graph(hops):
    start_time = time.time()
    G = nx.Graph()
    current_node = 'A'
    nodes_at_current_level = ['A']
    for i in range(hops):
        next_nodes = []
        for node in nodes_at_current_level:
            for j in range(1, hops + 2):
                next_node = f"{node}-{j}"
                G.add_edge(node, next_node)
                next_nodes.append(next_node)
        nodes_at_current_level = next_nodes
    end_time = time.time()
    print("Time taken to create graph:", end_time - start_time, "seconds")
    return G

def visualize_hops_graph(G):
    start_time = time.time()
    pos = nx.spring_layout(G)  # Better layout than spring_layout can be chosen
    edge_x = []
    edge_y = []
    for edge in G.edges():
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
        edge_x.extend([x0, x1, None])
        edge_y.extend([y0, y1, None])

    edge_trace = go.Scatter(
        x=edge_x,
        y=edge_y,
        line=dict(width=0.5, color='#888'),
        hoverinfo='none',
        mode='lines')

    node_x = []
    node_y = []
    node_text = []
    for node in G.nodes():
        x, y = pos[node]
        node_x.append(x)
        node_y.append(y)
        node_text.append(node)

    node_trace = go.Scatter(
        x=node_x,
        y=node_y,
        mode='markers',
        hoverinfo='text',
        marker=dict(
            showscale=False,
            colorscale='YlGnBu',
            reversescale=True,
            color=[],
            size=10,
            colorbar=dict(
                thickness=15,
                title='Node Connections',
                xanchor='left',
                titleside='right'
            ),
            line_width=2))

    fig = go.Figure(data=[edge_trace, node_trace],
                 layout=go.Layout(
                    title='Hops Graph Visualization',
                    titlefont_size=16,
                    showlegend=False,
                    hovermode='closest',
                    margin=dict(b=20,l=5,r=5,t=40),
                    annotations=[ dict(
                        text="Python code: <a href='https://github.com/openai/gpt-3-examples'> Link </a>",
                        showarrow=False,
                        xref="paper", yref="paper",
                        x=0.005, y=-0.002 ) ],
                    xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                    yaxis=dict(showgrid=False, zeroline=False, showticklabels=False))
                    )
    fig.show()
    end_time = time.time()
    print("Time taken to visualize graph:", end_time - start_time, "seconds")
    print("Number of nodes:", len(G.nodes()))

def main():
    hops = int(input("Enter the number of hops: "))
    G = create_hops_graph(hops)
    visualize_hops_graph(G)

if __name__ == "__main__":
    main()