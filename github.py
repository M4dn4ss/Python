import requests
import json
class Github:
    def __init__(self):
        self.api_url = "https://api.github.com"
        self.token = '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'
    
    def getUser(self, username):
        response = requests.get(self.api_url + "/users/" + username)
        return response.json()

    def getRepositories(self, username):
        response = requests.get(self.api_url + '/users/' + username + '/repos')
        return response.json()
    
    def authorize(self):
        pass

    def createRepository(self, name):
        description = "Created with api"

        payload = {'name':name,'description':description,'auto_init': 'true'}        
        login = requests.post('https://api.github.com/' + 'user/repos', auth=('user','token'), data=json.dumps(payload))




github = Github()

while True:
    choice = input("1- Find User\n2- Get Repositories\n3- Create Repository\n4- Exit\nChoice: ")

    if choice == '4':
        break
    else:
        if choice == '1':
            username = input("Username: ")
            result = github.getUser(username)
            print(f"name: {result['name']} public repos: {result['public_repos']} follower: {result['followers']}")
        elif choice == '2':
            username = input('Username: ')
            result = github.getRepositories(username)
            for repo in result:
                print(repo['name'])
        elif choice == '3':
            name = input('repository name:')
            result = github.createRepository(name)
            print(result)
        else:
            print("Wrong choice")