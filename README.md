# Invite members in batch

This script is about a simple web interaction using Github API-[add-or-update-team-membership-for-a-user](https://docs.github.com/en/rest/reference/teams#add-or-update-team-membership-for-a-user) and adopted from the python implementation of [Auto Invite To The Organization By Star](https://github.com/BaseMax/AutoInviteToOrgByStar#auto-invite-to-the-organization-by-star) by [Max Base](https://github.com/BaseMax). There're more interesting auto-inviting projects in this author's repos. 

## 1. Create a file with usernames/id/emails

Create a file with usernames and modify functions of read files accordingly.

## 2. Run the InviteByUsername.py

Before you run the script, remember to edit the vairiables so that you can add members to the correct org and team.

### Workflow:

find usernames by searching id or email if necessary -> check username in the team or not -> make a invitation request -> record errors