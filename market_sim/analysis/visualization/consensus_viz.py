import matplotlib.pyplot as plt

def visualize_bft_thresholds(max_nodes: int = 20):
    
    nodes = list(range(1, max_nodes + 1))
    thresholds = [(2 * (n // 3)) + 1 for n in nodes]
    faults_tolerated = [n // 3 for n in nodes]

    plt.figure(figsize=(10, 6))
    plt.step(nodes, thresholds, label='Required Agreement (2f+1)', where='post', color='blue', linewidth=2)
    plt.step(nodes, faults_tolerated, label='Max Faulty Nodes Tolerated (f)', where='post', color='red', linestyle='--')
    
    plt.title('BFT Consensus Scaling (n > 3f Rule)')
    plt.xlabel('Total Network Nodes (n)')
    plt.ylabel('Number of Nodes')
    plt.xticks(nodes)
    plt.grid(True, which='both', linestyle=':', alpha=0.5)
    plt.legend()
    
    print("Saving visualization to bft_thresholds.png...")
    plt.savefig('bft_thresholds.png')
    plt.show()

if __name__ == "__main__":
    visualize_bft_thresholds()