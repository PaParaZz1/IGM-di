from rich import print
from InquirerPy import inquirer
from InquirerPy.validator import PathValidator, EmptyInputValidator

from igm.conf import InquireRestart
from igm.env import env
from igmdi.data import env_choices, algo_choices, subenv_choices, env_doc_link, algo_doc_link
from igmdi.utils import pretty_print

LAST_ENV, LAST_ALGO = None, None


def env_query():
    global LAST_ENV
    di_env = env.LAST_ENV or inquirer.rawlist(
        message="Pick your env:",
        choices=env_choices,
        multiselect=True,
        instruction="\nPress <Enter> to submit, <Space> to multi-select",
    ).execute()
    di_env = {k: None for k in di_env}
    for item in di_env:
        if item in subenv_choices:
            subenv = inquirer.rawlist(
                message="Pick your subenv of {}:".format(item),
                choices=subenv_choices[item],
                multiselect=True,
                instruction="\nPress <Enter> to submit, <Space> to multi-select",
            ).execute()
            di_env[item] = subenv
    return di_env


def algorithm_query():
    global LAST_ALGO
    algo = env.LAST_ALGO or inquirer.rawlist(
        message="What's your algorithm:",
        choices=algo_choices,
        multiselect=True,
        default=LAST_ALGO,
        instruction="\nPress <Enter> to submit, <Space> to multi-select",
    ).execute()
    return algo


def inquire_func():
    global LAST_ENV, LAST_ALGO
    print('We are trying to create a project to use DI-engine')
    view = inquirer.select(
        message="Select user view:",
        choices=[
            "Normal View",
            "Algorithm View",
            "Environment View",
        ],
        default=LAST_ENV,
        validate=EmptyInputValidator,
    ).execute()

    if view == "Algorithm View":
        algo = algorithm_query()
    elif view == "Environment View":
        di_env = env_query()
    elif view == "Normal View":
        di_env = env_query()
        algo = algorithm_query()

    mode = inquirer.select(
        message="Select mode:",
        choices=[
            "Default Mode",
            "Customized Mode",
        ],
        validate=EmptyInputValidator,
    ).execute()

    if mode == 'Customized Mode':
        exp_dir = inquirer.filepath(
            message="Enter experiment directory filepath:",
            default="./",
            validate=PathValidator(is_dir=True, message="Input is not a directory"),
            only_directories=True,
        ).execute()
        multi_seed = inquirer.confirm(
            message="Do you want to run your experiment with several random seeds (default: 1-3)?", default=False
        ).execute()
        hpo = inquirer.confirm(
            message="Do you want to run your experiment with HPO (Hyper-Parameters Optimization)?", default=False
        ).execute()
        if hpo:
            raise NotImplementedError
    else:
        exp_dir = "./"
        multi_seed = False
        hpo = False
    metadata = {
        'env': di_env,
        'algo': algo,
        'exp_dir': exp_dir,
        'multi_seed': multi_seed,
    }
    confirm_instruction = "\n" + pretty_print({'metadata': metadata}) + "(Y/n)"
    confirm = inquirer.confirm(
        message="Do you confirm the following experiment setting:",
        default=True,
        instruction=confirm_instruction,
    ).execute()

    print(
        "Your DI-engine project has started in '{}', you can refer to following link for more related information:".
        format(exp_dir)
    )
    for item in di_env:
        print("\tenv doc of '{}': {}".format(item, env_doc_link[item]))
    for item in algo:
        print("\talgo doc of '{}': {}".format(item, algo_doc_link[item]))

    if env.NON_CONFIRM:
        confirm = True
    else:
        confirm = inquirer.confirm(message=f"Customize your DI-engine project, confirm?").execute()

    if confirm:
        return metadata
    else:
        # save this time's fillings
        LAST_ENV, LAST_ALGO = di_env, algo
        raise InquireRestart('Not confirmed.')
