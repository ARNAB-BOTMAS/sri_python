import os
import subprocess

<<<<<<< HEAD
=======
# Run git config commands to set user email and name
subprocess.run('git config --global user.email "arnabmondal203@gmail.com"', shell=True)
subprocess.run('git config --global user.name "ARNAB-BOTMAS"', shell=True)

>>>>>>> a1ba1f29127802128a443043209b1b9f64550d6d
def git():
    # Change to the directory where the Python file is located
    subprocess.run('git config --global user.email "arnabmondal203@gmail.com"', shell=True)
    subprocess.run('git config --global user.name "ARNAB-BOTMAS"', shell=True)
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    # Commit message
    commit_message = "Automatic commit"

    # Git commands
    git_commands = [
        "git add .",
        f'git commit -m "{commit_message}"',
<<<<<<< HEAD
        "git push -u origin main"
=======
        "git remote add origin https://github.com/ARNAB-BOTMAS/sri_python.git",  # Replace <remote_url> with the actual remote URL
        "git push -u origin master"
>>>>>>> a1ba1f29127802128a443043209b1b9f64550d6d
    ]

    # Execute git commands
    for command in git_commands:
        subprocess.run(command, shell=True)

git()
