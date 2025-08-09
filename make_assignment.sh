#!/usr/bin/env bash

# CHANGE THESE FOR YOUR REPO!
GITHUB_REPO='git@github.com:HaileyHL/gradescope-python-autograder-template.git'
REPO_NAME="gradescope-python-autograder-template"

# usage: ./make_assignment.sh <assignment_name>
name=${1:-}
if [ -z "${name}" ]; then
  echo "Usage: $0 <assignment_name>"
  exit 1
fi

# we always use a folder named 'solution' now
solution_dir="solution"

# delete previous file if any
rm -f "$name.zip"

# stage files for the zip
mkdir -p "zip_$name"

# copy everything Gradescope needs
cp gradescope_base/* "zip_$name/"            # run_autograder, ssh_config, deploy_key, etc.
cp setup.sh "zip_$name/setup.sh"             # <-- ensure setup.sh is included

# inject variables into run_autograder and setup.sh
sed "s/REPLACE_NAME/NAME=$name/"                    "zip_$name/run_autograder" > /tmp/run_autograder && mv /tmp/run_autograder "zip_$name/run_autograder"
sed "s/REPLACE_SOLUTION_DIR/SOLUTION_DIR=$solution_dir/" "zip_$name/run_autograder" > /tmp/run_autograder && mv /tmp/run_autograder "zip_$name/run_autograder"
sed "s/REPLACE_REPO_NAME/REPO_NAME=$REPO_NAME/"     "zip_$name/run_autograder" > /tmp/run_autograder && mv /tmp/run_autograder "zip_$name/run_autograder"

sed "s/REPLACE_REPO_NAME/REPO_NAME=$REPO_NAME/"     "zip_$name/setup.sh" > /tmp/setup.sh && mv /tmp/setup.sh "zip_$name/setup.sh"
sed "s,REPLACE_GITHUB_REPO,GITHUB_REPO=$GITHUB_REPO," "zip_$name/setup.sh" > /tmp/setup.sh && mv /tmp/setup.sh "zip_$name/setup.sh"

# zip (flatten) and clean up
zip -r -m -j "$name.zip" "zip_$name"/*
rmdir "zip_$name"
