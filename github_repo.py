import os
import subprocess

def git():
    # Change to the directory where the Python file is located
    subprocess.run('git config --global user.email "arnabmondal203@gmail.com"', shell=True)
    subprocess.run('git config --global user.name "ARNAB-BOTMAS"', shell=True)
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    # Commit message
    commit_message = "Automatic commit"

    # Git commands
    git_commands = [
        "cls",
        "git add .",
        f'git commit -m "{commit_message}"',
        "git remote add origin https://github.com/ARNAB-BOTMAS/sri_python.git",
        "git push -u origin master"
    ]

    # Execute git commands
    for command in git_commands:
        subprocess.run(command, shell=True)

git()
