

import requests
from bs4 import BeautifulSoup as Soup
import time
import json
import collections

from urlparse import urlparse
from threading import Thread
import httplib, sys
from Queue import Queue


# with open('average.json') as data_file:
#     modes = json.load(data_file)
#
# print modes['Stephen Curry']

# def addToDict (key, d, cb):
#     if (not key in d.keys()):
#         d[key] = {}
#
#     d[key] = cb(d[key])
#     return d
#
# def addPlayerStat (key, playerGame):
#     player = playerGame['player']
#     value = playerGame[key]
#
#     def getStat(key, playerDict):
#         return addToDict(key, playerDict, lambda d: getStatValue(value, d))
#
#     def getStatValue (key, statDict):
#         if (key in statDict.keys()):
#             statDict[key] += 1
#         else:
#             statDict[key] = 1
#         return statDict
#
#     return addToDict(player, modes, lambda d: getStat(key, d))
#
# for playerGame in table:
#     for key in playerGame.keys():
#         addPlayerStat(key, playerGame)
#
# for name in modes.keys():
#     mode = modes[name]
#     finalModes[name] = {}
#     for prop in mode.keys():
#         maxi = -1
#         maxv = ''
#         for value in mode[prop].keys():
#             if mode[prop][value] >= maxi:
#                 maxi = mode[prop][value]
#                 maxv = value
#
#         finalModes[name][prop] = maxv
#
#
# print finalModes['Tyler Zeller']
#
# with open('average.json', 'w') as write_file:
#     json.dump(finalModes, write_file)

# offsetIndex = 291
# print(len(table))

playerData = []

def concurrentRequests (urls, shouldQuitFor):
    concurrent = 200
    results = []

    def doWork():
        while True:
            url = q.get()
            result = getResult(url)
            doSomethingWithResult(result)
            q.task_done()

    def getResult(ourl):
        try:
            return requests.get(ourl).content
        except:
            return "error"

    def doSomethingWithResult(result):
        results.append(result)

    q = Queue(concurrent * 2)
    for i in range(concurrent):
        t = Thread(target=doWork)
        t.daemon = True
        t.start()
    try:
        count = 0;
        for url in urls:
            count += 1;

            if count > 200:
                count = 0
                if shouldQuitFor(url):
                    break;

            q.put(url.strip())
        q.join()

        return results
    except KeyboardInterrupt:
        sys.exit(1)

def getData ():
    global playerData

    if len(playerData) == 0:
        with open('data.json') as data_file:
            playerData = json.load(data_file)

    print(len(playerData))

    return (0, playerData[1:])

def writeData (today, data):
    global playerData
    data = [today] + data
    playerData = data

    with open('data.json', 'w') as fp:
        json.dump(data, fp)

def updateDataIfNeeded ():
    fields = ['rk', 'player', 'age', 'pos', 'date', 'tm', 'home', 'opp', 'res', 'gs', 'mp', 'fg', 'fga', 'fg%', '2p', '2pa', '2p%', '3p', '3pa', '3p%', 'ft', 'fta', 'ft%', 'orb', 'drb', 'trb', 'ast', 'stl', 'blk', 'tov', 'pf', 'pts', 'gmsc']
    table = []
    modes = {}
    finalModes = {}

    (writeDate, data) = getData()

    today = time.time()

    if writeDate + 86400 < today:

        def urls ():
            offsetIndex = 0
            while True:
                yield 'http://www.basketball-reference.com/play-index/pgl_finder.cgi?request=1&player_id=&match=game&year_min=2015&year_max=2016&age_min=0&age_max=99&team_id=&opp_id=&is_playoffs=N&round_id=&game_num_type=&game_num_min=&game_num_max=&game_month=&game_location=&game_result=&is_starter=&is_active=&is_hof=&pos_is_g=Y&pos_is_gf=Y&pos_is_f=Y&pos_is_fg=Y&pos_is_fc=Y&pos_is_c=Y&pos_is_cf=Y&c1stat=&c1comp=gt&c1val=&c2stat=&c2comp=gt&c2val=&c3stat=&c3comp=gt&c3val=&c4stat=&c4comp=gt&c4val=&is_dbl_dbl=&is_trp_dbl=&order_by=player&order_by_asc=&offset=' + str(offsetIndex*100)
                offsetIndex += 1

        def shouldQuitFor (url):
            document = Soup(requests.get(url).content, 'lxml')
            tree = document.select('table.stats_table tbody tr td')

            if len(tree) == 0:
                return True

            return False

        print "Fetching player games..."
        results = concurrentRequests(urls(), shouldQuitFor)
        print "Fetched about " + str(len(results)*100) + " results"

        print "Parsing data..."

        for data in results:
            start = time.time()

            # Parse
            document = Soup(data, 'lxml')
            tree = document.select('table.stats_table tbody tr td')
            if (len(tree) == 0):
                print data
                break

            currentDoc = {}
            currentFieldIndex = 0
            currentField = fields[currentFieldIndex]
            for node in tree:
                if currentField == 'rk':
                    pass
                elif currentField == 'player' or currentField == 'date' or currentField == 'tm' or currentField == 'opp':
                    currentDoc[currentField] = node.a.string
                elif currentField == 'res' or currentField == 'age' or currentField == 'pos' or currentField == 'home':
                    currentDoc[currentField] = node.string
                else:
                    if node.string != None:
                        currentDoc[currentField] = float(node.string)
                    else:
                        currentDoc[currentField] = None

                if currentFieldIndex == 32:
                    currentFieldIndex = 0
                    table.append(currentDoc)
                    currentDoc = {}
                else:
                    currentFieldIndex += 1

                currentField = fields[currentFieldIndex]

            # gameID = 0
            # for game in data:
            #     teamed = {}
            #     for gameGamed in data:
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

            end = time.time()

            print(len(table))
            print 'time:' + str(end - start)



        writeData(today, table)


updateDataIfNeeded()
