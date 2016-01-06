
import json
import itertools

# Get averages for all other players

# with open('average.json') as data_file:
#     averages = json.load(data_file)
#
#
# # Identify games
#
# with open('data.json') as data_file:
#     games = json.load(data_file)
#
# player = 'Deron Williams'
#
# lineups = [{
#     'PG': ['Deron Williams', 'T.J. McConnell'],
#     'SG': ['Wesley Matthews', 'Nik Stauskas'],
#     'SF': ['Chandler Parsons', 'Jerami Grant'],
#     'PF': ['Dirk Nowitzki', 'Nerlens Noel'],
#     'C': ['Zaza Pachulia', 'Jahlil Okafor']
# }]
#
# usingfields = ['gs', 'mp', 'fg', 'fga', '2p', '2pa', '3p', '3pa', 'ft', 'fta', 'orb', 'drb', 'trb', 'ast', 'stl', 'blk', 'tov', 'pf', 'pts', 'gmsc']

# class Playerdata:
#     def __init__(self, lineups, games):
#         self.
#
#     def getSixGameAverage(self, player):
#         pass
#
#     def ajustToLatest(self, player):
#
#     def (self, player):
#         pass
#
# x = Playerdata(linups, games)
#
# class FuturePattern:
#     def __init__(self, data):
#         data
#
#     def permute(self, length, data, out):
#
#     def compareData(self, data):
#
#
#     def quantify(field, value):
#         pass

ops = [1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10]
j = 0
for i in itertools.permutations(ops):
    j += 1

print j

[a b c]

[d e b]

###
# tag gameids
###

# gameID = 0
# for game in games:
#     teamed = {}
#     for gameGamed in games:
#         if gameGamed['date'] == game['date'] and (gameGamed['tm'] == game['tm'] or gameGamed['opp'] == game['tm']):
#             teamed = gameGamed
#             break
#
#     if teamed == game:
#         gameID += 1
#         game['game'] = gameID
#
#     else:
#         game['game'] = teamed['game']
#
# with open('data.json') as data_file:
#     games = json.dump(games, data_file)
