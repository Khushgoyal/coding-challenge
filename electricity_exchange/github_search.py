from github import Github
import requests
import json
from variables import ACCESS_TOKEN

#accessing github token key
g = Github(ACCESS_TOKEN)
endpoint = r'https://api.github.com/search/repositories'

#This param is the query which is used in the url 
params = {'q':'Reactive'}

g = Github(ACCESS_TOKEN)
search_words = []
#Function for search reactive in the search bar
def search_github(endpoint,params):
    
    rate_limit = g.get_rate_limit()
    rate = rate_limit.search
    
    #Check the conditon for the api limit.
    if rate.remaining == 0:
        print(f'You have 0/{rate.limit} API calls remaining. Reset time: {rate.reset}')
        return
    else:
        print(f'You have {rate.remaining}/{rate.limit} API calls remaining')
        
    ret = requests.get(endpoint,params=params)
    output = json.loads(ret.content)
    for i in output['items']:
        search_word = i['full_name']
        search_words.append(search_word)
    print(search_words)
    

if __name__ == '__main__':
    search_github(endpoint,params)
    

