import yaml


def process_yml(yaml_file, docker_composes_key="docker_composes"):
    with open(yaml_file, "r") as yaml_file:
        yaml_data = yaml.safe_load(yaml_file)

    docker_composes = yaml_data[docker_composes_key]

    container_name_list = []
    for key in docker_composes.keys():
        container_name_list.append(key)
    return container_name_list
