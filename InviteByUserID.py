# Max Base
# 2021-06-19
# https://github.com/BaseMax/AutoInviteToOrgByStar

# Modified by Yiwei Liu
# 2021-9-17
#
import requests

personal_access_token = '' # Get it from your developer setting
org=''# organization name
team_slug = '' #your team's name
users_list=''
with open(users_list) as userfile:
    user_names=[user.split('\n')[0] for user in userfile.readlines()]
for user in user_names:
    print('Inviting @ '+user)
    # TODO: check the user already joined or no/ update the user'role in the team
    url='https://api.github.com/orgs/{}/teams/{}/memberships/{}'.format(org,team_slug,user)
    payload=''
    # payload={
    #     'role':'member'
    # }
    headers = {
        'Accept': 'application/vnd.github.v3+json',
        'Authorization': 'token '+personal_access_token
    }
    response = requests.request("PUT", url, headers=headers, data=payload)
    # print(response.text)
    if 'message' in response.json():
        print('Error @ '.format(user))
        print(response.text)
