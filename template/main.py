import os
import subprocess
from tqdm import tqdm

if __name__ == "__main__":
    experiment_list = [os.path.dirname(t['dst']) for t in {{user.task_path}}]
    for path in tqdm(experiment_list, desc="DI-engine experiment with {} x {}".format({{user.env}}, {{user.algo}})):
        with open(os.path.join(path, 'output.txt'), "w") as outfile:
            subprocess.run("cd {} && python3 -u main.py".format(path), shell=True, stdout=outfile, stderr=outfile)
