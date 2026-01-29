# Fictitious play and reinforcement learning for computing equilibria
- Repeated & zero sum (stochastic) games
- Fictitious play (FP) (theory and implementation)
- Reinforcement Learning (RL) (theory and implementation)
- Experimental results comparing FP and RL

---

## Repeated & zero sum (stochastic) games

### Zero-sum game
**Situation**
- competing entities
- the result is an **advantage for one side** and an **equivalent loss** for the other (+5, -5)
- the net improvement in benefit of the whole game is zero.
    - Why? The advantage for one side is an equal loss for the other side.
    - This sum is zero.

#### Examples of games
- poker
- chess
- sports?
- bridge

### Repeated/Iterated game
- The same stage is played at each timeframe.
- Repeated number of repetitions of a base game (stage game)
- Same game, multiple games

#### Examples
- 2 gas stations offer competing prices
- Stage Game: The single-shot game played in each period.

### Stochastic/Markov games
- dynamic, multi-agent
- probabilities influence the transition to next state
- player strategies depend only on the current state

## Environment/Game description

Construct a game/environment which combines the above 3 characteristics.
In other words, it asks for a Competitive Markov Game, a two-player zero-sum game.


---


## Equilibria

### Nash equilibrium
- no player could gain more by changing their play strategy in a game.
- players choose their optimal strategy against the other players constant strategy
- does not guarantee overall best pay-off
- suboptimal for the group
- **Pareto inefficient**


### Pareto optimality/efficiency
- is a group/collective strategy
- every player is better off
- no players in worse situations (aka no punished players)


---


## Fictitious play - FP
- players keep track of the empirical frequency of opponent's past moves
    - i.e. player 2 played heads 60% of the time
    - choose best response against that average
- players adjust their strategies
- players assume opponent's strategy based on past historical frequency
- FP is guaranteed to converge to Nash equilibrium.
    - WHY?
    - Player 2, always chooses best/rational response against player 1's move
- FP approach can be systematically exploited!!!

**Refs**:
What's FP:
- https://en.wikipedia.org/wiki/Fictitious_play

FP Agent design:
- https://www.youtube.com/watch?v=_XIdEr-wtJg

FP Agent beliefs initialization:
- https://cse.unl.edu/~lksoh/Classes/CSCE475_875_Fall17/handouts/sup09.pdf


---


## Reinforcement Learning - RL
- Player explores actions and receives rewards or punishments - feedback
- Implemented via Q-learning or variants.
- Q-value updated on trial and error - exploration


---

## Implementation


### 1. Beefy Rock-Paper-Scissors - RPS

This is a high stakes Rock-Paper-Scissors game.

#### States
1. `State-i`: Initial state: Standard rewards (+1 win, -1 loss)
2. `State-n`: Next state: Rewards of previous state are doubled each time
3. We cap the states to a number to reduce the amount of memory for the agents

#### Stochastic transition (P)
- If there's a draw at any state, there's a P-chance to transition into next state in which rewards double.
- Otherwise, game stays in the same state.

#### Zero-Sum rewards (R)
- The sum of the rewards for Player 1 and Player 2 is always 0.
- One player wins, other loses: rewards for one is equal penalty for other.

#### Repeated
- Player play 10 rounds of the same game.

---

# TODO

- [x] imlement beefy RPS env
- [x] implement FP agent
- [x] implement q-learning agent
- [ ] implement **decaying** epsilon

```python
np.linspace(1, 0, 1000)
```

- [ ] **implement minmax q-learning**

- [ ] Convert into stochastic with limit cap
- [ ] break into modules
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

