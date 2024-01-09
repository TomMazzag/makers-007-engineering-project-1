# Flask HTML Web & Database Project Starter

This is a starter project for you to use to start your Flask HTML web & database
projects.

It contains quite a lot of example code. You can use this to see how the various
parts of the project work, or you can delete it and start from scratch.

There are two videos to support:

- [A demonstration of setting up the project](https://www.youtube.com/watch?v=YStsRfMVx44&t=0s)
- [A walkthrough of the project codebase](https://www.youtube.com/watch?v=YStsRfMVx44&t=314s)

## Setup

```shell
# Clone the repository to your local machine
; git clone https://github.com/JonnySB/makers-007-engineering-project-1.git

; cd makers-007-engineering-project-1

# Install dependencies and set up the virtual environment
; pipenv install

# Activate the virtual environment
; pipenv shell

# Install the virtual browser we will use for testing
; playwright install
# If you have problems with the above, contact your coach

# Create a test and development database
; createdb MAKERS_BNB
; createdb MAKERS_BNB_test

# Open lib/database_connection.py and change the database names
; open lib/database_connection.py

# Seed the development database (ensure you have run `pipenv shell` first)
; python seed_dev_database.py

# Run the tests (with extra logging)
; pytest -sv

# Run the app
; python app.py
# Now visit http://localhost:5001/emoji in your browser
```

If you would like to remove the example code:

```shell
; ./remove_example_code.sh
```

# Git and Github Developer Workflow

## 1. Pick a task

Before anything else, create a new branch locally to work on it.

```bash
# Make sure you're on main
# with the latest changes on main
# (this will help to avoid conflicts later on).
git checkout main
git pull origin main

# Create a new branch (branching out from main).
# Make sure the branch name is descriptive of the 
# task, bug or feature you're working on.
git checkout -b new-feature-calendar
```

## 2. Test-drive and Implement the feature

Then commit your work, and push the branch:

```bash
git add .

# Make sure the commit message is descriptive
# of the changes (so it's easier to find it later).
git commit -m "Implement the calendar feature on the booking page"

git push -u origin new-feature-calendar
```

## 3. Open a pull request

_The guidance below is for the developers who implemented the changes, and will open the PR - the PR's owners._

A pull request (PR), also called a _diff_, is a way to list all the changes you made on
your branch that are not on the `main` branch yet. By reviewing these changes, your team
is able to see what will get merged in the main branch, and have the opportunity to review
it and make suggestions to improve the code before it gets merged.

Make sure your PR's title and description contains enough details for someone else who's
not familiar with the code to review. Once the PR is created, send the link to your team.

## 4. Someone else reviews the PR

_The guidance below is for the developer who will review the PR._

A code review is usually a task done alone. This is because reviewing code takes a lot of
cognitive effort, so it's important to focus on the code and make note of anything you
feel should be changed.

Avoid suggesting too many things — focus on offering feedback to _improve_ the PR, by
pointing out a couple of changes you feel would be important (code readability, OOP and
design, improve the tests...), but also offer _validation_ feedback on something you think
was done really well.

When suggesting changes, try to tie it to the software engineering practices you've
learned and used so far, and make sure it will be useful to the PR's owner to improve the
code. Make it an observation, rather than a judgement, and always leave the room for
discussion in your feedback.

## 5. The PR owner will make changes based on the feedback

```bash
# Implement the changes and commit them.
git add .
git commit -m "Changed the method name based on PR feedback"
git push
```

## 6. The PR is merged

Merging the PR on Github means the branch is merged into `main` by Github on the central
repository. The task is done.

After this, make sure everyone pulls the latest version of `main`, before starting a new
branch.

```bash
git checkout main

git pull origin main
```

If you're already working on another branch, it's also good, before opening a PR, to merge
the latest `main` _into your branch_. This reduces the potential amount of changes between
your branch and `main`, and avoids having too many conflicts when opening a PR.

```bash
# On your feature branch.
git checkout new-feature-calendar

# Fetching and merging the latest main
# into your feature branch.
git fetch
git merge origin/main

# Push your feature branch.
git push origin new-feature-calendar
```




<!-- END GENERATED SECTION DO NOT EDIT -->
