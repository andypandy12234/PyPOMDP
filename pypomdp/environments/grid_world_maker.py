class POMDPModelMaker:
    def __init__(self, configs):
        self.configs = configs
        self.states = configs['states'].split()
        self.actions = configs['actions'].split()
        self.observations = configs['observations'].split()
    
    def make_meta(self, lines):
        lines.append(f"discount: {self.configs['discount']}\n")
        lines.append(f"values: {self.configs['values']}\n")
        lines.append(f"states: {' '.join(self.states)}\n")
        lines.append(f"actions: {' '.join(self.actions)}\n")
        lines.append(f"observations: {' '.join(self.observations)}\n")
        lines.append(f"init_state: {self.configs['init_state']}\n\n")

    def make_R(self, lines):
        template = 'R: {action} : {state} : * : * {reward}\n'
        for action in self.actions:
            for state in self.states:
                reward = self.configs['rewards'][action][state]
                lines.append(template.format(action=action, state=state, reward=reward))

    def make_T(self, lines):
        template = 'T: {action} : {state} : {next_state} {prob}\n'
        for action in self.actions:
            for state in self.states:
                transition_probs = self.configs['transitions'][action][state]
                for next_state, prob in zip(self.states, transition_probs):
                    lines.append(template.format(action=action, state=state, next_state=next_state, prob=prob))

    def make_O(self, lines):
        template = 'O: {action} : {state} : {observation} {prob}\n'
        for action in self.actions:
            for state in self.states:
                obs_probs = self.configs['observation_probabilities'][action][state]
                for observation, prob in zip(self.observations, obs_probs):
                    lines.append(template.format(action=action, state=state, observation=observation, prob=prob))

# Example configuration for menopause treatment
definition = {
    'discount': 0.9,
    'values': 'reward',
    'states': 's1 s2 s3 s4',
    'actions': 'HRT CBT',
    'observations': 'o1 o2 o3 o4',
    'init_state': 's1',
    'transitions': {
        'HRT': {
            's1': [0.28, 0.12, 0.42, 0.18],
            's2': [0.3, 0.2, 0.35, 0.15],
            's3': [0.14, 0.56, 0.21, 0.09],
            's4': [0.18, 0.18, 0.42, 0.22]
        },
        'CBT': {
            's1': [0.32, 0.08, 0.48, 0.12],
            's2': [0.21, 0.07, 0.49, 0.23],
            's3': [0.24, 0.36, 0.24, 0.16],
            's4': [0.2, 0.3, 0.25, 0.25]
        },
    },
    'observation_probabilities': {
        'HRT': {
            's1': [0.03, 0.27, 0.07, 0.63],
            's2': [0.18, 0.02, 0.72, 0.08],
            's3': [0.07, 0.63, 0.03, 0.27],
            's4': [0.56, 0.24, 0.14, 0.06]
        },
        'CBT': {
            's1': [0.1, 0.1, 0.4, 0.4],
            's2': [0.07, 0.03, 0.63, 0.27],
            's3': [0.48, 0.12, 0.32, 0.08],
            's4': [0.63, 0.07, 0.27, 0.03]
        }
    },
    'rewards': {
        'HRT': {'s1': 120, 's2': 130, 's3': 100, 's4': 90},
        'CBT': {'s1': 120, 's2': 120, 's3': 130, 's4': 100}
    }
}

maker = POMDPModelMaker(definition)
lines = []
maker.make_meta(lines)
maker.make_R(lines)
maker.make_T(lines)
maker.make_O(lines)

with open('./pomdp/MenopauseTreatment.POMDP', 'w+') as outfile:
    outfile.writelines(lines)


