#!/usr/bin/env bash
# make_assignment.sh will replace the lines below, DO NOT REMOVE
REPLACE_GITHUB_REPO
REPLACE_REPO_NAME

cd /autograder/source

apt-get install -y python3 python3-pip python3-dev

mkdir -p /root/.ssh
cp ssh_config /root/.ssh/config
cp deploy_key /root/.ssh/deploy_key
chmod 400 /root/.ssh/deploy_key
ssh-keyscan -t rsa github.com >> ~/.ssh/known_hosts

git clone $GITHUB_REPO /autograder/$REPO_NAME
pip3 install -r /autograder/$REPO_NAME/requirements.txt
