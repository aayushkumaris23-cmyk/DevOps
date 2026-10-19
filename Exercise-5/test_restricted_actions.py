
import docker
import time

client = docker.from_env()
container = None

try:
    print("Starting Flask container with AppArmor profile...")

    container = client.containers.run(
        "flask-apparmor",
        ports={"5000/tcp": 8089},
        security_opt=["apparmor=my-apparmor-profile"],
        detach=True
    )

    print("Container started:", container.short_id)
    time.sleep(2)

    container.reload()
    print("Container status:", container.status)

    # Verify the configured security options
    info = client.api.inspect_container(container.id)
    print("Security options:", info["HostConfig"]["SecurityOpt"])

    # Test reading /etc/passwd
    print("\nTesting access to /etc/passwd...")
    exit_code, output = container.exec_run(
        ["cat", "/etc/passwd"]
    )

    print("Attempt to read /etc/passwd:")
    print("Exit Code:", exit_code)
    print("Output:", output.decode(errors="replace").strip())

    # Test executing /bin/bash
    print("\nTesting execution of /bin/bash...")
    exit_code, output = container.exec_run(
        ["/bin/bash", "-c", "echo BASH_EXECUTED"]
    )

    print("Attempt to execute /bin/bash:")
    print("Exit Code:", exit_code)
    print("Output:", output.decode(errors="replace").strip())

finally:
    if container is not None:
        try:
            container.stop()
            print("\nContainer stopped.")
        finally:
            container.remove()
            print("Container removed.")
