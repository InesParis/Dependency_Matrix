import random
import numpy as np
import matplotlib.pyplot as plt

class TechnologyModel:
    def __init__(self, n, d, num_iterations=1000):
        self.n = n  # Number of components
        self.d = d  # Connectivity (degree)
        self.num_iterations = num_iterations
        
        # Initialize the components with costs between 0 and 1
        self.costs = np.random.rand(n)
        
        # Initialize the design complexity (connectivity)
        self.design_complexity = self.d  # Assuming constant d
        self.total_cost = np.sum(self.costs)
        
        # Initialize the adjacency list (to represent the clusters of components)
        self.network = self.create_network()

    def create_network(self):
        """Creates a random network of components with degree d."""
        network = {i: set() for i in range(self.n)}
        for i in range(self.n):
            while len(network[i]) < self.d - 1:
                # Randomly connect components to other components
                j = random.randint(0, self.n - 1)
                if i != j:  # Avoid self-loops
                    network[i].add(j)
                    network[j].add(i)
        return network

    def innovation_attempt(self):
        """Perform an innovation attempt: randomly change costs of a cluster."""
        # Randomly select a cluster (a component and its neighbors)
        component = random.randint(0, self.n - 1)
        neighbors = list(self.network[component]) + [component]
        
        # Save the old total cost of the selected cluster
        old_cost = np.sum(self.costs[neighbors])
        
        # Modify the costs of the selected cluster randomly
        for idx in neighbors:
            self.costs[idx] = random.random()  # Assign new random cost between 0 and 1
        
        # Accept the change only if the new total cost is lower
        new_cost = np.sum(self.costs[neighbors])
        if new_cost < old_cost:
            return True
        else:
            # Revert changes if not accepted
            for idx in neighbors:
                self.costs[idx] = old_cost / len(neighbors)
            return False

    def run_simulation(self):
        """Run the simulation of innovation attempts."""
        cost_history = []
        for _ in range(self.num_iterations):
            self.innovation_attempt()
            self.total_cost = np.sum(self.costs)
            cost_history.append(self.total_cost)
        
        return cost_history

    def plot_results(self, cost_history):
        """Plot the results: total cost vs. number of attempts."""
        plt.plot(cost_history)
        plt.xlabel('Number of Innovation Attempts')
        plt.ylabel('Total Cost of Technology')
        plt.title(f'Innovation Process: Cost vs. Attempts (n={self.n}, d={self.d})')
        plt.show()

# Example of running the model
n = 50  # Number of components
d = 5   # Connectivity (degree)
num_iterations = 1000  # Number of innovation attempts

# Create the model
model = TechnologyModel(n, d, num_iterations)

# Run the simulation
cost_history = model.run_simulation()

# Plot the results
model.plot_results(cost_history)
