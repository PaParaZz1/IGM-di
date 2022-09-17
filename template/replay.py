import os
from ding.entry import eval

if __name__ == "__main__":
    replay_dir = 'replay_videos'
    experiment_list = [os.path.dirname(t['dst']) for t in {{user.task_path | potc}}]
    seed = {{user.seed}}[0]  # only replay first seed
    for item in experiment_list:
        dirname, algo = os.path.split(item)
        dirname, env = os.path.split(dirname)

        dirname = '{}_{}_seed{}'.format(env, algo, seed)
        ckpt_name = os.path.join(item, dirname, 'ckpt', 'ckpt_best.pth.tar')
        replay_name = os.path.join(replay_dir, dirname)
        if len({{user.seed}}) > 1:
            config_path = os.path.join(item, 'main_seed{}.py'.format(seed))
        else:
            config_path = os.path.join(item, 'main.py')
        eval(config_path, seed=seed, load_path=ckpt_name, replay_path=replay_name)
        # clean dir
        os.popen('rm -rf {}*'.format(env))
        os.popen('rm -rf default_experiment')
        os.popen('cd {} && rm -rf *.json'.format(replay_name))
        video_list = [
            os.path.join(replay_name, item) for item in os.listdir(replay_name) if os.path.splitext(item)[1] == '.mp4'
        ]
        video_size = [os.path.getsize(item) for item in video_list]
        if max(video_size) > min(video_size) * 5:
            threshold = min(video_size) * 2
            invalid_video_list = [item for item in video_list if os.path.getsize(item) < threshold]
            for item in invalid_video_list:
                os.popen('rm -rf {}'.format(item))
