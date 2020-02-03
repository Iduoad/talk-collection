---
title: 7 Tips to Pimp Your Git History
description: Roland talks about ways to make your git history look better.
type: talk
speaker: Roland Weisleder
source: https://www.youtube.com/watch?v=prlYwbCHTdE
---
- Initial commits should be as small as possible. you should avoid putting to much into it. (blackhole)
- Write commit messages for your reader. Commit messages should express what changes were made, in a way readers can follow easily.
- Write concise commit summaries, commit messages should be around 50 characters.
- Commits should be atomic, if a commit changed more stuff it shoud be put into seperate commits.
- Add the context of the commit into the commit message e.g add links to issues and stackoverflow answers.
- Use `git add -p` to add changes separately to the next commit.
- Separte changes from refactoring, by adding a hint to the commit message. e.g. `git commit -m "refactoring: my commit message`
- Use `git commit --amend` to edit last commit
- Interactive rebasing is cool `git rebase -i`.
