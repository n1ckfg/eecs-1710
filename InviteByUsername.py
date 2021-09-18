# Max Base
# 2021-06-19
# https://github.com/BaseMax/AutoInviteToOrgByStar

# Modified by Yiwei Liu
# 2021-9-17
# https://github.com/t07902301/eecs-1710
import requests

personal_access_token = '' # Get it from your developer setting on Github
org_name=''
team_name = '' 
txt_file='demo.txt'

def get_username():
    '''
    e.g. usernames are stored in a text file
    '''
    with open(txt_file) as userfile:
        usernames=[user.split('\n')[0] for user in userfile.readlines()]
    return usernames
def get_members():
    url='https://api.github.com/orgs/{org}/teams/{team_slug}/members'.format(org=org_name,team_slug=team_name)
    headers={
    'Accept': 'application/vnd.github.v3+json',
    'Authorization': 'token '+personal_access_token
    }
    response = requests.request("GET", url, headers=headers)
    old_users=[user['login'] for user in response.json()]
    return old_users
def add_users(usernames,existing_members):
    new_users=set(usernames)-set(existing_members)
    new_users=list(new_users)
    if len(new_users)==0:
        print('No new users.')
        return None
    error_msg=''
    for user in new_users:
        print('Inviting @ '+user)
        url = 'https://api.github.com/orgs/{org}/teams/{team_slug}/memberships/{username}'.format(org=org_name,team_slug=team_name,username=user)
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
            print('Error @ {}'.format(user))
            print(response.text)
            # error_msg+='Error @ {}'.format(user)+'\n'+response.text+'\n'
    # if error_msg !='':
    #     with open('error_record.txt','w') as error_record:
    #         error_record.write(error_msg)
    #         print('error_record saved')
def main():
    usernames=get_username()
    old_members=get_members()
    add_users(usernames,old_members)
    # print(add_users(usernames,old_members))
if __name__ == '__main__':
    main()
