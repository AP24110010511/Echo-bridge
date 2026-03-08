#!/usr/bin/env python3
import subprocess
import os

os.chdir('/Users/simhadrinandagopal/Desktop/EchoBridge')

# First, let's see the git status
result = subprocess.run(['git', 'status'], capture_output=True, text=True)
with open('/Users/simhadrinandagopal/Desktop/EchoBridge/git_output.txt', 'w') as f:
    f.write("GIT STATUS:\n")
    f.write(result.stdout)
    f.write(result.stderr)

# Add and set remote
subprocess.run(['git', 'remote', 'add', 'origin', 'https://github.com/AP24110010511/Echo-bridge.git'], capture_output=True)
subprocess.run(['git', 'remote', 'set-url', 'origin', 'https://github.com/AP24110010511/Echo-bridge.git'], capture_output=True)

# Push
result = subprocess.run(['git', 'push', '-u', 'origin', 'main'], capture_output=True, text=True)
with open('/Users/simhadrinandagopal/Desktop/EchoBridge/git_output.txt', 'a') as f:
    f.write("\nGIT PUSH:\n")
    f.write("STDOUT: " + result.stdout)
    f.write("STDERR: " + result.stderr)
    f.write("Return code: " + str(result.returncode))

print("Done. Check git_output.txt")

