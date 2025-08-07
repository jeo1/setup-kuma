import argparse


def create_args():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-t",
        "--monitor_type_str",
        type=str,
        help="Monitor type. Currently supported types are: ping, https, docker",
    )
    parser.add_argument(
        "-n",
        "--name",
        type=str,
    )
    parser.add_argument(
        "-hn",
        "--hostname",
        default=None,
        type=str,
    )
    parser.add_argument(
        "-u",
        "--url",
        default=None,
        type=str,
    )
    parser.add_argument(
        "-d",
        "--docker_container_name",
        type=str,
    )

    parser.add_argument(
        "-y",
        "--yaml_file",
        default=None,
        type=str,
        help="var_docker_deploy.yml yaml file, which used to get docker container names.",
    )

    parser.add_argument("--kuma_url")
    parser.add_argument("--kuma_username")
    parser.add_argument("--kuma_password")

    args = parser.parse_args()

    return args
