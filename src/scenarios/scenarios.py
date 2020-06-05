import os

import yaml

dir_path = os.path.dirname(os.path.realpath(__file__))


def read_master():
    with open(f'{dir_path}/../../scenarios/master.yml', 'r') as master:
        return yaml.safe_load(master)


def read_scenarios(master):
    s = {}
    for scenario in master:
        with open(f'{dir_path}/../../scenarios/scenarios/{scenario["name"]}.yml', 'r') as sc:
            s[scenario['name']] = yaml.safe_load(sc)
    return s


def get_scenarios():
    master = read_master()
    s = read_scenarios(master)
    return {'master': master, 'individual': s}


scenarios = get_scenarios()
