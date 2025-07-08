import subprocess
import time
import json

def is_deployment_ready():
    try:
        output = subprocess.check_output(
            ["kubectl", "get", "deployment", "myapp", "-o", "json"],
            stderr=subprocess.STDOUT,
            text=True
        )
        data = json.loads(output)
        desired = data["status"].get("replicas", 1)
        available = data["status"].get("availableReplicas", 0)
        return available >= desired
    except subprocess.CalledProcessError as e:
        print("Error running kubectl:", e.output)
        return False

while not is_deployment_ready():
    print("Waiting for myapp to be ready...")
    time.sleep(10)

print("myapp is ready!")
