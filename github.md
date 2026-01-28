### A learning playground for Git and GitHub.

`git --version` ⌘ Check version of git

`git config --global user.name "<user-name>"` ⌘  Configure user-name globally in system, without value prints already configured value

`git config --global user.email "<user-email>"` ⌘ Configure user email globally in the system, without value prints already configured value

`git config --global alias.<shortcut> <git-command>` ⌘ Create a global alias for git command as shortcut

`git config --global --list` ⌘ Configure list of configured values in the system

`git init` OR `git init .` OR `git init <folder-name>` ⌘ Create a git repository

`git add .` OR `git add <file1>...<fileN>` OR `git add --all` ⌘ Add one or more files to staging area

`git status` ⌘ Check the status of git repository

`git commit -m <commit-message>` ⌘ Commit the changes into local repository

`git commit -am <commit-message>` ⌘ Commit the changes without moving to stage area, works only for tracked files

`git commit -m ammend` ⌘ Rewrite a commit message

`git log` or `git log --oneline` ⌘ Print logs with details and oneline

`git log --online --graph --all` ⌘ Graph of oneline logs

`git log grep="<pattern>"` ⌘ List logs based on the pattern in commits 

`git diff <filename>` ⌘ Show difference between local directory and staging area

`git diff HEAD <filename>` ⌘ Show difference between local directory and local repository

`git diff --staged <filename>` ⌘ Show difference between staging area and local repository

`.gitignore` ⌘ Create a file in repository to ignore pattern based file/s from tracking in repository

`git annotate <filename>` ⌘ Shows the author and commit information for each line of a given file

`git rm <filename>` ⌘ Remove file from repository

`git rm --cached <filename>` ⌘ Clear git cache

`git mv <old-location> <new-location>` ⌘ Move files within repository

`git restore <file-name>` ⌘ Restore a file to its last committed state

`git checkout -- <file-name>` ⌘ Revert changes from working directory

`git restore --staged <file-name>` ⌘ Unstage a file from staging area to working area

`git checkout -- <filename>` ⌘ Undo filename changes to last commit by discarding 

`git checkout -f` ⌘ Rollback to previous commit of local repository

`git branch` ⌘ List branches in a git repository

`git branch -v` ⌘ Last commit in a branch

`git branch <branch-name>` ⌘ Create a new branch

`git checkout <branch-name>` ⌘ Switch a branch

`git checkout -b <branch-name>` ⌘ Create and switch to a new branch

`git checkout <commit-ID>` ⌘ Navigate to the specific commit ID and `git switch -` to go back to HEAD of branch

`git switch -c <branch-name>` ⌘ Create a branch after specific commit checkout

`git branch -d <branch-name>` ⌘ Delete a branch

`git branch -D <branch-name>` ⌘ Forceful deletion of a branch as you can not delete branch without merge

`git branch -a` ⌘ Lists all local and remote branches

`git remote add alias <URL>` ⌘ Create an alias = 'origin' for remote URL

`git remote` ⌘ List configured remote alias

`git remote -v` ⌘ # List configured remote alias details in verbose format

`git push <alias> <branch-name>` ⌘ Push changes from local branch to remote branch

`git push -f` ⌘ Forcefully push the local changes to remote repository

`git clone <URL>` ⌘ Create a copy of a remote repository

`git remote rename <old-name> <new-name>` ⌘ Rename old remote with new remote

`git remote remove <remote-name>` ⌘ Remove the remote alias

`git remote set-url <alias> <URL>` ⌘ Set new alias URL for remote

`git show <commit-ID>` ⌘  Inspect various Git objects, such as commits, tags, trees, and blobs

`git tag` ⌘ Lists all local tags

`git tag <tag-name> <commit-ID>` ⌘ Create a tag at HEAD or optional commit-ID

`git tag -a <tag-name> <commit-ID> -m <message>` ⌘ Create an annotated tag for specific commit with message

`git tag -d <tag-name>` ⌘ Delete a tag

`git show <tag-name>` ⌘ Displays details about a specific tag, including the commit it points to and its message

`git push origin <tagname>` ⌘ Pushes a specific local tag to the remote repository

`git push --tags` ⌘ Push all local tags to remote repository

`git push origin -d <tag-name>` ⌘ Delete tag from remote repository

`git fetch origin --tags` ⌘ Fetches all tags from the remote repository that are not already present locally

`git stash` ⌘ Stash the work from staging area to stashing area

`git stash list` ⌘ ⌘ List the stash from the stashing area

`git stash show <stash-ID>` ⌘ ⌘ Show details about specific stash

`git stash drop` ⌘ ⌘ Drop the top most stash from the stashing area

`git stash pop` ⌘ Pop the first stash from the stashing area and remove from stack [LIFO]

`git stash apply <stash-ID>` ⌘ ⌘ Apply the specific stash, keep in stack

`git stash clear` ⌘ Clear the stashing stack

`git clean -f` ⌘ Clean the working area completely 

`git revert <commit-ID>` ⌘ Undo a specific commit

`git revert -n <commit-ID>` ⌘ Revert specific N commit

`git revert --abort` ⌘ Abort the revert of commit

`git reset --mixed <commit-ID>` # By default it's mixed reset, keeps your changes in working area

`git rest --soft <commit-ID>` ⌘ Keeps your changes staged for recommit

`git reset --hard <commit-ID>` ⌘ completely discards both staged and working directory changes, making it the most destructive option.

`git cherry-pick <commit-ID>` ⌘ Pick specific commit and merge into current branch

`git rebase -i HEAD~N` ⌘ Squeeze N commits into one commit interactively, squash commit, Reword/Reorder commit, Drop/Delete commit, exec a custom command in between commands

`git bisect start` ⌘ Start the debugging process with start. Bisect helps to identify the git commit which introduced the bug in the repository | `git bisect bad <commit-ID>` && `git bisect good <commit-ID>`









































