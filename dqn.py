import torch as T
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import numpy as np

class DeepQNetwork(nn.Module):
	def __init__(self, lr, input_dims, fc1_dims, fc2_dims, n_actions):
		super(DeepQNetwork, self).__init__()
		self.input_dims = input_dims
		self.fc1_dims = fc1_dims
		self.fc2_dims = fc2_dims
		self.n_actions = n_actions

		self.fc1 = nn.Linear(*self.input_dims, self.fc1_dims)
		self.fc2 = nn.Linear(self.fc1_dims, self.fc2_dims)
		self.fc3 = nn.Linear(self.fc2_dims, 256)
		self.fc3 = nn.Linear(256, 256)
		self.fc4 = nn.Linear(256, 128)
		self.fc5 = nn.Linear(128, 64)
		self.fc6 = nn.Linear(64,32)
		self.fc7 = nn.Linear(32, self.n_actions)

		self.optimizer = optim.Adam(self.parameters(), lr=lr)
		self.loss = nn.MSELoss()
		self.device = T.device('cuda:0' if T.cuda.is_available() else 'cpu')
		self.to(self.device)

	def forward(self, state):
		state = state.float()
		x = F.relu(self.fc1(state)).float()
		x = F.relu(self.fc2(x)).float()
		x = F.relu(self.fc3(x)).float()
		x = F.relu(self.fc4(x)).float()
		x = F.relu(self.fc5(x)).float()
		x = F.relu(self.fc6(x)).float()
		actions = self.fc7(x)
		return actions
