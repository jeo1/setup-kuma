from uptime_kuma_api import UptimeKumaApi
from utils import create_args, add_monitor, process_yml


if __name__ == "__main__":
    args = create_args()

    container_name_list = []
    if args.yaml_file != None:
        container_name_list = process_yml(args.yaml_file)
    container_name_list += args.other_container_names

    with UptimeKumaApi(args.kuma_url) as api:
        api.login(args.kuma_username, args.kuma_password)
        if len(container_name_list) == 0:
            add_monitor(
                api,
                args.monitor_type_str,
                args.name,
                hostname=args.hostname,
                url=args.url,
                docker_container_name=args.docker_container_name,
            )
        else:
            for container_name in container_name_list:
                monitor_type_str = "docker"
                name = "docker-{}".format(container_name)
                add_monitor(
                    api, monitor_type_str, name, docker_container_name=container_name
                )
