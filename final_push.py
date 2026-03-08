#!/usr/bin/env python3
import subprocess
import os

os.chdir('/Users/simhadrinandagopal/Desktop/EchoBridge')

# Add all files
subprocess.run(['git', 'add', '-A'], capture_output=True)

# Commit
result = subprocess.run(['git', 'commit', '-m', 'Add push scripts'], capture_output=True, text=True)

# Push
result = subprocess.run(['git', 'push', 'origin', 'main'], capture_output=True, text=True)

with open('/Users/simhadrinandagopal/Desktop/EchoBridge/git_output.txt', 'w') as f:
    f.write("COMMIT:\n")
    f.write("STDOUT: " + result.stdout)
    f.write("STDERR: " + result.stderr)
    f.write("Return code: " + str(result.returncode))
    
print("Done")

