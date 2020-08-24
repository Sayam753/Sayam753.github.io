# Git

1. Git is a distributed version control system.
2. Svn is a central control system.
3. In central control system, all the files are stored in the server's database. In distributed vcs, everybody has a local repository.
4. There are three areas -

   - `Working Directory` - Where we put up all the files and codes in the local repository. We need to add them.
   - `Staging Area` - Where we commit our files
   - `Repo` - Contains all the files



## Basic Commands -

```bash
git --version
git config --global user.name "<user-name>"
git config --global user.email "<user-email-ID>"
git config --global --list
git config --local --list
git help <verb>
git <verb> --help
git init  # For initialising a repository with git
rm -rf .git  # To stop tracking
touch .gitignore  # To put all the unwanted files which we do not want to git
git remote -v  # Info about remote repo
```

#### To Save changes -

```bash
git status
git add -A  # Adds files to staging area
git commit -m "Message"
git pull origin master  # If remote is set
git push origin master
```

#### To create a new git repo with existing code -

```bash
git init  # In the folder. Also create a new repo in GitHub
git add -A
git commit -m "message"
git remote add origin link_to_repo
git push -u origin master
```



## Branches -

Common Overflow - create a branch for desire feature

```bash
git branch  # To check the current branch
git branch my_branch  # To initialise a branch
git checkout my_branch  # To change the branch
git checkout -b my_branch  # Single command for above two operations
```

After adding and commiting, push branch to remote

```bash
git push -u origin my_branch  # To create a separate branch in the repo with the modified changes
git branch -a  # Check all branches at local as well as remote repo
```

#### Merge a branch -

```bash
git checkout master
git pull origin master
git branch --merged
git merge my_branch
git push origin master
```

#### Delete a branch -

```bash
git branch --merged  # To check if everything is merged correctly
git branch -d my_branch  # Deleted locally
git branch -D my_branch  # Delete branch forcefully, if not merged
git branch -a  # To check
git push origin --delete my_branch
```



## Fixing Mistakes and Bad Commits

#### To rename a message after a commit - 

But this changes the hash of the commit as the hash depends of message. This also changes the git history so it is not a good option.

```bash
git commit --amend -m "Added add function"
```

#### To add a file to previous commit - 

First add that file to staging area. This again changes the git history.

```bash
touch new.py
git add new.py
git commit --amend  # Amend the file to last commit. Vim is opened asking for any changes in commit message. OR
git commit --amend --no-edit  # To keep the last commit message same
git log --stat  # To see changes in a commit
```

#### Move a commit to different branch -

1. Copy the `hash` of commit you want to move - 

   ```bash
   git checkout <branch-name>
   git cherry-pick <hash-of-commit>  # The changes are reflected but the commit hash is changed
   ```

2. Remove that `commit` from previous branch - 

   ```bash
   # Remove from branch
   git checkout <branch-name>
   
   # Three different types of reset -
   git reset --soft <previous-commit-hash-of-branch>  # It will keep the changes in staging area.
   git reset <previous-commit-hash-of-branch>  # Mixed reset - It will keep the changes in the working directory.
   git reset --hard <previous-commit-hash-of-branch>  # Remove all the changes from tracked files. All new files added will be there in working directory. Untracked files are left
   ```

   **Warning**- Use of `git reset --hard`, will reset to `previous commit` only when files are staged or commited. If they are in working directory, git reset --hard will reset only tracked files.

3. To delete untracked files/directories forcefully - 

   ```bash
   git clean -df
   ```

4. Retrieve critical files that were lost, and you want them back -

   ```bash
   git reflog  # Copy the hash
   git checkout <hash-copied-from-reflog>  # Now the head is detached. You need to create a branch if you want those changes
   git branch backup  # Create a backup branch
   ```

#### Git revert

Creates new commit on top of earlier commits to revert the changes.

```bash
git revert <hash-of-commit>
```



## Using stash command

Git stash helps when you have some uncommitted changes. You want to revert or switch between branches. Stash will temporarily save your changes.

1. Save you changes before moving around.

   ```bash
   git stash save "Message for your changes"
   git stash save -u "Message for your changes"  # For including all untracked as well
   git stash save --all "Message for your changes"  # For including all untracked and ignored files as well
   git stash list  # To list out all our stashes
   ```

2. Explore whatever you wish like.

3. View the contents of the stash

   ```bash
   git stash show -p  # For latest stash
   git stash show -p stash:{index}  # For a particular stash
   ```

