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

- requirements.txt: Python dependencies required to run the simulations (e.g., numpy, matplotlib, scipy).

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

---

# DONE

- [x] imlement beefy RPS env
- [x] implement FP agent
- [x] implement q-learning agent
- [x] Move into notebook
- [x] implement **decaying** epsilon
- [x] break into modules
- [x] **implement minmax q-learning** - https://github.com/tocom242242/minimax_q_learning - https://dl.acm.org/doi/pdf/10.5555/945365.964288

# TODO

- [ ] Convert into stochastic with limit cap
- [ ] extract metrics [scores, env.state, q-table, sigma, epsilon, diagrams, experiments, interpretations, self-plays]
- [ ] use petting zoo for RPS
- [ ] research - competitive grid world
- [ ] research - implement pong game (discrete actions)
- [ ] research - hunter-pray game gridworld
- [ ] research - implement multi-agent shooting game
- [ ] implement SARSA agent - https://www.geeksforgeeks.org/machine-learning/sarsa-reinforcement-learning/
- [ ] practical application ???
- [ ] evolutionary algorithms - research
- [ ] bomb difusal game/environment
- [ ] penalties game/environment
- [ ] DoubleQ - https://arxiv.org/html/2310.06286v3


# Resources

READ THIS FIRST: https://lefkippos.ds.unipi.gr/modules/document/file.php/AI_IIT113/Lectures%205%20%26%206%20Agents-Interactions_Game_Theory.pdf

- Q-Learning (Pong) - https://courses.grainger.illinois.edu/ece448/sp2018/assignment4.html
- evolutionary algo - https://www.cs.vu.nl/~gusz/ecbook/Eiben-Smith-Intro2EC-Ch2.pdf
- evolutionary rl - https://github.com/RichardAragon/EvolutionaryReinforcementLearning
- paper to get games, metrics, algos - https://github.com/shiivashaakeri/Pong-Deep-QLearning/blob/main/Report.pdf
- q-learning tutorial - https://www.geeksforgeeks.org/machine-learning/q-learning-in-python/
- book implementations for RL - https://github.com/ShangtongZhang/reinforcement-learning-an-introduction
- RL taxonomy - https://github.com/bennylp/RL-Taxonomy
- OpenAI RL taxonomy - https://spinningup.openai.com/en/latest/spinningup/rl_intro2.html
- SARSA - https://github.com/linesd/tabular-methods/blob/master/algorithms/temporal_difference.py; https://www.geeksforgeeks.org/machine-learning/sarsa-reinforcement-learning/
- ALL RL ALGOS - https://github.com/FareedKhan-dev/all-rl-algorithms/blob/master/cheatsheet.md
- RL algorithms paper - https://arxiv.org/pdf/2209.14940
- minmax q-learning - https://github.com/tocom242242/minimax_q_learning/blob/master/minimax_q_learner.py; https://github.com/theevann/MinimaxQ-Learning
- Multi-Step Minimax Q-learning Algorithm for Two-Player Zero-Sum Markov Games - https://arxiv.org/abs/2407.04240
- Policies in MDPS and games - https://courses.cs.duke.edu/spring07/cps296.3/littman94markov.pdf
