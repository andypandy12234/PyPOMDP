import json
import matplotlib.pyplot as plt
import pandas as pd

# Load simulation data
with open('simulation_data.json', 'r') as f:
    data = json.load(f)

# Convert data to DataFrame
df = pd.DataFrame(data)

# Plotting total rewards over simulations
plt.figure(figsize=(10, 6))
plt.plot(df['simulation'], df['reward'], marker='o', linestyle='-')
plt.title('Rewards Over Simulations')
plt.xlabel('Simulation Number')
plt.ylabel('Total Reward')
plt.grid(True)
plt.show()

# Plotting belief states if they are dimensionally consistent
if all('belief' in d for d in data):
    beliefs_df = pd.DataFrame(df['belief'].tolist())
    beliefs_df.plot()
    plt.title('Belief States Over Simulations')
    plt.xlabel('Simulation Number')
    plt.ylabel('Belief Probability')
    plt.show()