4. Get those changes back

   1. Use `git stash apply`

      ```bash
      git stash apply  # To apply the latest stash
      git stash apply stash:{index}  # To see the changes OR
      git stash list  # But it does not get rid of the stash
      git checkout -- .  # To return to spec
      ```

   2. Use `git stash pop`

      ```bash
      git stash pop  # Applies the changes of topmost in git stash list and remove that one OR
      git stash pop stash:{index}  # Apply and delete
      git stash list  # That stash has been removed
      ```

5. Let's suppose now you do not want to keep that changes.

   1. Drop a single stash - 

      ```bash
      git stash drop  # For topmost stash
      git stash drop stash:{index}  # For a specific stash
      ```

   2. Drop all stashes - 

      ```bash
      git stash clear
      git stash list  # Empty list
      ```

6. Stashes are carried from branch to branch -

   ```bash
   git stash save "Message"
   git checkout <branch_name>
   git stash pop
   ```

7. Create a new branch and apply that stash - The stash is also deleted.

   ```bash
   git stash branch <branch_name>  # For topmost stash
   git stash branch <branch_name> stash:{index}  # For a specific stash
   ```

**Note** - The `git stash save` API is deprecated in favour of new `git stash push` API from 2.16 version onwards.



## Different Types of git add -

1. Stage all the changes including untracked and .dot files, in the `entire working tree`

   ```bash
   git add --all
   git add --all <directory-name>  # It will only stage changes made in that directory
   git add <directory-name>  # --all or -A option is by default
   git add --no-all <directory-name>  # It will stage only modified and new files, not the deleted ones in directory
   ```

2. Stage only modified and deleted files, in the entire working directory, `-u` or `--update`

   ```bash
   git add -u
   git add -u <directory-name>  # It will stage only modified and deleted, not the new ones in the directory
   ```

3. Stage all the changes including untracked and .dot files, in the `current working directory and below` not the parent ones.

   ```bash
   git add .  # Changes will be visible if we run this command in any sub directory
   ```

4. Stage with * It will stage the files it can see in ls * - This is not recommended as its not including deleted as well as .dot files

   ```bash
   git add *
   ```



## Extras -

```bash
# List out the differences
git diff  # In working directory
git diff --staged  # In staging area
git diff hash1 hash2  # Between two commits via hashes

# Discard the changes in a working directory
git checkout <filename>  # For a single file
git checkout -- .  # All tracked files
git clean -df  # All untracked files

# Remove files from staging area and put them back into working directory
git reset <filename>  # For a single file
git reset  # To remove everything

# Newer APIs
git restore <filename>  # To discard changes in working directory
git restore --staged <filename>  # To unstage

# Logs
git log  # To check the various commits
git log -p  # Log with patches
git log -2  # For last 2 commits
git log --stat  # To see the changes
git log --oneline  # All commit messages in single line

# Show the changes done by a commit
git show  # For latest commit. This is equivalent to git log -p -1
git show <commit-hash>

# Alias
git config --global alias.<alias> <command>
git config --global alias.st status  # Typing git st will show results of git status

# Remote
git remote  # List of all remotes
git remote -v  # Be a little more verbose
git remote add <remote name> <url>  # To set a remote
git remote rename <oldname> <newname>  # To modify remote's name
git remote set-url <remote name> <url>  # To modify a remote's url
git remote rm <remote name>  # To delete a remote
# If we set-url or add a new remote, we need to do -
git fetch
git remote set-head <remote name> master
git push --set-upstream <remote name> master  # To track all the branches

# Rename
git mv <old filename> <new filename>  # Rename a file
git branch -m <newname>  # Rename a branch while working on branch
git branch -m <oldname> <newname>  # Rename a branch from outside the branch

# Signing commits
git config --global commit.gpgsign true
git config --global --edit  # To change the settings

# Forks
git remote add upstream <url>
git fetch upstream
git checkout master
git merge upstream/master

# gitignore
git rm --cached <file name>  # To ignore a file that is already checked in
git rm --cached -r <folder name>  # To ignore a folder that is already checked in
git config --global core.excludesfile ~/.gitignore_global  # And put in the files you want to ignore

# Rewriting git history
git rebase upstream/master
git rebase <branch name>  # To bring all the commits forward
git rebase -i HEAD~n  # n for which changes you want to make
# reword - to rename a commit
# drop - to delete a commit
# squash - to combine commits and give a name
# fixup - to combine commits and keep the name of base commit
# edit - to stop execution of rebase and if you wish, split the commits
# To reorder commits, just change their order in interactive rebase prompt
```
