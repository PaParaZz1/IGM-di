from collections import defaultdict

env_choices = [
    'cartpole',
    'pendulum',
    'mpe',
    'slime_volley',
    'gym_hybrid',
]
subenv_choices = {
    'mpe': ['simple_thread', 'simple_comm'],
    'gym_hybrid': ['moving-v0', 'sliding-v0'],
}

algo_choices = [
    'dqn',
    'c51',
    'r2d2',
    'a2c',
    'ppo',
    'ppg',
    'ddpg',
    'td3',
    'sac',
]
env_doc_link = {
    'cartpole': "https://di-engine-docs.readthedocs.io/zh_CN/latest/13_envs/cartpole_zh.html",
    'pendulum': "https://di-engine-docs.readthedocs.io/zh_CN/latest/13_envs/pendulum_zh.html",
    'mpe': "https://di-engine-docs.readthedocs.io/zh_CN/latest/13_envs/multiagent_particle_zh.html",
    'slime_volley': "Empty",
    'gym_hybrid': "https://di-engine-docs.readthedocs.io/zh_CN/latest/13_envs/gym_hybrid_zh.html",
}
algo_doc_link = defaultdict(list)
algo_doc_link.update(
    {
        "dqn": "https://di-engine-docs.readthedocs.io/zh_CN/latest/12_policies/dqn_zh.html",
        "c51": "https://di-engine-docs.readthedocs.io/en/latest/12_policies/c51.html",
        "sac": "https://di-engine-docs.readthedocs.io/en/latest/12_policies/sac.html",
    }
)
