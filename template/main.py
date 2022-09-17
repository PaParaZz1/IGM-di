import os
import subprocess
import sys

from tqdm import tqdm

if __name__ == "__main__":
    experiment_list = [os.path.dirname(t['dst']) for t in {{user.task_path | potc}}]
    for path in tqdm(experiment_list,
                     desc="DI-engine experiment with {} x {}".format({{user.env | potc}}, {{user.algo | potc}})):
        with open(os.path.join(path, 'output.txt'), "w") as outfile:
            subprocess.run(f"cd {path!r} && {sys.executable!r} -u main.py",
                           shell=True, stdout=outfile, stderr=outfile)
