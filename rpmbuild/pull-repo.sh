#!/bin/bash
#
# Prepare a git repository for use.

usage() {
  cat << EOF
  usage: $0 [options] path

  This script prepares a git repository for use. Typically used within
  a makefile to pull and prep a repository for a build process.

  OPTIONS:
  -h          Show this message
  -b branch   The branch to pull: defaults to 'master'
  -r repo     The github repo URL suitable for use with git clone
  -s          Initialize submodules if repo is cloned
  -v          Make the operations verbose
EOF
}

BRANCH=master
REPO=
REPO_PATH=
INIT_SUBMODULES=false
QUIET="-q"

while getopts "hb:r:sv" OPTION
do
  case $OPTION in
    h)
      usage
      exit 1
      ;;
    b)
      BRANCH=$OPTARG
      ;;
    r)
      REPO=$OPTARG
      ;;
    s)
      INIT_SUBMODULES=true
      ;;
    v)
      QUIET=
      ;;
    ?)
      usage
      exit
      ;;
  esac
done

shift $((OPTIND-1))

# Verify that the path has been specified
[ $# -eq 1 ] || (echo "Must provide directory" && exit)
REPO_PATH=$1

# Verify that the github repo has been specified
[ ! -z "$REPO" ] || (echo "Must specify the github repo" && exit)

# First, get the commit hash of the desired branch/tag/version
commit=$(git ls-remote ${REPO} ${BRANCH} | cut -f 1)

# What we do next depends on whether the repo_path actually exists or not
if [ -d ${REPO_PATH} ]
then
  # Directory exists; move into the directory and make sure that we have
  # pulled the code from the repository, checkout the appropriate 
  # branch/tag/commit, then clean up the working directory.
  cd ${REPO_PATH} && \
    git fetch ${QUIET} origin && \
    git fetch --tags ${QUIET} origin && \
    git reset ${QUIET} --hard ${commit} && \
    git clean ${QUIET} -d -x -f
else 
  # Directory didn't exist; go ahead and clone the repository
  # then checkout the requested branch/tag/commit
  git clone ${QUIET} ${REPO} ${REPO_PATH} && \
    cd ${REPO_PATH} && \
    if [ $INIT_SUBMODULES == true ]; then git submodule init; git submodule update; fi && \
    git checkout ${QUIET} ${commit}
fi
