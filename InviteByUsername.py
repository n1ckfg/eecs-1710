# Max Base
# 2021-06-19
# https://github.com/BaseMax/AutoInviteToOrgByStar

# Modified by Yiwei Liu
# 2021-9-17
# https://github.com/t07902301/eecs-1710
import requests,json,re

#Open config file and load your github information
with open('config.json','r') as config:
    config_file=json.load(config)

personal_access_token = config_file['personal_access_token'] # Get it from your developer setting on Github
org_name=config_file['org_name']
team_name = config_file['team_name'] 
user_info=config_file['user_info']

def load_username_file():
    '''
    e.g. usernames are stored in a text file(.txt)
    '''
    with open(user_info) as userfile:
        usernames=[user.rstrip() for user in userfile]
        usernames=[user for user in usernames if user]
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
def get_username_by_id(user_id):
    url='https://api.github.com/user/{}'.format(user_id)
    headers={
        'Accept': 'application/vnd.github.v3+json',
        'Authorization': 'token '+personal_access_token
    }
    response = requests.request("GET", url, headers=headers)
    try:
        return response.json()['login']
    except:
        print('invalid id %s'%user_id)
        with open('error.json','w') as f:
            json.dump(response.json(),f,indent=4)
        return None
def get_username_by_email(user_email):
    url='https://api.github.com/search/users?q={}+in:email'.format(user_email)
    headers={
        'Accept': 'application/vnd.github.v3+json',
    }   
    response = requests.request("GET", url, headers=headers).json()
    if response['total_count']!=1:
        return False
    else:
        return response['items'][0]['login']
def invite_request(user):
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
    return response
def get_username(user_info):
    if re.search('^\d*$',user_info):
        sereach_by_id=get_username_by_id(user_info)
        if sereach_by_id is None:
            print('invalid id %s'%user_info)
            return None
        else:
            return sereach_by_id
    elif re.search('.*@.*\.com',user_info):
        search_by_email=get_username_by_email(user_info)
        if search_by_email is False:
            print('invalid email %s'%user_info)
            return None
        else:
            return search_by_email
    else:
        return user_info
def add_users(usernames,existing_members):
    usernames=[get_username(user) for user in usernames]
    new_users=set(usernames)-set(existing_members)
    new_users=list(new_users)
    if len(new_users)==0:
        print('No new users.')
        return None
    error_msg=''
    for user in new_users:
        if user: # the username exists
            print('Inviting @ '+user)
            response=invite_request(user)
            if 'message' in response.json():
                print('Error @ {}'.format(user))
                print(response.text)

    # # Dump error msgs into files
    # if error_msg !='':
    #     with open('error_record.txt','w') as error_record:
    #         error_record.write(error_msg)
    #         print('error_record saved')
def main():
    usernames=load_username_file()
    old_members=get_members()
    print('got existig members')
    add_users(usernames,old_members)
    print('inivitation is done')
    # print(usernames)
if __name__ == '__main__':
    main()
