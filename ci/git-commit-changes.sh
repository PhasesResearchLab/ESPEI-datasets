#!/usr/bin/env bash

# We expect that this can "fail". If there are no changes, there should be nothing to commit.
# Modified from https://gist.github.com/willprice/e07efd73fb7f13f917ea

# Set up git
git config --global user.email "travis@travis-ci.org"
git config --global user.name "Travis CI"


git branch -v

# add all the files and commit
git add -A
git commit -m "LINT: Travis CI automated linting [ci skip]"

# upload
git remote add origin https://${GH_TOKEN}@github.com/phasesresearchlab/espei-datasets.git > /dev/null 2>&1
git push --quiet --set-upstream origin $TRAVIS_BRANCH > /dev/null 2>&1
