import yaml


def read_master():
    with open('../../scenarios/master.yml', 'r') as master:
        return yaml.safe_load(master)


def read_scenarios(master):
    scenarios = {}
    for scenario in master:
        with open('../../scenarios/scenarios/' + scenario['name'] + '.yml', 'r') as sc:
            scenarios[scenario['name']] = yaml.safe_load(sc)
    return scenarios


def get_scenarios():
    master = read_master()
    scenarios = read_scenarios(master)
    return {'master': master, 'scenarios': scenarios}
