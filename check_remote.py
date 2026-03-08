#!/usr/bin/env python3
import subprocess
import os

os.chdir('/Users/simhadrinandagopal/Desktop/EchoBridge')

# Check remote URL
result = subprocess.run(['git', 'remote', '-v'], capture_output=True, text=True)
with open('/Users/simhadrinandagopal/Desktop/EchoBridge/git_output.txt', 'a') as f:
    f.write("\n\nREMOTE URL:\n")
    f.write(result.stdout)
    f.write(result.stderr)

