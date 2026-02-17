#!/usr/bin/env python3
import subprocess
import os

os.chdir('/Users/simhadrinandagopal/Desktop/EchoBridge')

# Initialize git repo if not exists
subprocess.run(['git', 'init'], capture_output=True)

# Add all files
subprocess.run(['git', 'add', '-A'], capture_output=True)

# Commit
result = subprocess.run(['git', 'commit', '-m', 'Initial commit - Emotion Connection System'], capture_output=True, text=True)
print("Commit result:", result.returncode)
print("Stdout:", result.stdout)
print("Stderr:", result.stderr)

# Set branch to main
subprocess.run(['git', 'branch', '-M', 'main'], capture_output=True)

# Set remote
subprocess.run(['git', 'remote', 'set-url', 'origin', 'https://github.com/AP24110010511/emotion-connection-system.git'], capture_output=True)

# Push
result = subprocess.run(['git', 'push', '-u', 'origin', 'main'], capture_output=True, text=True)
print("Push result:", result.returncode)
print("Stdout:", result.stdout)
print("Stderr:", result.stderr)

# Write status
with open('/tmp/py_status.txt', 'w') as f:
    f.write(f"Done! Return code: {result.returncode}\n")
    f.write(f"Output: {result.stdout}\n")
    f.write(f"Error: {result.stderr}\n")

