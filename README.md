# Computing Equilibria in Repeated Zero-Sum Games

This repository contains the research, implementation, and experimental analysis of learning algorithms in adversarial environments. The project focuses on how agents reach Nash Equilibrium in repeated zero-sum games using both model-based and model-free approaches.

## Project Overview

The study utilizes Rock-Paper-Scissors (RPS) as a fundamental model for zero-sum interactions. It explores the convergence properties, stability, and exploitability of three distinct algorithmic approaches:

1. Fictitious Play (FP): A model-based learning heuristic where agents maintain an empirical frequency of the opponent's past actions to compute a Best Response.

2. Standard Q-Learning: A model-free reinforcement learning approach that treats the opponent as part of the stochastic environment.

3. Minimax Q-Learning (Nash-Q): An adversarial reinforcement learning algorithm that utilizes Linear Programming to solve for the game's value and optimal mixed strategy (π).

### Key Features

- Custom Environment: A modular RPS_environment supporting stationary repeated games and scalable to stochastic transitions.

- Adversarial Modeling: Implementation of the Minimax-Q solver using scipy.optimize.linprog.

- Experimental Metrics: Tracking of Cumulative Regret and strategy convergence (σ vs π) over long-horizon simulations (up to 1,000 rounds).

- Adaptive Exploration: Implementation of exponential epsilon decay strategies to balance the exploration-exploitation trade-off.

### Repository Structure

- report.ipynb: The primary research document containing the theory, implementation code, and interactive visualizations.

- report.html: A static, pre-rendered version of the research for quick viewing.

- requirements.txt: Python dependencies required to run the simulations (e.g., numpy, matplotlib, scipy).

- LICENSE: Project licensing information.

### Installation

```bash
# Clone the repository
git clone "https://github.com/your-username/repo-name.git"
cd "repo-name"

# Install dependencies
pip install -r "requirements.txt"
```

### Usage

```bash
jupyter notebook "report.ipynb"
```
