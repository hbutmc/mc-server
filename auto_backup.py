import os
import subprocess
from datetime import datetime

CONTAINER_NAME = "hbutmc"
SERVER_PATH = "/srv/hbutmc/"

os.chdir(SERVER_PATH)

subprocess.run(["docker", "stop", CONTAINER_NAME])

time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

subprocess.run(["tar", "-czf", f"backup/{time}.tar.gz", "world/", "world_nether/", "world_the_end/"])

subprocess.run(["docker", "start", CONTAINER_NAME])
