import subprocess
import os

def modify_pomdp_rewards(file_path, new_rewards):
    # Attempt to open and read the file
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
        return

    # Prepare to collect modified lines
    new_lines = []

    # Iterate over each line in the file
    for line in lines:
        modified = False
        if line.startswith('R:'):
            parts = line.strip().split()  # Split the line into components
            action = parts[1]
            state = parts[3]

            # Check if this line's action and state are in the new_rewards dictionary
            if action in new_rewards and state in new_rewards[action]:
                # Modify the reward value at the end of the line
                parts[-1] = str(new_rewards[action][state])
                new_line = ' '.join(parts) + '\n'
                new_lines.append(new_line)
                modified = True

        # If the line was not modified, append it as is
        if not modified:
            new_lines.append(line)

    # Write the new lines back to the file
    with open(file_path, 'w') as file:
        file.writelines(new_lines)
        print("File updated successfully.")

def run_pomdp_simulation():
    # Define the command to run the simulation
    command = ['C:/Users/super/venv/Scripts/python.exe', 'main.py', 'pomcp', '--env', 'MenopauseTreatment.POMDP', '--max_play', '4']
    # Run the simulation and capture the output
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout

def main():
    pomdp_file_path = 'environments/pomdp/MenopauseTreatment.POMDP'  # Path to your .POMDP file
    
    # Define new reward values to test
    reward_configurations = [
        {'HRT': {'s1': 0, 's2': 0, 's3': 0, 's4': 0}, 'CBT': {'s1': 150, 's2': 100, 's3': 100, 's4': 50}},
        {'HRT': {'s1': 10, 's2': 20, 's3': 30, 's4': 40}, 'CBT': {'s1': 160, 's2': 120, 's3': 140, 's4': 70}},
        {'HRT': {'s1': 20, 's2': 30, 's3': 40, 's4': 50}, 'CBT': {'s1': 170, 's2': 130, 's3': 140, 's4': 80}}
    ]

    # Iterate over each reward configuration, modify the .POMDP file, and run the model
    for config in reward_configurations:
        print(f"Testing configuration: {config}")
        modify_pomdp_rewards(pomdp_file_path, config)
        simulation_output = run_pomdp_simulation()
        print("Simulation output:", simulation_output)
        # Here, you would add your analysis functions to process simulation_output

if __name__ == "__main__":
    main()



