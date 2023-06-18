import os
import subprocess
import urllib.parse

def git():
    # Change to the directory where the Python file is located
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    # Initialize a Git repository
    subprocess.run('git init', shell=True)

    # Set Git configuration
    subprocess.run('git config --global user.email "arnabmondal203@gmail.com"', shell=True)
    subprocess.run('git config --global user.name "ARNAB-BOTMAS"', shell=True)

    # Commit message
    commit_message = "Automatic commit"

    # Git commands
    git_commands = [
        "git add .",
        f'git commit -m "{commit_message}"',
        f'git remote add origin https://github.com/ARNAB-BOTMAS/sri_python.git',
        f'git config --local credential.helper "!f() {{ echo username=ARNAB-BOTMAS; echo password=$1; }}; f"',
        "git push -u origin main"
    ]

    # Execute git commands
    for command in git_commands:
        subprocess.run(command, shell=True, check=True, input="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".encode())

git()
