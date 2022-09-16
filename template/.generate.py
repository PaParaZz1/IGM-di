import os
import shutil
from igm.render import igm_script
from igm.env import user
from extras import project_dir


@igm_script
def generate_experiment():
    for item in user.task_path:
        src, dst = item['src'], item['dst']
        dst_dir = os.path.dirname(dst)
        dst_dir = os.path.join(project_dir, dst_dir)
        os.makedirs(dst_dir)
        shutil.copy(src, dst)
