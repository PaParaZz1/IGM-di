import re
from rich import print
from InquirerPy import inquirer
from InquirerPy.validator import PathValidator, EmptyInputValidator

from igm.conf import InquireRestart
from igm.env import env
from igmdi.data import env_choices, algo_choices, subenv_choices, env_doc_link, algo_doc_link
from igmdi.utils import pretty_print
from igmdi.runnable import generate_runnable_entry


def seed_filter(s):
    if s[-1] == ',':
        s = s[:-1]
    try:
        return [
            int(s),
        ]
    except:  # noqa
        return [int(t) for t in s.strip().split(',')]


LAST_ENV, LAST_ALGO = None, None


def env_query():
    global LAST_ENV
    if LAST_ENV is not None:
        default_value = list(LAST_ENV.keys())
    else:
        default_value = None
    di_env = env.LAST_ENV or inquirer.rawlist(
        message="Pick your env:",
        choices=env_choices,
        multiselect=True,
        default=default_value,
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
    # view = inquirer.select(
    #     message="Select user view:",
    #     choices=[
    #         "Normal View",
    #         "Algorithm View",
    #         "Environment View",
    #     ],
    #     validate=EmptyInputValidator,
    # ).execute()
    view = "Normal View"

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
        seed = inquirer.text(
            message="Please indicate the random seed list for each experiment:",
            default="0",
            filter=seed_filter,
            validate=lambda s: re.match("\d(,\d)*", s),
            invalid_message="Please use correct format, e.g. 0,1,3"
        ).execute()
        hpo = inquirer.confirm(
            message="Do you want to run your experiment with HPO (Hyper-Parameters Optimization)?", default=False
        ).execute()
        if hpo:
            raise NotImplementedError
    else:
        seed = [
            0,
        ]
        hpo = False
    metadata = {
        'env': di_env,
        'algo': algo,
        'seed': seed,
    }
    confirm_instruction = "\n" + pretty_print({'metadata': metadata}) + "(Y/n)"
    confirm = inquirer.confirm(
        message="Do you confirm the following project setting:",
        default=True,
        instruction=confirm_instruction,
    ).execute()

    print("Your DI-engine project has started, you can refer to following link for more related information:")
    for item in di_env:
        print("\tEnv doc of '{}': {}".format(item, env_doc_link[item]))
    for item in algo:
        print("\tAlgo doc of '{}': {}".format(item, algo_doc_link[item]))

    if env.NON_CONFIRM:
        confirm = True
    else:
        confirm = inquirer.confirm(message="Customize your DI-engine project, confirm?").execute()

    if confirm:
        return generate_runnable_entry(metadata)
    else:
        # save this time's fillings
        LAST_ENV, LAST_ALGO = di_env, algo
        raise InquireRestart('Not confirmed.')
