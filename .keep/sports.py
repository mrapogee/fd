
import requests
from lxml import html


fanheaders = {
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'Authorization': 'Basic N2U3ODNmMTE4OTIzYzE2NzVjNWZhYWFmZTYwYTc5ZmM6',
    'Origin': 'https://www.fanduel.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2560.0 Safari/537.36',
    'Accept': 'application/json, text/plain, */*',
    'X-FirePHP-Version': '0.0.6',
    'Referer': 'https://www.fanduel.com/games',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'en-US,en;q=0.8'
}

# r = requests.get('http://www.footballdb.com/players/deandre-hopkins-hopkide01')
# tree = html.fromstring(r.content)

# stats = tree.xpath('//')

###
# Pick games (least populated/most prize) TODO find best games. For now, will choose myself
###

'''
# Get NBA fixture list
lists = requests.get('https://api.fanduel.com/contests?fixture_list=13569&include_restricted=true', headers=fanheaders)
listID = filter(
    lambda e: e['sport'] == 'NBA',lists.json()['fixture_lists']
    )[0]['id']

# get games
contests = requests.get(
    'https://api.fanduel.com/contests?fixture_list=' + listID + '&include_restricted=true',
     headers=fanheaders).json()['contests']

# get teams, pricing for each game
cheapContests = filter(lambda e: e['entry_fee'] == 1, contests)
print len(cheapContests)
'''

contestID = '13569-18857667'

contest = requests.get('https://api.fanduel.com/contests/' + contestID,
    headers=fanheaders)

teams = map(lambda e: e['code'] ,contest.json()['teams'])
print(teams)

# Get the players in the gamees



# Identify worst/best of teams



# Compare teams history
# Identify cheapest/most performance players
# Choose players
