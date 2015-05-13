#!/bin/bash
branch=$1
branchName=$1
if [[ $branchName == refs/heads/* ]]; then
  branchName=${branchName:11}
fi

branchRemote=`git config branch.$branchName.remote`
branchMerge=`git config branch.$branchName.merge`

if [ "$branchRemote" == "" ] || [ "$branchMerge" == "" ]; then
  echo "Branch '$branch' is not tracking any remote branch."
  exit 1;
fi

if ! [[ $branchMerge == refs/heads/* ]]; then
  echo "Branch '$branch' is tracking invalid branch '$branchMerge'."
  exit 1;
fi

upstream="refs/remotes/$branchRemote/${branchMerge:11}"
upstreamSha=`git show-ref --hash $upstream`
if [ "$upstreamSha" == "" ]; then
  echo "Upstream '$upstream' not found."
  exit 1;
fi

branchSha=`git show-ref --hash $branch`
if [ $upstreamSha == $branchSha ]; then
  echo "Branch '$branch' is already identical with '$upstream'."
  exit 0;
fi

git merge-base --is-ancestor $branch $upstreamSha
if ! [[ $? == 0 ]] ; then
  echo "Upstream '$upstream' is not ahead of '$branch'."
  exit 1;
fi

head=`git rev-parse --symbolic-full-name HEAD`
if [ $head == $branch ]; then
  git merge --ff-only $upstream
else
  git update-ref $branch $upstreamSha
fi

