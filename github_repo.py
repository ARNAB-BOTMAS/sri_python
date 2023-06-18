import os
import subprocess

# Change to the directory where the Python file is located
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Commit message
commit_message = "Automatic commit"

# Git commands
git_commands = [
    "git add .",
    f'git commit -m "{commit_message}"',
    "git push"
]

# Execute git commands
for command in git_commands:
    subprocess.run(command, shell=True)
