import numpy as np
import random
import matplotlib.pyplot as plt

class TechnologyModel:
    def __init__(self, n, gamma, t_steps, dsm_density=0.2):
        self.n = n  # Number of components
        self.gamma = gamma  # Difficulty of reducing costs (exponent)
        self.t_steps = t_steps  # Number of innovation steps
        self.dsm_density = dsm_density  # Density of DSM (probability of interactions)
        
        # Initialize costs randomly between 0 and 1
        self.costs = np.random.rand(n)
        
        # Initialize Design Structure Matrix (DSM) with some density
        self.dsm = self.generate_dsm()
        
    def generate_dsm(self):
        """Generate a random Design Structure Matrix (DSM)"""
        dsm = np.random.rand(self.n, self.n) < self.dsm_density
        np.fill_diagonal(dsm, 0)  # No self-dependence
        return dsm

    def update_costs(self):
        """Perform one innovation attempt and update costs"""
        # Step 1: Pick a random component i
        i = random.randint(0, self.n - 1)
        
        # Step 2: Find components 
        Ai = np.where(self.dsm[i, :] == 1)[0]
        
        # Step 3: Propose new costs for components 
        new_costs = np.random.rand(len(Ai)) ** self.gamma 
        
        # Calculate current sum of costs 
        current_sum = np.sum(self.costs[Ai])
        
        # Calculate new sum of costs
        new_sum = np.sum(new_costs)
        
        # Step 4: Accept or reject based on the total cost
        if new_sum < current_sum:
            self.costs[Ai] = new_costs  # Accept the new costs
            return True
        return False  # Reject the change
    
    def run_simulation(self):
        """Run the simulation for t_steps"""
        cost_history = [np.sum(self.costs)]  # Track total cost
        for _ in range(self.t_steps):
            self.update_costs()
            cost_history.append(np.sum(self.costs))
        return cost_history

    def plot_results(self, cost_history):
        """Plot the evolution of total cost over time"""
        plt.figure(figsize=(10, 6))
        plt.plot(cost_history)
        plt.xlabel('Innovation Attempts')
        plt.ylabel('Total Cost of Technology')
        plt.title(f'Total Cost Evolution Over {self.t_steps} Innovation Attempts')
        plt.show()

    def plot_dsm_heatmap(self):
        """Plot a heatmap of the Design Structure Matrix (DSM) using Matplotlib"""
        plt.figure(figsize=(8, 6))
        plt.imshow(self.dsm, cmap="Blues", interpolation='nearest')
        plt.colorbar(label='Dependency Strength')  # Add a color bar for reference
        plt.title("Design Structure Matrix (DSM) Heatmap")
        plt.xlabel('Component Index')
        plt.ylabel('Component Index')
        plt.show()

# Example of running the model
n = 50  # Number of components
gamma = 2.0  # Difficulty of reducing costs
t_steps = 1000  # Number of innovation attempts

# Create the model
model = TechnologyModel(n, gamma, t_steps)

# Run the simulation
cost_history = model.run_simulation()

# Plot the results: total cost over time
model.plot_results(cost_history)

# Plot the DSM heatmap to visualize the dependencies
model.plot_dsm_heatmap()

