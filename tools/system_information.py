import platform

def system_information():
    system = platform.system()

    version = platform.version()

    architecture = platform.architecture()

    hostname = platform.node()

    print(f"OS: {system}")

    print(f"OS Version: {version}")

    print(f"Architecture: {architecture}")

    print(f"Hostname: {hostname}")