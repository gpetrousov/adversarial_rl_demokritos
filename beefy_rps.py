import random


class BeefyRPSEnv():
    """
    Beefy ROck Paper Scissors environment - high stakes.
    """

    def __init__(self):

        # Payoff Matrix: Player 1 rows, Player 2 cols
        # 0: Rock
        # 1: Paper
        # 2: Scissors
        self.matrix = [
                # R  P  S
                [0, -1, 1],  # R
                [1, 0, -1],  # P
                [-1, 1, 0],  # S
                ]

        # Initial state - Normal
        self.state = 0
        # Transition probability
        self.P = 0.3
        self.max_states = 3

    def step(self, action1, action2):
        """
        Transition function:
        1. receive actions from players
        2. calculate rewards
        3. update state
        4. return information
        """

        reward1 = self.matrix[action1][action2]*(self.state+1)
        reward2 = -reward1

        # Calculate transition
        # if action1 == action2:
        #     if random.random() < self.P:
        #         if self.state < self.max_states:
        #             # We transition
        #             self.state += 1
        # else:
        #     self.reset()

        return self.state, reward1, reward2

    def reset(self):
        """ Winning condition reached. """
        self.state = 0


class FictitiousPlayAgent():

    def __init__(self):
        # Times a move has been played
                      #R #P #S
        self.counts = [0, 0, 0]

        # Probability distribution
                      #R #P #S
        self.sigma = [0, 0, 0]

        # Utility matrix
        self.rows = 3
        self.cols = 3
        self.u = [
            # R  P  S
            [0, -1, 1],  # R
            [1, 0, -1],  # P
            [-1, 1, 0],  # S
            ]

    def action(self, opponent_action):
        """
        Calculate the best action and ACT.
        """
        if opponent_action is not None:
            self.update_counts(opponent_action)
            self.update_sigma(opponent_action)
            best_move = self.find_best_move()
        else:
            best_move = random.randint(0, 2)
        return best_move

    def update_counts(self, opponent_action):
        self.counts[opponent_action] += 1

    def update_sigma(self, opponent_action):
        for i in range(len(self.sigma)):
            self.sigma[i] = self.counts[i]/sum(self.counts)

    def find_best_move(self):
        """
        Calculates utilities using distribution sigma and returns best move.
        """
        max_u = -float("inf")
        best_move = random.randint(0, 2)
        for i in range(self.rows):
            row_i_sum = sum([a*b for a, b in zip(self.u[i], self.sigma)])
            if row_i_sum > max_u:
                max_u = row_i_sum
                best_move = i

        return best_move


def main():
    env = BeefyRPSEnv()
    agent1 = FictitiousPlayAgent()
    agent2 = FictitiousPlayAgent()

    # Initializer
    last_act2 = None
    last_act1 = None

    env.reset()

    for i in range(1000):
        curr_act1 = agent1.action(last_act2)
        curr_act2 = agent2.action(last_act1)

        env.step(curr_act1, curr_act2)

        last_act1 = curr_act1
        last_act2 = curr_act2


if __name__ == "__main__":
    main()
