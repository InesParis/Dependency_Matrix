class TechnologyModel {
    constructor(n, t_steps, dsm_density = 0.2) {
        this.n = n;  // Number of components
        this.t_steps = t_steps;  // Number of innovation steps
        this.dsm_density = dsm_density;  // Density of DSM (probability of interactions)

        // Initialize costs randomly between 0 and 1
        this.costs = Array.from({ length: n }, () => Math.random());

        // Initialize Design Structure Matrix (DSM) with some density
        this.dsm = this.generateDSM();
    }

    generateDSM() {
        let dsm = Array.from({ length: this.n }, () =>
            Array.from({ length: this.n }, () => Math.random() < this.dsm_density ? 1 : 0)
        );
        for (let i = 0; i < this.n; i++) {
            dsm[i][i] = 0;  // No self-dependence
        }
        return dsm;
    }

    updateCosts() {
        // Step 1: Pick a random component i
        let i = Math.floor(Math.random() * this.n);

        // Step 2: Find components that depend on i
        let Ai = this.dsm[i].map((val, idx) => val === 1 ? idx : -1).filter(idx => idx !== -1);

        // Step 3: Propose new costs for components
        let newCosts = Ai.map(() => Math.random());

        // Calculate current sum of costs
        let currentSum = Ai.reduce((sum, idx) => sum + this.costs[idx], 0);
 
        // Calculate new sum of costs
        let newSum = newCosts.reduce((sum, cost) => sum + cost, 0);

        // Step 4: Accept or reject based on the total cost
        if (newSum < currentSum) {
            Ai.forEach((idx, idx2) => {
                this.costs[idx] = newCosts[idx2];
            });
            return true;
        }
        return false;
    }

    runSimulation() {
        let costHistory = [this.costs.reduce((sum, cost) => sum + cost, 0)];
        for (let i = 0; i < this.t_steps; i++) {
            this.updateCosts();
            costHistory.push(this.costs.reduce((sum, cost) => sum + cost, 0));
        }
        return costHistory;
    }
}

document.getElementById("simulation-form").addEventListener("submit", function(event) {
    event.preventDefault();

    // Get user inputs and ensure valid values
    let n = parseInt(document.getElementById("n").value);
    let dependencies = parseFloat(document.getElementById("dependencies").value); // density of dependencies
    let t_steps = parseInt(document.getElementById("t_steps").value);

    // Validation for n (number of components)
    if (isNaN(n) || n <= 0) {
        alert("Number of components must be a positive whole number.");
        return;
    }

    // Validation for dependencies (between 0 and 1)
    if (isNaN(dependencies) || dependencies < 0 || dependencies > 1) {
        alert("Number of dependencies must be between 0 and 1.");
        return;
    }

    // Validation for t_steps (minimum 20000)
    if (isNaN(t_steps) || t_steps < 20000) {
        alert("Innovation steps must be at least 20000.");
        return;
    }

    // Create the model with the specified parameters
    let model = new TechnologyModel(n, t_steps, dependencies);

    // Run the simulation
    let costHistory = model.runSimulation();

    // Plot Total Cost Evolution
    let costTrace = {
        x: Array.from({ length: t_steps + 1 }, (_, i) => i),
        y: costHistory,
        mode: 'lines',
        type: 'scatter'
    };
    let costLayout = {
        title: 'Total Cost Evolution Over Time',
        xaxis: { title: 'Innovation Attempts' },
        yaxis: { title: 'Total Cost of Technology' }
    };
    Plotly.newPlot('cost-evolution', [costTrace], costLayout);

    // Plot DSM Heatmap
    let dsmData = {
        z: model.dsm,
        colorscale: 'Blues',
        showscale: true
    };
    let dsmLayout = {
        title: 'Design Structure Matrix (DSM)',
        xaxis: { title: 'Component Index' },
        yaxis: { title: 'Component Index' }
    };
    Plotly.newPlot('dsm-heatmap', [dsmData], dsmLayout);
});
