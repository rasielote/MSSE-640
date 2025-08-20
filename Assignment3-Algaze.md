##  Configuration
How do you set your Git name and email? Should it be global or just in one repo? Why?  
If you want Git to use your name and email for every repo on your computer, use global. But if you're working on a project for someone else, you can change it just in that repo (local).
### Set your Git username and email globally:
```
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

### Set them locally for a specific repo:
```
git config user.name "Other Name"
git config user.email "other@example.com"
```

### Set the core editor (example: VS Code):
```
git config --global core.editor "code --wait"
```

### View your config settings:
```
git config --global --list
git config --local --list
```

---

##  Working with a Local Repo

### Create a new local repository:
```
mkdir my-repo
cd my-repo
git init
```

### Clone an existing repository:
```
git clone https://github.com/user/repo.git
```

### Check the status of your repo:
```
git status
```

### Stage changes:
```
git add file.txt     # Stages one file
git add .            # Stages everything
```

### Commit changes:
```
git commit -m "Your message here"
```

### Example `.gitignore` file:
```
# .gitignore
*.log
node_modules/
.env
```

### Delete a file with Git:
```
git rm filename.txt
git commit -m "Remove file"
```

---

##  Working with a Remote

### View the remote repo:
```
git remote -v
```

### Fetch updates from the remote:
```
git fetch
```

### Pull updates and merge them:
```
git pull
```

### Push local changes to the remote:
```
git add .
git commit -m "Update something"
git push origin main
```

---

## Branches

### View local and remote branches:
```
git branch      # Local
git branch -r   # Remote
git branch -a   # All
```

### Create a new branch:
```
git branch new-feature
```

### Switch to a different branch:
```
git switch new-feature
# or
git checkout new-feature
```

### Delete a local branch:
```
git branch -d new-feature
git branch   # To confirm it's gone