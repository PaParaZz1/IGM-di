import os
import ding

on_policy_algo = set(['a2c', 'ppo'])


def generate_runnable_entry(metadata):
    dirname = os.path.join(os.path.dirname(ding.__path__[0]), 'dizoo')
    env_mapping = {'cartpole': ['classic_control', 'cartpole', 'config']}
    base_dir = 'experiment'
    metadata['task_path'] = []

    for env in metadata['env']:
        env_dir = os.path.join(base_dir, env)
        for algo in metadata['algo']:
            algo_dir = os.path.join(env_dir, algo)
            filename = '{}_{}_config.py'.format(env, algo)
            filename = os.path.join(dirname, *env_mapping[env], filename)
            metadata['task_path'].append({'src': filename, 'dst': os.path.join(algo_dir, 'main.py')})
    return metadata
