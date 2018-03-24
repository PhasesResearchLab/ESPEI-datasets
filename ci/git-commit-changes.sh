#!/usr/bin/env bash

# We expect that this can "fail". If there are no changes, there should be nothing to commit.
# Modified from https://gist.github.com/willprice/e07efd73fb7f13f917ea

# Set up git
git config --global user.email "travis@travis-ci.org"
git config --global user.name "Travis CI"

# have to checkout otherwise we'll be detached
git checkout $TRAVIS_BRANCH

# add all the files and commit
git add -A
# we added miniconda and have to remove it
git reset HEAD miniconda.sh
git commit -m "LINT: Travis CI automated linting [ci skip]"

# upload
git remote add origin-travis https://${GH_TOKEN}@github.com/phasesresearchlab/espei-datasets.git > /dev/null 2>&1
git push --quiet --set-upstream origin-travis $TRAVIS_BRANCH > /dev/null 2>&1
