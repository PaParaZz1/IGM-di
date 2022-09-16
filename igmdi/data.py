from collections import defaultdict
from functools import reduce

env_choices = [
    'cartpole',
    'pendulum',
    'lunarlander',
    'bipedalwalker',
    'slime_volley',
    'atari',
    'mujoco',
    'dmcontrol',
    'gym_hybrid',
]
subenv_choices = {
    'atari': ['pong', 'qbert', 'spaceinvaders', 'enduro', 'breakout'],
    'mujoco': ['hopper', 'halfcheetah', 'walker2d'],
    'dmcontrol': ['cartpole_swingup'],
    'gym_hybrid': ['moving-v0', 'sliding-v0'],
    'mpe': ['simple_thread', 'simple_comm'],
}

env_id_mapping = {
    'cartpole': 'CartPole-v0',
    'pendulum': 'Pendulum-v1',
}

env_algo_mapping = {
    'cartpole': set(['dqn', 'rainbow', 'r2d2', 'a2c', 'ppo', 'impala']),
    'pendulum': set(['ddpg', 'td3', 'sac']),
}

algo_choices = [
    'dqn',
    'rainbow',
    'r2d2',
    'a2c',
    'ppo',
    'impala',
    'ddpg',
    'td3',
    'sac',
]
env_doc_link = {
    'cartpole': "https://di-engine-docs.readthedocs.io/zh_CN/latest/13_envs/cartpole_zh.html",
    'pendulum': "https://di-engine-docs.readthedocs.io/zh_CN/latest/13_envs/pendulum_zh.html",
    'lunarlander': 'https://di-engine-docs.readthedocs.io/zh_CN/latest/13_envs/lunarlander_zh.html',
    'bipedalwalker': 'https://di-engine-docs.readthedocs.io/zh_CN/latest/13_envs/bipedalwalker_zh.html',
    'slime_volley': "https://di-engine-docs.readthedocs.io/zh_CN/latest/13_envs/slime_volleyball_zh.html",
    'atari': 'https://di-engine-docs.readthedocs.io/zh_CN/latest/13_envs/atari_zh.html',
    'mujoco': 'https://di-engine-docs.readthedocs.io/zh_CN/latest/13_envs/mujoco_zh.html',
    'dmcontrol': 'https://di-engine-docs.readthedocs.io/zh_CN/latest/13_envs/dmc2gym_zh.html',
    'gym_hybrid': "https://di-engine-docs.readthedocs.io/zh_CN/latest/13_envs/gym_hybrid_zh.html",
}
algo_doc_link = defaultdict(list)
algo_doc_link.update(
    {
        "dqn": "https://di-engine-docs.readthedocs.io/zh_CN/latest/12_policies/dqn_zh.html",
        # "c51": "https://di-engine-docs.readthedocs.io/en/latest/12_policies/c51.html",
        # "qrdqn": "https://di-engine-docs.readthedocs.io/en/latest/12_policies/qrdqn.html",
        "rainbow": "https://di-engine-docs.readthedocs.io/en/latest/12_policies/rainbow.html",
        # "sql": "https://di-engine-docs.readthedocs.io/en/latest/12_policies/sql.html",
        "r2d2": "https://di-engine-docs.readthedocs.io/en/latest/12_policies/r2d2.html",
        "a2c": "https://di-engine-docs.readthedocs.io/en/latest/12_policies/a2c.html",
        "ppo": "https://di-engine-docs.readthedocs.io/en/latest/12_policies/ppo.html",
        "impala": "https://di-engine-docs.readthedocs.io/en/latest/12_policies/impala.html",
        "ddpg": "https://di-engine-docs.readthedocs.io/en/latest/12_policies/ddpg.html",
        "td3": "https://di-engine-docs.readthedocs.io/en/latest/12_policies/td3.html",
        "sac": "https://di-engine-docs.readthedocs.io/en/latest/12_policies/sac.html",
    }
)


def filter_algo_choices(env, mode='intersection'):
    env = list(env.keys())
    sets = []
    for e in env:
        sets.append(env_algo_mapping[e])
    if mode == 'intersection':
        return reduce(lambda x, y: x.intersection(y), sets)
    else:
        raise KeyError("not support mode: {}".format(mode))
