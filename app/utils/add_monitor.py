from uptime_kuma_api import MonitorType, DockerType


def _add_monitor_ping(api, name, hostname):
    monitor_list = api.get_monitors()
    for monitor in monitor_list:
        if monitor["type"] == MonitorType.PING:
            id = monitor["id"]
            if monitor["name"] == name:
                if monitor["hostname"] == hostname:
                    return
                else:
                    api.edit_monitor(id, hostname=hostname)
                    return
    api.add_monitor(type=MonitorType.PING, name=name, hostname=hostname)


def _add_monitor_http(api, name, url, ignoreTls=True):
    monitor_list = api.get_monitors()
    for monitor in monitor_list:
        if monitor["type"] == MonitorType.HTTP:
            id = monitor["id"]
            if monitor["name"] == name:
                if monitor["url"] == url:
                    return
                else:
                    api.edit_monitor(id, url=url)
                    return
    api.add_monitor(type=MonitorType.HTTP, name=name, url=url, ignoreTls=ignoreTls)


def _get_docker_host_id(
    api, docker_hostname="docker", dockerDaemon="/var/run/docker.sock"
):
    docker_host_list = api.get_docker_hosts()
    # Check for existing docker host
    for docker_host in docker_host_list:
        if dockerDaemon == docker_host["dockerDaemon"]:
            return docker_host["id"]

    # Create new docker host
    docker_host = api.add_docker_host(
        name=docker_hostname, dockerType=DockerType.SOCKET, dockerDaemon=dockerDaemon
    )
    return docker_host["id"]


def _add_monitor_docker(
    api, name, docker_container_name, dockerDaemon="/var/run/docker.sock"
):
    monitor_list = api.get_monitors()
    docker_host_id = _get_docker_host_id(api, dockerDaemon=dockerDaemon)
    for monitor in monitor_list:
        if monitor["type"] == MonitorType.DOCKER:
            id = monitor["id"]
            if monitor["name"] == name:
                if monitor["docker_container"] == docker_container_name:
                    return
                else:
                    api.edit_docker_host(id, docker_container=docker_container_name)
    api.add_monitor(
        type=MonitorType.DOCKER,
        name=name,
        docker_container=docker_container_name,
        docker_host=docker_host_id,
    )


def add_monitor(
    api,
    monitor_type_str,
    name,
    hostname=None,
    url=None,
    docker_container_name=None,
    ignoreTls=True,
    dockerDaemon="/var/run/docker.sock",
):
    monitor_type = monitor_type_str.lower()
    if monitor_type == "ping" and hostname != None:
        _add_monitor_ping(api, name, hostname)
    elif monitor_type == "http" and url != None:
        _add_monitor_http(api, name, url, ignoreTls=ignoreTls)
    elif monitor_type == "docker" and docker_container_name != None:
        _add_monitor_docker(api, name, docker_container_name, dockerDaemon=dockerDaemon)
