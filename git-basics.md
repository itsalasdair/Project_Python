# Install Git
apt install -y git

# Configure user and email
- Not used to login, used to track changes
git config --global user.name "My Name"
git config --global user..email "myemail@domain.com"

# Initialise your Local Repository
- (Working Directory)
git init

# Track Changes and Status of Local/Remote Repos
git status

# Add to Staging
git add myfilename.cool

# Check Status
git status

# Commit to Remote Repository
git commit -m "My notes"
# -m = message

# Add the Remote Repository
git remote add origin https://github.com/username/repo.git

# Push the changes to the Remote Repository
git push -u origin master
# Committed!



# Git Commit Logs
git log


# Staging -> To Commit
