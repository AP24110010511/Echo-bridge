#!/bin/bash
cd /Users/simhadrinandagopal/Desktop/EchoBridge

# Check if this is a git repo
if [ ! -d ".git" ]; then
    git init
fi

# Add all files
git add -A

# Commit
git commit -m "Initial commit - Emotion Connection System"

# Set branch to main
git branch -M main

# Set remote
git remote set-url origin https://github.com/AP24110010511/emotion-connection-system.git

# Push
git push -u origin main

echo "Done!" > /tmp/status.txt

