from igm.conf import igm_project, cpy, cpip


def info():
    print('This is the project of DI-engine.')


igm_project(
    name='IGM-ding-demo',
    version='0.0.1',
    template_name={{template.name | potc}},
    template_version={{template.version | potc}},
    created_at={{py.time.time() | potc}},
    scripts={
        None: cpy('main.py'),
        'info': info,
        'install': cpip('install', '-r', 'requirements.txt'),
    }
)
