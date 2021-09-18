# Max Base
# 2021-06-19
# https://github.com/BaseMax/AutoInviteToOrgByStar

# Modified by Yiwei Liu
# 2021-9-17
# https://github.com/t07902301/eecs-1710
import requests,json

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
def get_username_by_id(user_id):
    url='https://api.github.com/user/{}'.format(user_id)
    headers={
        'Accept': 'application/vnd.github.v3+json',
    }
    response = requests.request("GET", url, headers=headers)
    try:
        return response.json()['login']
    except:
        print(user_id)
        with open('error.json','w') as f:
            json.dump(response.json(),f)
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
def invite(user):
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
    return response.json()
def add_users(usernames,existing_members):
    new_users=set(usernames)-set(existing_members)
    new_users=list(new_users)
    if len(new_users)==0:
        print('No new users.')
        return None
    error_msg=''
    for user in new_users:
        # if r'[a-z]' not in user or r'[A-Z]'not in user:
        #     search_by_id=get_username_by_id(user)
        #     print(user,search_by_id)
        #     user=search_by_id
        # else:
        #     print(user)
        print('Inviting @ '+user)
        invitation_result=invite(user)
        if 'message' in invitation_result:
            search_by_email=get_username_by_email(user)
            if search_by_email:
                invitation_result=invite(search_by_email)
            else:
                print('@ {} doesn''t exist or this email is used by one more users'.format(user))

            # else:
            #     search_by_id=get_username_by_id(user)
            #     if search_by_id:
            #         invitation_result=get_username_by_id(search_by_id)
            #     else:
            #         print('@ {} doesn''t exist'.format(user))
            print('Error @ {}'.format(user))
            print(invitation_result.text)
    
    # # Dump error msgs into files
    # if error_msg !='':
    #     with open('error_record.txt','w') as error_record:
    #         error_record.write(error_msg)
    #         print('error_record saved')
def main():
    usernames=get_username()
    old_members=get_members()
    add_users(usernames,old_members)
if __name__ == '__main__':
    main()
