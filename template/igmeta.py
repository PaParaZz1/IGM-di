from rich import print
from tabulate import tabulate
from igm.conf import igm_project, cpy, cpip


def info():
    print('This is the IGM generated project of DI-engine:')
    headers = ['Env\Algo'] + {{user.algo}}
    data = []
    for k in {{user.env}}:
        tmp = [k] + ['Available'] * len({{user.algo}})
        data.append(tmp)
    info = tabulate(data, headers=headers, tablefmt='grid')
    print(info)
    print({{user.doc | potc}})


igm_project(
    name='IGM-ding-demo',
    version='0.0.1',
    template_name={{template.name | potc}},
    template_version={{template.version | potc}},
    created_at={{py.time.time() | potc}},
    scripts={
        None: cpy('main.py'),
        'info': info,
        'tbviz': 'tensorboard --logdir=. --bind_all',
        'install': cpip('install', '-r', 'requirements.txt'),
    }
)
