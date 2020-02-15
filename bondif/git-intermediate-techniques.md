---
title: Git Intermediate Techniques
description: Kevin shows us concepts that can help us work more efficiently with the popular open-source version control software.   
NB: This is not a full course summary, but just what I found most useful in day to day work with Git.   
instructor: Kevin Skoglund   
source: https://www.linkedin.com/learning/git-intermediate-techniques   
tags: ['Git', 'VCS']
---
- Delete branch : `git branch -d new_feature` or `git branch -D new_feature` to force deletion.   
- Delete remote branch : `git push --delete origin new_feature`
- List remote branches : `git branch -r`
- Rebase the current branch to the tail of the master branch : `git rebase master`
- Rebase the new_feature to the tail of the master branch : `git rebase master new_feature`
- Interactive rebase (new feature onto master) : `git rebase -i master new_feature`
- Rebase last 3 commits onto the same branch but with the opportunity to modify them : `git rebase -i HEAD~3`
- Pull with rebase : `git pull --rebase`
- List commits with diffs : `git log -p` or `git log --patch`
- List edits between lines 100 and 150 in filename : `git log -L 100,150:filename`
- Annotate file with commit details and ignore whitespaces : `git blame -w filename`
