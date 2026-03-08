#!/usr/bin/env python3
import subprocess
import os

os.chdir('/Users/simhadrinandagopal/Desktop/EchoBridge')

# Set up remote
subprocess.run(['git', 'remote', 'add', 'origin', 'https://github.com/AP24110010511/Echo-bridge.git'], capture_output=True)

# Push
result = subprocess.run(['git', 'push', '-u', 'origin', 'main'], capture_output=True, text=True)
print("STDOUT:", result.stdout)
print("STDERR:", result.stderr)
print("Return code:", result.returncode)

