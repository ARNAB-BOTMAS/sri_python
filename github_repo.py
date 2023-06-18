import git

# Specify the path to your local repository
repo_path = "D:\New folder\sri_python"

# Open the repository
repo = git.Repo(repo_path)

# Add all files to the staging area
repo.git.add(all=True)

# Commit the changes
commit_message = "Automatic commit"
repo.index.commit(commit_message)

# Push the changes to the remote repository
origin = repo.remote(name='origin')
origin.push()
