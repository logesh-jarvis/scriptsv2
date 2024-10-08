import concurrent.futures
import subprocess

def run_command(cmd):
    return subprocess.run(cmd, shell=True, capture_output=True)

with open("curl.txt", "r") as f:
    commands = f.readlines()
    commands = [x.strip() for x in commands]

with concurrent.futures.ThreadPoolExecutor() as executor:
    results = [executor.submit(run_command, cmd) for cmd in commands]
    for f in concurrent.futures.as_completed(results):
        print(f.result())
        print("")
