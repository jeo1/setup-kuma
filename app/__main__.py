from uptime_kuma_api import UptimeKumaApi
from utils import create_args, add_monitor, process_yml


if __name__ == "__main__":
    args = create_args()

    container_name_list = []
    if args.yaml_file != None:
        container_name_list = process_yml(args.yaml_file)

    with UptimeKumaApi(args.kuma_url) as api:
        if len(container_name_list) == 0:
            api.login(args.kuma_username, args.kuma_password)
            add_monitor(
                api,
                args.monitor_type_str,
                args.name,
                hostname=args.hostname,
                url=args.url,
                docker_container_name=args.docker_container_name,
            )
