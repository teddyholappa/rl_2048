from game import Game 
import numpy as np
from q_agent import Agent
import os
import matplotlib.pyplot as plt

os.environ['KMP_DUPLICATE_LIB_OK']='True'

game = Game()
agent = Agent(gamma=1, epsilon = 1.0, batch_size=64,
				n_actions=4, eps_end=0.01, input_dims=[16],
				lr=0.0001)
scores, eps_history = [],[]
avg_scores = []
n_games = 20000
for i in range(n_games):
	game.reset()
	score = 0
	done = False
	observation = game.get_state()
	while not done:
		action = agent.choose_action(observation)
		game.move(game.actions[action])
		game.update()
		observation_,reward,done = game.get_info()
		score+=reward
		agent.store_transition(observation, action, reward, observation_,done)
		agent.learn()
		observation = observation_
	#game.print_board()
	scores.append(game.score)
	eps_history.append(agent.epsilon)

	avg_score = np.mean(scores[-100:])
	print("i: ", i, "avg_score: ", avg_score, " epsilon: ", agent.epsilon)

plt.plot(avg_scores)
plt.show()




