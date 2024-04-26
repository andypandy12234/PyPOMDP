from grid_world_maker import POMDPModelMaker

if __name__ == '__main__':
    definition = {
        'discount': 0.90,
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
            }
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
            
            'HRT': {'s1': 150, 's2': 100, 's3': 100, 's4': -50},
            'CBT': {'s1': 150, 's2': 100, 's3': 100, 's4': -50},
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
