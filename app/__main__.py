from uptime_kuma_api import UptimeKumaApi
from utils import create_args, add_monitor


if __name__ == "__main__":
    args = create_args()

    with UptimeKumaApi(args.kuma_url) as api:
        api.login(args.kuma_username, args.kuma_password)
        add_monitor(
            api,
            args.monitor_type_str,
            args.name,
            hostname=args.hostname,
            url=args.url,
            docker_container_name=args.docker_container_name,
        )
