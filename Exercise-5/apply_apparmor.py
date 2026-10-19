
import docker
import time
import urllib.request

client = docker.from_env()

print("Building Docker image...")
client.images.build(path=".", tag="flask-apparmor")

container = None

try:
    print("Starting Flask container...")

    container = client.containers.run(
        "flask-apparmor",
        ports={"5000/tcp": 8089},
        security_opt=["apparmor=my-apparmor-profile"],
        detach=True
    )

    print("Container started:", container.short_id)

    # Verify the security options
    info = client.api.inspect_container(container.id)
    print("Security options:", info["HostConfig"]["SecurityOpt"])

    time.sleep(2)

    container.reload()
    print("Container status:", container.status)

    with urllib.request.urlopen("http://localhost:8089", timeout=5) as response:
        print("Flask response:", response.read().decode())

finally:
    if container is not None:
        container.stop()
        container.remove()
        print("Container stopped and removed.")
