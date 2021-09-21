# Invite members in batch

This script is about a simple web interaction using Github API-[add-or-update-team-membership-for-a-user](https://docs.github.com/en/rest/reference/teams#add-or-update-team-membership-for-a-user) and adopted from the python implementation of [Auto Invite To The Organization By Star](https://github.com/BaseMax/AutoInviteToOrgByStar#auto-invite-to-the-organization-by-star) by [Max Base](https://github.com/BaseMax). There're more interesting auto-inviting projects in this author's repos. 

## 1. Create a file with usernames/id/emails

Create a file with usernames(e.g. example_users.txt in this repo) and modify functions of reading/loading files accordingly. 

## 2. Run the InviteByUsername.py

Before you run the script, remember to edit the global vairiables in the config json file (e.g. examples_config.json). These variables are about your personal information in Github and help you to add members to the correct org and team. 

### Replace the name of user_info file in config with your own file
```
{
    "personal_access_token" : "(Get it from your developer setting on Github)",  
    "org_name":"",
    "team_name" : "" ,
    "user_info":"example_users.txt"
}
```
### Replace the name of config json file with your own config
```
#Open your config file and load your github information
with open('examples_config.json','r') as config:
    config_file=json.load(config)
``` 

### Workflow:

find usernames by searching id or email if necessary -> check username in the team or not -> make a invitation request -> record errors