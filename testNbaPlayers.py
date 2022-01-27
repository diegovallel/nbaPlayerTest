import requests


class NBAPlayer:

    NBAPlayerList = []

    NBAPlayersLength = 0

    countPlayer = 0

    pairHeightPlayers = "Pair Height Players: \n"

    flagMatchFound = False

    URL = ''

    def __init__(self):
        self.URL = 'https://mach-eight.uc.r.appspot.com'

        self.callServie()

        self.NBAPlayersLength = len(self.NBAPlayerList)
    
    def callServie(self):
        r = requests.get(url = self.URL)

        data = r.json()
        
        self.NBAPlayerList = data['values']
    
    def pairHeights(self, height):

        player = self.NBAPlayerList[self.countPlayer]

        playerList = self.NBAPlayerList[(self.countPlayer+1)::]

        heightDiff = height - int(player['h_in'])
        
        if (heightDiff > 0):
                for playerPair in playerList:
                    if (int(playerPair['h_in']) == heightDiff):
                        self.flagMatchFound = True
                        self.pairHeightPlayers += "- " + player['first_name'] + " " + player["last_name"] + "    " +  playerPair['first_name'] + " " + playerPair["last_name"] + "\n"
        
        self.countPlayer += 1

        if (self.countPlayer < self.NBAPlayersLength):

            self.pairHeights(height)
        
    def displayResult(self):
        if (self.flagMatchFound):
            return self.pairHeightPlayers
        else:
            return "No match found"
        

if __name__ == '__main__':
    nbaPlayers = NBAPlayer()

    height = input("Please enter the height to match: ")

    if height.isdigit():
        nbaPlayers.pairHeights(int(height))

        print(nbaPlayers.displayResult())
    else:
        print("The value must be a numeric (integer)")


    

    